#!/usr/bin/env bash
# Harvest Reddit Saved posts for kab264set. Requires logged-in agent-browser session.
# Usage: BU_CDP_URL=http://127.0.0.1:PORT ./scripts/reddit_clear_saved.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export BU_CDP_URL="${BU_CDP_URL:?Set BU_CDP_URL}"

ab_url() {
  agent-browser eval "location.href" | tr -d '"'
}

ab_tab_reddit() {
  agent-browser tab reddit 2>/dev/null || agent-browser tab t10 2>/dev/null || true
}

ab_tab_reddit
agent-browser open 'https://www.reddit.com/user/kab264set/saved/'
sleep 5
url=$(ab_url)
body=$(agent-browser eval "document.body.innerText.slice(0,400)" | tr -d '"')
if echo "$body" | grep -qi 'nobody on Reddit goes by that name' || echo "$url" | grep -qiE '/login|register'; then
  echo "NOT LOGGED IN: $url" >&2
  echo "Login: reddit.com/login → email+password or one-time link → Kab264z@gmail.com" >&2
  exit 1
fi

extract_ids() {
  agent-browser eval "JSON.stringify([...new Set([...document.querySelectorAll('a[href*=\"/comments/\"]')].map(a=>{const m=a.href.match(/comments\\/([a-z0-9]+)/i);return m?m[1]:null;}).filter(Boolean))])"
}

ids=$(extract_ids)
echo "saved posts: $ids"
for id in $(echo "$ids" | python3 -c "import sys,json; [print(x) for x in json.load(sys.stdin)]" 2>/dev/null); do
  folder="$ROOT/raw/items/reddit-$id"
  if [[ ! -d "$folder" ]]; then
    echo "CAPTURE NEEDED: reddit-$id (HTTP/browser ingest lane)"
  fi
  agent-browser open "https://www.reddit.com/comments/$id/"
  sleep 3
  # Unsave: click saved/bookmark control if present
  agent-browser eval "(()=>{const b=[...document.querySelectorAll('button')].find(e=>/unsave|saved/i.test(e.getAttribute('aria-label')||e.innerText||'')); b&&b.click(); return b?'clicked':'none';})()"
  echo "processed reddit-$id"
done

ab_tab_reddit
agent-browser open 'https://www.reddit.com/user/kab264set/saved/'
sleep 4
remaining=$(extract_ids)
if [[ "$remaining" == "[]" ]]; then
  echo "VERIFIED: Reddit Saved list empty"
else
  echo "WARN: saved posts remain: $remaining" >&2
  exit 1
fi
