#!/usr/bin/env bash
# Clear X Bookmarks + Likes after disk verify. Requires logged-in agent-browser session.
# Usage: BU_CDP_URL=http://127.0.0.1:PORT ./scripts/x_clear_lists.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export BU_CDP_URL="${BU_CDP_URL:?Set BU_CDP_URL to agent-browser Chrome CDP (not 9222 Grok Bot)}"

ab_url() {
  ab_tab_x
  agent-browser eval "location.href" | tr -d '"'
}

ab_tab_x() {
  agent-browser tab x 2>/dev/null || agent-browser tab t9 2>/dev/null || true
}

ab_eval_x() {
  ab_tab_x
  agent-browser eval "$1"
}

extract_ids() {
  ab_tab_x
  agent-browser eval "JSON.stringify([...new Set([...document.querySelectorAll('a[href*=\"/status/\"]')].map(a=>(a.href.match(/status\\/(\\d+)/)||[])[1]).filter(Boolean))])"
}

clear_bookmarks() {
  ab_tab_x
  agent-browser open 'https://x.com/i/bookmarks'
  sleep 5
  url=$(ab_url)
  if echo "$url" | grep -qE 'login|onboarding'; then
    echo "NOT LOGGED IN: $url" >&2
    return 1
  fi
  ids=$(extract_ids)
  echo "bookmarks: $ids"
  # GraphQL unsave (UI clicks often stall/re-sync — see skills/x-harvest-clear/SKILL.md)
  for id in $(echo "$ids" | python3 -c "import sys,json; [print(x) for x in json.load(sys.stdin)]" 2>/dev/null); do
    folder="$ROOT/raw/items/x-$id"
    [[ -d "$folder" ]] || echo "WARN: x-$id not on disk" >&2
    if [[ -n "${X_AUTH_TOKEN:-}" && -n "${X_CT0:-}" ]]; then
      "$ROOT/scripts/x_delete_bookmark.sh" "$id" || true
    else
      agent-browser open "https://x.com/i/status/$id"
      sleep 3
      ab_tab_x
      agent-browser eval "(()=>{const b=document.querySelector('button[data-testid=removeBookmark]'); b&&b.click(); return b?'unsaved':'none';})()"
    fi
  done
}

clear_likes() {
  ab_tab_x
  # Navigate via profile → Likes (URL varies by handle)
  agent-browser open 'https://x.com/home'
  sleep 3
  agent-browser snapshot -i | rg -i 'likes|like' || true
  # Fallback: try common likes path after reading profile link
  handle=$(agent-browser eval "(()=>{const a=document.querySelector('a[data-testid=\"AppTabBar_Profile_Link\"]'); return a?a.getAttribute('href'):null;})()")
  if [[ -n "$handle" && "$handle" != null ]]; then
    agent-browser open "https://x.com${handle}/likes"
    sleep 5
    ids=$(extract_ids)
    echo "likes: $ids"
    for id in $(echo "$ids" | python3 -c "import sys,json; [print(x) for x in json.load(sys.stdin)]" 2>/dev/null); do
      folder="$ROOT/raw/items/x-$id"
      [[ -d "$folder" ]] || echo "WARN: x-$id not on disk" >&2
      agent-browser open "https://x.com/i/status/$id"
      sleep 3
      ab_tab_x
      unliked=$(agent-browser eval "(()=>{const b=document.querySelector('button[data-testid=unlike]'); if(b){b.click(); return 'unliked'} return 'none';})()")
      if [[ "$unliked" == *unliked* ]]; then
        echo "unliked x-$id"
      fi
    done
  fi
}

clear_bookmarks || exit 1
clear_likes || true

ab_tab_x
agent-browser open 'https://x.com/i/bookmarks'
sleep 4
bm_ids=$(extract_ids)
ab_tab_x
handle=$(agent-browser eval "(()=>{const a=document.querySelector('a[data-testid=\"AppTabBar_Profile_Link\"]'); return a?a.getAttribute('href'):null;})()" | tr -d '"')
if [[ -n "$handle" && "$handle" != null ]]; then
  agent-browser open "https://x.com${handle}/likes"
  sleep 4
fi
like_ids=$(extract_ids)
if [[ "$bm_ids" == "[]" && "$like_ids" == "[]" ]]; then
  echo "VERIFIED: bookmarks and likes list pages empty"
else
  echo "WARN: lists not empty — bookmarks=$bm_ids likes=$like_ids" >&2
  exit 1
fi
