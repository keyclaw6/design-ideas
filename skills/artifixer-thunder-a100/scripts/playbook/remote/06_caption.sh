#!/usr/bin/env bash
# Qwen3-VL-30B-A3B-Instruct is hardcoded as DEFAULT_CAPTIONING_MODEL_ID in ArtiFixer.
# --text_encoder_model_id is Wan UMT5 for the h5 embeddings, not a substitute for Qwen.
set -euo pipefail
SCENE="${1:?scene}"
export HF_HOME=/home/ubuntu/workspace/hf-cache
ROOT=/home/ubuntu/workspace
exec > >(tee -a $ROOT/logs/06_caption_${SCENE}.log) 2>&1
echo "phase=caption" > $ROOT/logs/phase.txt
cd $ROOT/ArtiFixer
python3 -m data_processing.prepare_colmap_artifixer_inputs \
  --colmap_dir $ROOT/data/$SCENE \
  --output_root $ROOT/artifixer-prep/$SCENE \
  --phases caption \
  --text_encoder_model_id Wan-AI/Wan2.1-T2V-14B-Diffusers || {
  echo "Qwen caption failed — stop (do not write text onto caption.h5)"
  exit 1
}
python3 - <<CHECK
import json
from pathlib import Path
root = Path("/home/ubuntu/workspace/artifixer-prep/$SCENE")
split = json.loads((root / "split.json").read_text())
sid = next(iter(split["test"]))
rel = split["test"][sid]["prompt_path"]
p = (root / rel).resolve()
assert p.is_file(), p
print("prompt_path ok", p)
CHECK
python3 -c 'import torch; torch.cuda.empty_cache()' || true
echo "06_caption $SCENE done"
