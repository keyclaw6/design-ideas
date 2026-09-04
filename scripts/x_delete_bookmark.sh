#!/usr/bin/env bash
# Unsave one X bookmark via GraphQL (preferred over UI clicks).
# Usage: X_AUTH_TOKEN=... X_CT0=... ./scripts/x_delete_bookmark.sh <tweet_id>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TWEET_ID="${1:?tweet id required}"
AUTH="${X_AUTH_TOKEN:?Set X_AUTH_TOKEN}"
CT0="${X_CT0:?Set X_CT0}"
QID="${X_DELETE_BOOKMARK_QID:-Wlmlj2-xzyS1GN3a6cj-mQ}"
BEARER="${X_BEARER_TOKEN:-AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA}"

RESP=$(curl -sS -w "\n%{http_code}" \
  -X POST "https://x.com/i/api/graphql/${QID}/DeleteBookmark" \
  -H "content-type: application/json" \
  -H "x-csrf-token: ${CT0}" \
  -H "x-twitter-active-user: yes" \
  -H "x-twitter-auth-type: OAuth2Session" \
  -H "authorization: Bearer ${BEARER}" \
  -H "cookie: auth_token=${AUTH}; ct0=${CT0}" \
  -d "{\"variables\":{\"tweet_id\":\"${TWEET_ID}\"},\"queryId\":\"${QID}\"}")

BODY=$(echo "$RESP" | head -n -1)
CODE=$(echo "$RESP" | tail -n 1)

if [[ "$CODE" != "200" ]]; then
  echo "DeleteBookmark failed ($CODE): $BODY" >&2
  exit 1
fi

FOLDER="$ROOT/raw/items/x-${TWEET_ID}"
if [[ -f "$FOLDER/source.json" ]]; then
  python3 - "$FOLDER/source.json" <<'PY'
import json, sys
from datetime import datetime, timezone
p = sys.argv[1]
d = json.load(open(p))
d["unsaved"] = True
d.setdefault("extra", {})["unsaved_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
json.dump(d, open(p, "w"), indent=2)
open(p, "a").write("\n")
PY
fi
echo "UNSAVED x-${TWEET_ID}"
