#!/usr/bin/env bash
set -euo pipefail
export HF_HOME=/home/ubuntu/workspace/hf-cache
ARTIFIXER_REF="${ARTIFIXER_REF:-a392c4dfe17459ef9952407accdb9fcdcdddba98}"
LOG=/home/ubuntu/workspace/logs/03_install.log
mkdir -p /home/ubuntu/workspace/{logs,hf-cache,ckpts,data}
exec > >(tee -a "$LOG") 2>&1

export DEBIAN_FRONTEND=noninteractive
sudo apt-get update -qq
sudo apt-get install -y -qq --no-install-recommends wget git curl build-essential gcc-11 g++-11 libgl1-mesa-dev libglib2.0-0 colmap || \
  sudo apt-get install -y -qq --no-install-recommends wget git curl build-essential libgl1 libglib2.0-0

gpu="$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1 || true)"
echo "GPU=$gpu"
IS_HOPPER=0
[[ "$gpu" == *H100* || "$gpu" == *H200* || "$gpu" == *GB200* ]] && IS_HOPPER=1
free -h || true

if [[ ! -d /home/ubuntu/workspace/ArtiFixer/.git ]]; then
  git clone --recurse-submodules https://github.com/nv-tlabs/ArtiFixer.git /home/ubuntu/workspace/ArtiFixer
fi
cd /home/ubuntu/workspace/ArtiFixer
git checkout "$ARTIFIXER_REF"
git submodule update --init --recursive

python3 -m pip install -q "torch==2.11.0" torchvision --index-url https://download.pytorch.org/whl/cu128 || \
  python3 -m pip install -q torch torchvision

if [[ "$IS_HOPPER" -eq 0 ]]; then
  python3 -m pip uninstall -y flash-attn 2>/dev/null || true
  echo "A100/Ampere: no FA3"
else
  echo "Hopper: FA3 allowed; FLASH_ATTN_MAX_JOBS=4"
  export FLASH_ATTN_MAX_JOBS=4
fi

cd thirdparty/3DGRUT-ArtiFixer
[[ -x /usr/local/bin/slangc ]] || bash scripts/install_slangc.sh /usr/local
python3 -m pip install -q -r requirements.txt
python3 -m pip install -q -e .
python3 -m pip uninstall -y opencv-python 2>/dev/null || true
python3 -m pip install -q opencv-python-headless h5py accelerate diffusers transformers ftfy einops scipy wandb tqdm Pillow matplotlib pyyaml torchmetrics imageio-ffmpeg av plyfile 'git+https://github.com/microsoft/MoGe.git'

cd /home/ubuntu/workspace/ArtiFixer
python3 - <<'SMOKE'
import torch, threedgrut
from moge.model.v2 import MoGeModel
print("smoke", torch.__version__, torch.cuda.get_device_name(0), threedgrut.__file__)
SMOKE
date -u +%Y-%m-%dT%H:%M:%SZ > /home/ubuntu/workspace/ArtiFixer/.bess_install_complete
echo "03_install done"
