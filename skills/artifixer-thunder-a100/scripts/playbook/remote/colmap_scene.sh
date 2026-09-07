#!/usr/bin/env bash
set -euo pipefail
SCENE="${1:?scene}"
MIN_PCT="${2:-30}"
ROOT=/home/ubuntu/workspace/data/$SCENE
IMG=$ROOT/images
DB=$ROOT/database.db
SPARSE=$ROOT/sparse
mkdir -p "$SPARSE" "$(dirname "$DB")" /home/ubuntu/workspace/logs
exec > >(tee -a /home/ubuntu/workspace/logs/colmap_${SCENE}.log) 2>&1

if [[ -f $ROOT/sparse/0/cameras.bin ]]; then
  echo "reuse existing sparse for $SCENE"
  n_img=$(find "$IMG" -iname '*.jpg' | wc -l)
  python3 /home/ubuntu/workspace/playbook/colmap_reg.py "$ROOT/sparse/0" "$n_img" "$MIN_PCT"
  exit $?
fi

gpu_flag=1
colmap feature_extractor --database_path "$DB" --image_path "$IMG" \
  --ImageReader.single_camera 1 --ImageReader.camera_model SIMPLE_RADIAL \
  --SiftExtraction.use_gpu "$gpu_flag" --SiftExtraction.max_num_features 8192 || \
colmap feature_extractor --database_path "$DB" --image_path "$IMG" \
  --ImageReader.single_camera 1 --ImageReader.camera_model SIMPLE_RADIAL \
  --SiftExtraction.use_gpu 0 --SiftExtraction.max_num_features 8192

colmap exhaustive_matcher --database_path "$DB" \
  --SiftMatching.use_gpu 1 --SiftMatching.guided_matching 1 || \
colmap exhaustive_matcher --database_path "$DB" \
  --SiftMatching.use_gpu 0 --SiftMatching.guided_matching 1

colmap mapper --database_path "$DB" --image_path "$IMG" --output_path "$SPARSE" \
  --Mapper.min_num_matches 10 --Mapper.init_min_tri_angle 4

# pick largest model
best=$(ls -d "$SPARSE"/* 2>/dev/null | head -1 || true)
[[ -n "$best" ]] || { echo "no sparse model"; exit 1; }
if [[ "$best" != "$SPARSE/0" ]]; then
  mkdir -p "$SPARSE/0"
  cp -a "$best"/* "$SPARSE/0/" || true
fi
colmap model_converter --input_path "$SPARSE/0" --output_path "$SPARSE/0" --output_type TXT || true
n_img=$(find "$IMG" -iname '*.jpg' | wc -l)
python3 /home/ubuntu/workspace/playbook/colmap_reg.py "$SPARSE/0" "$n_img" "$MIN_PCT"
echo "colmap $SCENE done"
