#!/usr/bin/env bash
# Orchestrator — Thunder Compute, 14B quality, multi-scene.
# Default DRY_RUN=1. Live run requires tnr auth (agent mints token in browser).
set -euo pipefail
PLAYBOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$PLAYBOOK_DIR/00_env.sh"

WIPED=0
DOWNLOADED=0
HAS_SSH=0
REACHED_GPU=0

wipe_instance() {
  [[ "$WIPED" == "1" ]] && return 0
  WIPED=1
  if bash "$PLAYBOOK_DIR/11_wipe.sh"; then
    return 0
  fi
  echo "STOP: delete failed. Kill INSTANCE_ID=${INSTANCE_ID:-see $INSTANCE_ENV} in Thunder console" >&2
  return 1
}

on_exit() {
  local rc=$?
  trap - EXIT
  if [[ -f "$INSTANCE_ENV" ]]; then
    # shellcheck disable=SC1090
    source "$INSTANCE_ENV"
  fi
  if [[ "${DRY_RUN:-1}" == "0" ]]; then
    if [[ "${DOWNLOADED}" != "1" && "${HAS_SSH}" == "1" ]]; then
      if bash "$PLAYBOOK_DIR/10_download.sh"; then
        DOWNLOADED=1
      elif [[ "${REACHED_GPU}" == "1" ]]; then
        echo "STOP: download failed after GPU work — KEEP instance ${INSTANCE_ID:-?}" >&2
        KEEP_POD=1
      fi
    fi
    if [[ "${KEEP_POD:-0}" != "1" ]]; then
      wipe_instance || true
    fi
  fi
  exit "$rc"
}

for f in "$PLAYBOOK_DIR"/*.sh "$PLAYBOOK_DIR"/remote/*.sh; do
  bash -n "$f"
done
trap on_exit EXIT

bash "$PLAYBOOK_DIR/pack_scenes.sh"
bash "$PLAYBOOK_DIR/01_create.sh"
if [[ "$DRY_RUN" != "1" && -f "$INSTANCE_ENV" ]]; then
  # shellcheck disable=SC1090
  source "$INSTANCE_ENV"
  HAS_SSH=1
fi

if [[ "$DRY_RUN" == "1" ]]; then
  echo "[DRY_RUN] agent browser token / tnr login --token"
  echo "[DRY_RUN] tnr scp playbook+scenes / 03_install / 04_weights"
  echo "[DRY_RUN] C4 kill-gate (30k recon) then COLMAP others then 14B+3D+ loop"
  echo "[DRY_RUN] dump RGB-D / download / delete / local TSDF"
  exit 0
fi

require_auth
# shellcheck disable=SC1091
source "$PLAYBOOK_DIR/tnr_ssh.sh"

REACHED_GPU=1
wait_running
add_playbook_key
mkdir -p "$(dirname "$INSTANCE_ENV")"
cat >"$INSTANCE_ENV" <<EOF
INSTANCE_ID=${INSTANCE_ID}
INSTANCE_UUID=${INSTANCE_UUID:-}
TNR_INDEX=${TNR_INDEX:-$INSTANCE_ID}
GPU_USED=${GPU_USED:-a100}
SSH_HOST=${SSH_HOST}
SSH_PORT=${SSH_PORT:-22}
SSH_KEY=${INSTANCE_KEY}
SSH_USER=${SSH_USER}
PLAYBOOK_SSH_KEY=${SSH_KEY}
EOF
chmod 600 "$INSTANCE_ENV"
HAS_SSH=1

TNR_INDEX="${TNR_INDEX:-$INSTANCE_ID}"
ssh_remote 'mkdir -p /home/ubuntu/workspace/{playbook,data,logs,exports}'
tnr scp "$PLAYBOOK_DIR/remote/." "${TNR_INDEX}:/home/ubuntu/workspace/playbook/"
tnr scp "${ROOT}/upload/scenes.tar.gz" "${TNR_INDEX}:/home/ubuntu/scenes.tar.gz"
ssh_remote 'tar -C /home/ubuntu/workspace/data -xzf /home/ubuntu/scenes.tar.gz'
ssh_remote 'bash /home/ubuntu/workspace/playbook/03_install.sh'
ssh_remote 'bash /home/ubuntu/workspace/playbook/04_weights.sh'
ssh_remote 'bash /home/ubuntu/workspace/playbook/05_prepare.sh c4-cabinet'
ssh_remote 'python3 /home/ubuntu/workspace/playbook/c4_gate.py /home/ubuntu/workspace/artifixer-prep/c4-cabinet' \
  || { echo "STOP: C4 recon kill-gate — abort splat path"; exit 1; }
if [[ -f "$KILL_FILE" ]]; then
  echo "KILL set after C4 prepare"
  exit 1
fi
ssh_remote 'bash /home/ubuntu/workspace/playbook/06_caption.sh c4-cabinet'
ssh_remote 'bash /home/ubuntu/workspace/playbook/07_infer.sh c4-cabinet'
ssh_remote 'bash /home/ubuntu/workspace/playbook/08_artifixer3d.sh c4-cabinet'
ssh_remote 'bash /home/ubuntu/workspace/playbook/09_export.sh c4-cabinet'
for scene in c5-lcu-closed c6-lcu-open c1-pcs c2-bcu c7-module-face; do
  [[ -f "$KILL_FILE" ]] && break
  min=30
  [[ "$scene" == c7-module-face ]] && min=70
  ssh_remote "bash /home/ubuntu/workspace/playbook/colmap_scene.sh $scene $min" || continue
  ssh_remote "bash /home/ubuntu/workspace/playbook/05_prepare.sh $scene" || continue
  ssh_remote "python3 /home/ubuntu/workspace/playbook/c4_gate.py /home/ubuntu/workspace/artifixer-prep/$scene" || continue
  ssh_remote "bash /home/ubuntu/workspace/playbook/06_caption.sh $scene" || continue
  ssh_remote "bash /home/ubuntu/workspace/playbook/07_infer.sh $scene" || continue
  ssh_remote "bash /home/ubuntu/workspace/playbook/08_artifixer3d.sh $scene" || continue
  ssh_remote "bash /home/ubuntu/workspace/playbook/09_export.sh $scene" || continue
done
bash "$PLAYBOOK_DIR/10_download.sh"
DOWNLOADED=1
wipe_instance
bash "$PLAYBOOK_DIR/12_mesh_local.sh"
