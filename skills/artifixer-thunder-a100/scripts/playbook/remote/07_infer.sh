#!/usr/bin/env bash
set -euo pipefail
SCENE="${1:?scene}"
export HF_HOME=/home/ubuntu/workspace/hf-cache
ROOT=/home/ubuntu/workspace
exec > >(tee -a $ROOT/logs/07_infer_${SCENE}.log) 2>&1
echo "phase=infer" > $ROOT/logs/phase.txt
cd $ROOT/ArtiFixer
run_infer() {
  local nv="$1"
  python3 -m model_eval.run_inference \
    --evalset reconstructed_colmap \
    --checkpoint_pt $ROOT/ckpts/artifixer-14b.pt \
    --model_id Wan-AI/Wan2.1-T2V-14B-Diffusers \
    --save_dir $ROOT/artifixer-out/$SCENE \
    --split_path $ROOT/artifixer-prep/$SCENE/split.json \
    --render_trajectory all_frames \
    --save_frame_outputs_only \
    --num_inference_steps 4 \
    --num_views "$nv"
}
# A100 80GB: try 6 (quality), then 4, then 2. Do not drop to 1.3B unless 2 still OOMs.
run_infer 6 || {
  echo "14B OOM at num_views=6 — retry 4"
  run_infer 4 || {
    echo "14B OOM at num_views=4 — retry 2"
    run_infer 2
  }
}

PRED=$(find $ROOT/artifixer-out/$SCENE -type d -path '*/frames/batch_0000/pred' | head -1)
[[ -n "$PRED" ]] || { echo "STOP: no pred"; exit 1; }
echo "$PRED" > $ROOT/logs/pred_dir_${SCENE}.txt
echo "07_infer $SCENE pred=$PRED"
