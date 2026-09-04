# Research

## What it is

NVIDIA SIL official ArtiFixer (SIGGRAPH 2026, Apache-2.0): auto-regressive diffusion models that enhance and extend 3D reconstructions built on 3DGRUT. Checkpoints on Hugging Face (`artifixer-14b.pt` ~16.9B and `1.3b`).

## How it works

- Base: 3DGRUT submodule (clone `--recurse-submodules`); training in `model_training/`, eval on DL3DV and Nerfbusters in `model_eval/`.
- `data_processing/` handles splits, captioning, sparse-reconstruction conversion.
- Checkpoints must match `--model_id` (Wan2.1 T2V 14B or 1.3B). CUDA Dockerfiles for 12/13 and aarch64.
- Project page and paper at research.nvidia.com/labs/sil/projects/artifixer/.
- Intended to repair sparse/noisy reconstructions and extend coverage — post-process after capture, not a replacement for camera path design.

## Why saved

BESS/site flythroughs from Gaussian splats fail on holes and incomplete scans. ArtiFixer is the research-grade repair step before mesh export (Splat2Mesh) or web viewing.

## Topics

`video-generation`, `camera-control`, `gaussian-splatting`, `bess-3d-flythrough`

## Related

`web-arcana-splat2mesh`, `github-oso95-scroll-world`, `github-scottstts-threejs-awesome-graphics-agent-skills`, `web-fal-ai`, `web-utsubo`

## Use when

A 3DGS capture of a plant/site is sparse or incomplete; planning a splat → repair → mesh/web pipeline; comparing diffusion repair vs recapture.
