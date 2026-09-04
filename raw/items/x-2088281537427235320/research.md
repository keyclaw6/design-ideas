# Research

## What it is
Unsloth shipping Qwen3.8-27B local inference: Dynamic GGUFs at ~17GB RAM, plus NVFP4 quants; they call it the strongest model in its size class.

## How it works
- GGUF: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- Guide: https://unsloth.ai/docs/models/qwen3.8
- 17GB RAM target fits a 32–48GB workstation as a fully local coding/research agent.
- NVFP4 path is for NVIDIA boxes that want denser weights than GGUF Q-quants.
- Third rung of this batch’s local-model cluster (phone 1.7B / phone 35B MoE / desktop 27B).

## Why saved
Offline or private agent (plant data, unreleased DESIGN.md) needs a 27B-class local default. Unsloth’s RAM number is the install constraint.

## Topics
`agent-skills`

## Related
- `x-2087562269807030754` — Edge8-35B on-device MoE
- `x-2087962842985058365` — Bonsai 1.7B Android CPU
- `x-2087240056037908509` — cloud free DeepSeek/Qwen on AMD

## Use when
Standing up a local 27B agent (llama.cpp / Unsloth) or choosing GGUF vs NVFP4 for a 17GB+ machine.
