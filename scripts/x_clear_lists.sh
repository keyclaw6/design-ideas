#!/usr/bin/env bash
# Clear X Bookmarks + Likes after disk verify. Requires logged-in agent-browser session.
# Usage: BU_CDP_URL=http://127.0.0.1:PORT ./scripts/x_clear_lists.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export BU_CDP_URL="${BU_CDP_URL:?Set BU_CDP_URL to agent-browser Chrome CDP (not 9222 Grok Bot)}"

extract_ids() {
  agent-browser eval "JSON.stringify([...new Set([...document.querySelectorAll('a[href*=\"/status/\"]')].map(a=>(a.href.match(/status\\/(\\d+)/)||[])[1]).filter(Boolean))])"
}

clear_bookmarks() {
  agent-browser open 'https://x.com/i/bookmarks'
  sleep 5
  url=$(agent-browser get url)
  if echo "$url" | grep -qE 'login|onboarding'; then
    echo "NOT LOGGED IN: $url" >&2
    return 1
  fi
  ids=$(extract_ids)
  echo "bookmarks: $ids"
  # Unsave each visible bookmark via post detail
  for id in $(echo "$ids" | python3 -c "import sys,json; [print(x) for x in json.load(sys.stdin)]" 2>/dev/null); do
    folder="$ROOT/raw/items/x-$id"
    [[ -d "$folder" ]] || echo "WARN: x-$id not on disk" >&2
    agent-browser open "https://x.com/i/status/$id"
    sleep 3
    label=$(agent-browser eval "(()=>{const b=[...document.querySelectorAll('button,[role=button]')].find(e=>/bookmark/i.test(e.getAttribute('aria-label')||'')); return b?b.getAttribute('aria-label'):null;})()")
    if echo "$label" | grep -qi remove; then
      agent-browser eval "(()=>{const b=[...document.querySelectorAll('button,[role=button]')].find(e=>/remove.*bookmark/i.test(e.getAttribute('aria-label')||'')); b&&b.click(); return b?b.getAttribute('aria-label'):'none';})()"
      echo "unsaved x-$id"
    fi
  done
}

clear_likes() {
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
      liked=$(agent-browser eval "(()=>{const b=[...document.querySelectorAll('button,[data-testid=\"like\"]')].find(e=>/unlike/i.test(e.getAttribute('aria-label')||'')||e.getAttribute('aria-pressed')==='true'); return !!b;})()")
      if [[ "$liked" == "true" ]]; then
        agent-browser eval "(()=>{const b=[...document.querySelectorAll('button,[data-testid=\"like\"]')].find(e=>/unlike/i.test(e.getAttribute('aria-label')||'')||e.getAttribute('aria-pressed')==='true'); b&&b.click();})()"
        echo "unliked x-$id"
      fi
    done
  fi
}

clear_bookmarks || exit 1
clear_likes || true
echo "Done pass — reload bookmarks/likes to verify empty"
