#!/usr/bin/env bash
# Create Thunder instance. Persist numeric identifier BEFORE SSH. Never RunPod.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"

ensure_ssh_key

install_tnr() {
  if command -v tnr >/dev/null 2>&1; then
    return 0
  fi
  echo "Installing Thunder CLI"
  curl -fsSL https://raw.githubusercontent.com/Thunder-Compute/thunder-cli/main/scripts/install.sh | bash
  export PATH="${HOME}/.tnr/bin:${HOME}/.local/bin:${PATH}"
  command -v tnr >/dev/null 2>&1 || { echo "STOP: tnr missing"; exit 1; }
}

write_instance_env() {
  mkdir -p "$(dirname "$INSTANCE_ENV")"
  cat >"$INSTANCE_ENV" <<EOF
INSTANCE_ID=${INSTANCE_ID:-}
INSTANCE_UUID=${INSTANCE_UUID:-}
TNR_INDEX=${TNR_INDEX:-0}
GPU_USED=${GPU_USED:-}
SSH_HOST=${SSH_HOST:-}
SSH_PORT=${SSH_PORT:-22}
SSH_KEY=${INSTANCE_KEY}
SSH_USER=${SSH_USER}
PLAYBOOK_SSH_KEY=${SSH_KEY}
EOF
  chmod 600 "$INSTANCE_ENV"
  echo "Wrote $INSTANCE_ENV id=$INSTANCE_ID index=$TNR_INDEX"
}

create_one() {
  local gpu="$1" vcpus="$2"
  GPU_USED="$gpu"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "[DRY_RUN] tnr create --gpu $gpu --num-gpus 1 --vcpus $vcpus --template $TNR_TEMPLATE --disk $DISK_GB"
    echo "[DRY_RUN] host RAM would be $((vcpus * 8)) GiB (need ≥70 for 14B)"
    return 2
  fi
  local out
  out="$(tnr create --json --gpu "$gpu" --num-gpus 1 --vcpus "$vcpus" --template "$TNR_TEMPLATE" --disk "$DISK_GB" 2>&1)" || {
    echo "$out"
    return 1
  }
  echo "$out"
  eval "$(printf '%s' "$out" | python3 "$SCRIPT_DIR/parse_tnr_create.py" "$INSTANCE_KEY")"
  if [[ -z "${INSTANCE_ID:-}" ]]; then
    echo "STOP: could not parse identifier from tnr create --json"
    echo "$out"
    exit 1
  fi
  write_instance_env
}

main() {
  echo "=== Thunder create (A100, not H100; RunPod forbidden) ==="
  echo "Primary: a100 ${VCPUS_PRIMARY}vCPU/$((VCPUS_PRIMARY*8))GB  Fallback: a100 ${VCPUS_FALLBACK}vCPU/$((VCPUS_FALLBACK*8))GB  disk=${DISK_GB}G"
  echo "Est. ~\$1.66/hr at 16 vCPU + 400G  (GPU \$1.09 + 12 extra vCPU \$0.48 + disk \$0.09)"
  if [[ "$DRY_RUN" == "1" ]]; then
    create_one a100 "$VCPUS_PRIMARY" || true
    create_one a100 "$VCPUS_FALLBACK" || true
    echo "DRY_RUN complete — no instance."
    exit 0
  fi
  require_auth
  install_tnr
  if ! create_one a100 "$VCPUS_PRIMARY"; then
    echo "A100 16 vCPU failed — trying A100 12 vCPU (96 GB RAM)"
    if ! create_one a100 "$VCPUS_FALLBACK"; then
      echo "STOP: A100 stock-out. Not falling through to H100 unless you say so."
      exit 1
    fi
  fi
}

main "$@"
