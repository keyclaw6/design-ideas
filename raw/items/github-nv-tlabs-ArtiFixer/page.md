# ArtiFixer

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
