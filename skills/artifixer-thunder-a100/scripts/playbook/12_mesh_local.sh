#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"
mkdir -p "$OUT_DIR/meshes"
ok=0
for scene in c4-cabinet c5-lcu-closed c6-lcu-open c1-pcs c2-bcu c7-module-face; do
  d="$OUT_DIR/exports/$scene/tsdf"
  [[ -d "$d" ]] || d="$OUT_DIR/$scene/tsdf"
  if [[ ! -d "$d" ]]; then
    echo "skip mesh $scene (no tsdf dir)"
    continue
  fi
  python3 "$SCRIPT_DIR/local/tsdf_mesh.py" --depth-dir "$d" --out "$OUT_DIR/meshes/${scene}.ply" --voxel 0.005 \
    && ok=$((ok+1)) || echo "TSDF failed $scene"
done
echo "meshed $ok scenes -> $OUT_DIR/meshes"
