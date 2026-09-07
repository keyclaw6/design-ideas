#!/usr/bin/env bash
# Shared env. Thunder A100 only. Default DRY_RUN=1 until the agent has a token.
# Scripts live in the git skill; runtime artifacts (keys, token, tarball, instance id) stay in ROOT.
set -euo pipefail
export PATH="${HOME}/.tnr/bin:${HOME}/.local/bin:/usr/local/bin:${PATH}"

PLAYBOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${ARTIFIXER_WORKROOT:-${HOME}/.cache/splat-mesh-maxqual}"
ENV_FILE="${ROOT}/.env"
KILL_FILE="${ROOT}/KILL"
INSTANCE_ENV="${ROOT}/instance.env"
SSH_KEY="${ROOT}/ssh/id_ed25519"
SSH_PUB="${SSH_KEY}.pub"
INSTANCE_KEY="${ROOT}/ssh/instance.pem"
KNOWN_HOSTS="${ROOT}/ssh/known_hosts"
mkdir -p "$ROOT/ssh" "$ROOT/upload" "$ROOT/logs"

GPU_PRIMARY="a100"
GPU_FALLBACK="a100"
TNR_TEMPLATE="base"
DISK_GB=400
# A100 80GB. 16 vCPU → 128 GB host RAM (Wan-14B construct needs ≥70).
# Never default 8 vCPU (64 GB). Fallback 12 vCPU = 96 GB if 16 is stock-out.
# Do not rent H100 unless A100 is completely unavailable (see 01_create.sh).
VCPUS_PRIMARY=16
VCPUS_FALLBACK=12
VCPUS_H100=16
VCPUS_A100=16

ARTIFIXER_REF="${ARTIFIXER_REF:-a392c4dfe17459ef9952407accdb9fcdcdddba98}"
CHECKPOINT_NAME="artifixer-14b.pt"
MODEL_ID="Wan-AI/Wan2.1-T2V-14B-Diffusers"
TEXT_ENCODER_ID="$MODEL_ID"
RECON_STEPS=30000
ARTIFIXER3D_STEPS=30000
SSH_USER="${SSH_USER:-ubuntu}"
REMOTE_WORK="/home/ubuntu/workspace"
OUT_DIR="${HOME}/Downloads/splat-mesh-maxqual"

export DRY_RUN="${DRY_RUN:-1}"
SCENES=(c4-cabinet c5-lcu-closed c6-lcu-open c1-pcs c2-bcu c7-module-face)

ensure_ssh_key() {
  if [[ -f "$SSH_KEY" ]]; then
    return 0
  fi
  mkdir -p "$(dirname "$SSH_KEY")"
  ssh-keygen -t ed25519 -f "$SSH_KEY" -N "" -C "splat-mesh-maxqual"
}

load_env() {
  if [[ -f "$ENV_FILE" ]]; then
    set -a && source "$ENV_FILE" && set +a
  fi
}

require_auth() {
  load_env
  if [[ -n "${TNR_API_TOKEN:-${THUNDER_API_TOKEN:-}}" ]]; then
    export TNR_API_TOKEN="${TNR_API_TOKEN:-$THUNDER_API_TOKEN}"
    return 0
  fi
  if tnr status --no-wait --json >/dev/null 2>&1; then
    return 0
  fi
  echo "STOP: not logged into Thunder. Mint a token in the browser (skill references/browser.md)." >&2
  exit 1
}
