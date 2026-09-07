#!/usr/bin/env bash
# Wait RUNNING, then SSH with Thunder-returned PEM (fallback: playbook key).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"

wait_running() {
  local i line st ip port
  local match_id="${TNR_INDEX:-$INSTANCE_ID}"
  for i in $(seq 1 90); do
    line="$(tnr status --no-wait --json 2>/dev/null | python3 "$SCRIPT_DIR/parse_tnr_status.py" "$match_id" || true)"
    if [[ -z "$line" && -n "${INSTANCE_UUID:-}" ]]; then
      line="$(tnr status --no-wait --json 2>/dev/null | python3 "$SCRIPT_DIR/parse_tnr_status.py" "$INSTANCE_UUID" || true)"
    fi
    if [[ -n "$line" ]]; then
      st="${line%%$'\t'*}"
      ip="$(echo "$line" | cut -f2)"
      port="$(echo "$line" | cut -f3)"
      if [[ "$st" == "RUNNING" && -n "$ip" ]]; then
        SSH_HOST="$ip"
        SSH_PORT="${port:-22}"
        export SSH_HOST SSH_PORT
        echo "RUNNING $SSH_HOST:$SSH_PORT"
        return 0
      fi
    fi
    sleep 5
  done
  echo "STOP: instance $match_id not RUNNING with public IP" >&2
  return 1
}

add_playbook_key() {
  local token="${TNR_API_TOKEN:-}"
  [[ -n "$token" && -f "$SSH_PUB" ]] || return 0
  local id="${INSTANCE_UUID:-$INSTANCE_ID}"
  curl -fsS -X POST "https://api.thundercompute.com:8443/v1/instances/${id}/add_key" \
    -H "Authorization: Bearer $token" \
    -H "Content-Type: application/json" \
    -d "$(python3 -c "import json; print(json.dumps({'public_key': open('$SSH_PUB').read()}))")" \
    >/dev/null 2>&1 || echo "WARN: add_key failed (ok if create-response PEM works)"
}

_ssh() {
  local user="$1"; shift
  local key="$1"; shift
  ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new \
    -o UserKnownHostsFile="$KNOWN_HOSTS" \
    -i "$key" -p "${SSH_PORT:-22}" \
    "${user}@${SSH_HOST}" "$@"
}

ssh_remote() {
  local keys=()
  [[ -f "${INSTANCE_KEY}" ]] && keys+=("$INSTANCE_KEY")
  [[ -f "${SSH_KEY}" ]] && keys+=("$SSH_KEY")
  local users=("$SSH_USER" ubuntu root)
  local k u
  # First try last working combo if set
  if [[ -n "${SSH_WORKING_KEY:-}" && -n "${SSH_WORKING_USER:-}" ]]; then
    _ssh "$SSH_WORKING_USER" "$SSH_WORKING_KEY" "$@" && return 0
  fi
  for u in "${users[@]}"; do
    for k in "${keys[@]}"; do
      if _ssh "$u" "$k" "true" >/dev/null 2>&1; then
        SSH_WORKING_USER="$u"
        SSH_WORKING_KEY="$k"
        export SSH_WORKING_USER SSH_WORKING_KEY
        SSH_USER="$u"
        _ssh "$u" "$k" "$@"
        return 0
      fi
    done
  done
  echo "STOP: SSH failed as ubuntu/root with instance PEM and playbook key" >&2
  return 1
}
