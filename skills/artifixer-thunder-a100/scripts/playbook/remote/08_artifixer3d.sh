#!/usr/bin/env bash
set -euo pipefail
SCENE="${1:?scene}"
export HF_HOME=/home/ubuntu/workspace/hf-cache
ROOT=/home/ubuntu/workspace
STEPS="${ARTIFIXER3D_STEPS:-30000}"
exec > >(tee -a $ROOT/logs/08_artifixer3d_${SCENE}.log) 2>&1
echo "phase=artifixer3d" > $ROOT/logs/phase.txt
PRED=$(cat $ROOT/logs/pred_dir_${SCENE}.txt)
cd $ROOT/ArtiFixer
python3 -m data_processing.run_artifixer3d \
  --scene_root $ROOT/artifixer-prep/$SCENE \
  --artifixer_frames_dir "$PRED" \
  --artifixer3d_steps "$STEPS" \
  --phases distill,render,prepare_artifixer3d_plus

if [[ -f $ROOT/artifixer-prep/$SCENE/split_artifixer3d_plus.json ]]; then
  python3 -m model_eval.run_inference \
    --evalset reconstructed_colmap \
    --checkpoint_pt $ROOT/ckpts/artifixer-14b.pt \
    --model_id Wan-AI/Wan2.1-T2V-14B-Diffusers \
    --save_dir $ROOT/artifixer-out/${SCENE}-3dplus \
    --split_path $ROOT/artifixer-prep/$SCENE/split_artifixer3d_plus.json \
    --save_frame_outputs_only \
    --num_inference_steps 4 \
    --num_views 6 || python3 -m model_eval.run_inference \
    --evalset reconstructed_colmap \
    --checkpoint_pt $ROOT/ckpts/artifixer-14b.pt \
    --model_id Wan-AI/Wan2.1-T2V-14B-Diffusers \
    --save_dir $ROOT/artifixer-out/${SCENE}-3dplus \
    --split_path $ROOT/artifixer-prep/$SCENE/split_artifixer3d_plus.json \
    --save_frame_outputs_only \
    --num_inference_steps 4 \
    --num_views 2 || echo "3D+ infer failed (ckpt/mesh dumps still valid)"
fi
find $ROOT/artifixer-prep/$SCENE/artifixer3d -name 'ckpt*.pt' | tee $ROOT/logs/ckpt_${SCENE}.txt
echo "08_artifixer3d $SCENE done"
