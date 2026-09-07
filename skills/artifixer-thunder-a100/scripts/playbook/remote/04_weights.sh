#!/usr/bin/env bash
set -euo pipefail
export HF_HOME=/home/ubuntu/workspace/hf-cache
CKPT=/home/ubuntu/workspace/ckpts/artifixer-14b.pt
mkdir -p /home/ubuntu/workspace/{logs,ckpts,hf-cache}
exec > >(tee -a /home/ubuntu/workspace/logs/04_weights.log) 2>&1
command -v huggingface-cli >/dev/null || pip install -q "huggingface_hub[cli]"

if [[ ! -f "$CKPT" ]] || [[ "$(stat -c%s "$CKPT")" -lt 50000000000 ]]; then
  huggingface-cli download nvidia/ArtiFixer artifixer-14b.pt --local-dir /home/ubuntu/workspace/ckpts
fi
huggingface-cli download Wan-AI/Wan2.1-T2V-14B-Diffusers
huggingface-cli download Qwen/Qwen3-VL-30B-A3B-Instruct
du -sh /home/ubuntu/workspace/hf-cache /home/ubuntu/workspace/ckpts
df -h /home/ubuntu/workspace || df -h
echo "04_weights done"
