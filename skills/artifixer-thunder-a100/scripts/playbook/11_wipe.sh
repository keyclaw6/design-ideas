#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"
if [[ "$DRY_RUN" == "1" ]]; then
  echo "[DRY_RUN] tnr delete \$TNR_INDEX -y"
  exit 0
fi
load_env
# shellcheck disable=SC1090
[[ -f "$INSTANCE_ENV" ]] && source "$INSTANCE_ENV"
if [[ -z "${INSTANCE_ID:-}${TNR_INDEX:-}" ]]; then
  echo "wipe: no instance id"
  exit 0
fi
TOKEN="${TNR_API_TOKEN:-${THUNDER_API_TOKEN:-}}"
idx="${TNR_INDEX:-$INSTANCE_ID}"
if [[ "$idx" =~ ^[0-9]+$ ]] && command -v tnr >/dev/null 2>&1; then
  tnr delete "$idx" -y
else
  [[ -n "$TOKEN" ]] || { echo "STOP: no token to REST-delete"; exit 1; }
  curl -fsS -X POST "https://api.thundercompute.com:8443/v1/instances/${INSTANCE_UUID:-$INSTANCE_ID}/delete" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{}'
fi
echo "deleted index=$idx uuid=${INSTANCE_UUID:-}"
echo "Human: console must show zero instances (snapshots bill monthly — none should have been created)."
