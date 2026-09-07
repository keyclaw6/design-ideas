#!/usr/bin/env bash
set -euo pipefail
SCENE="${1:?scene}"
export HF_HOME=/home/ubuntu/workspace/hf-cache
ROOT=/home/ubuntu/workspace
exec > >(tee -a $ROOT/logs/05_prepare_${SCENE}.log) 2>&1
echo "phase=prepare" > $ROOT/logs/phase.txt

COLMAP=$ROOT/data/$SCENE
OUT=$ROOT/artifixer-prep/$SCENE
SEL=$COLMAP/selected.txt
[[ -f $SEL ]] || python3 /home/ubuntu/workspace/playbook/holdout_selected.py --images $COLMAP/images --out $SEL

cd $ROOT/ArtiFixer
python3 -m data_processing.prepare_colmap_artifixer_inputs \
  --colmap_dir "$COLMAP" \
  --output_root "$OUT" \
  --phases prepare,reconstruct,render,scale \
  --text_encoder_model_id Wan-AI/Wan2.1-T2V-14B-Diffusers \
  --selected_image_names_file "$SEL" \
  --reconstruction_steps 30000

test -f "$OUT/split.json"
echo "05_prepare $SCENE done"
