# ArtiFixer

> Source: https://github.com/nv-tlabs/ArtiFixer — by nv-tlabs, Riccardo de Lutio, Tobias Fischer, Yen-Yu Chang, Yuxuan Zhang, Jay Zhangjie Wu, Xuanchi Ren, Tianchang Shen, Katarina Tothova, Zan Gojcic, Haithem Turki — captured 2026-09-02T17:45:00Z — stats-at-capture: stargazer_count=635; license=Apache-2.0; primary_language=Python; description=Enhancing and extending 3D reconstruction with auto-regressive diffusion models (SIGGRAPH 2026)

## Article

**URL:** https://github.com/nv-tlabs/ArtiFixer

## What it is

NVIDIA SIL official implementation of **ArtiFixer** — auto-regressive diffusion models that enhance and extend 3D reconstructions (3DGRUT base). SIGGRAPH 2026. Apache-2.0, ~635 stars, Python.

## Links

- [Project page](https://research.nvidia.com/labs/sil/projects/artifixer/)
- [Paper](https://research.nvidia.com/labs/sil/projects/artifixer/assets/paper.pdf)
- [Hugging Face checkpoints](https://huggingface.co/nvidia/ArtiFixer) — `artifixer-14b.pt` (16.9B) and `artifixer-1.3b.pt` (1.68B)

## Layout

- `model_training/` — training loop, diffusion pipelines
- `model_eval/` — DL3DV and Nerfbusters inference + metrics
- `data_processing/` — splits, captioning, sparse-reconstruction conversion
- `thirdparty/` — 3DGRUT submodule (clone with `--recurse-submodules`)

## Setup

CUDA Dockerfiles (`Dockerfile.cuda12`, `cuda13`, `cuda13-aarch64`). Checkpoints require matching `--model_id` (Wan2.1 T2V 14B or 1.3B base).

## Capture note

README via raw GitHub (2026-09-02).

## Links

- https://x.com/0x0SojalSec/status/2094929928865341832
- https://arxiv.org/abs/2603.00492
- https://huggingface.co/nvidia/ArtiFixer
- https://research.nvidia.com/labs/sil/projects/artifixer/
