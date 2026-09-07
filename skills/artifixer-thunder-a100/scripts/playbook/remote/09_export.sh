#!/usr/bin/env bash
set -euo pipefail
SCENE="${1:?scene}"
ROOT=/home/ubuntu/workspace
OUT=$ROOT/exports/$SCENE
mkdir -p "$OUT/tsdf"
exec > >(tee -a $ROOT/logs/09_export_${SCENE}.log) 2>&1
find $ROOT/artifixer-prep/$SCENE -name '*.ply' -o -name 'ckpt*.pt' | head -50 > $OUT/paths.txt
cp -a $ROOT/logs/ckpt_${SCENE}.txt "$OUT/" 2>/dev/null || true
CKPT=$(head -1 $ROOT/logs/ckpt_${SCENE}.txt || true)
if [[ -z "$CKPT" || ! -f "$CKPT" ]]; then
  CKPT=$(find $ROOT/artifixer-prep/$SCENE -name 'ckpt_30000.pt' | head -1 || true)
fi
SCALE=$ROOT/artifixer-prep/$SCENE/metric_alignment/scale_info.txt
if [[ -n "$CKPT" && -f "$CKPT" ]]; then
  python3 /home/ubuntu/workspace/playbook/dump_rgbd.py \
    --checkpoint "$CKPT" \
    --out "$OUT/tsdf" \
    ${SCALE:+--scale-file "$SCALE"} || echo "WARN: RGB-D dump failed for $SCENE"
fi
if [[ -d $ROOT/artifixer-prep/$SCENE ]]; then
  tar -C $ROOT/artifixer-prep/$SCENE -czf $OUT/artifixer3d_dumps.tgz \
    --exclude='*.pt' --exclude='hf*' artifixer3d recon_results split.json 2>/dev/null || \
    tar -C $ROOT/artifixer-prep/$SCENE -czf $OUT/prep_meta.tgz split.json 2>/dev/null || true
fi
# copy a small ply if present
find $ROOT/artifixer-prep/$SCENE -name '*.ply' -size -2G | head -3 | while read -r p; do
  cp -n "$p" "$OUT/" || true
done
ls -lh "$OUT" "$OUT/tsdf" || true
echo "09_export $SCENE done"
