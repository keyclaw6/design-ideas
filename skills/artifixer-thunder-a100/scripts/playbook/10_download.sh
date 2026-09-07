#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"
mkdir -p "$OUT_DIR"
if [[ "$DRY_RUN" == "1" ]]; then
  echo "[DRY_RUN] tnr scp \$TNR_INDEX:exports -> $OUT_DIR"
  exit 0
fi
# shellcheck disable=SC1090
source "$INSTANCE_ENV"
: "${TNR_INDEX:=${INSTANCE_ID}}"
tnr scp "${TNR_INDEX}:/home/ubuntu/workspace/exports" "$OUT_DIR/" || true
tnr scp "${TNR_INDEX}:/home/ubuntu/workspace/logs" "$OUT_DIR/logs/" || true
if ! find "$OUT_DIR" \( -name 'ckpt*.pt' -o -name '*.ply' -o -name '*dumps.tgz' -o -name '*.depth.npy' \) | grep -q .; then
  echo "STOP: no ckpt/ply/dumps downloaded" >&2
  exit 1
fi
echo "downloaded $OUT_DIR"
