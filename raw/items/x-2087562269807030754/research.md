# Research

## What it is
Edge8-35B: a 35B ultra-sparse MoE with a jointly trained dynamic expert planner, plus an SSD-streaming inference engine, demoed on one iPhone with no cloud.

## How it works
- Claimed demo: 44 tok/s, ~1.06 GB peak memory on-device.
- Sparse MoE + expert planner decides which experts to page; SSD-streaming runtime keeps inactive experts off RAM.
- Model, runtime, and paper promised as open source (not linked in the post yet).
- Useful as a ceiling check for local agent runtimes (sidecars, voice loops, offline DESIGN.md lint) if the stack actually ships.
- Adjacent to other on-device posts in this batch (Bonsai Android CPU decode, Qwen GGUF).

## Why saved
Local/offline agents matter for a plant/BESS marketing stack that cannot always send site data to a cloud LLM. This is a pointer to a 35B-class on-phone path, not a ready install.

## Topics
`agent-skills`

## Related
- `x-2087962842985058365` — Bonsai-1.7B 90 tok/s on Android CPU
- `x-2088281537427235320` — Qwen3.8-27B Unsloth GGUF at 17GB RAM
- `x-2087240056037908509` — DeepSeek V4 Flash / Qwen free on AMD Token Factory
- `web-blume-codes` — local sidecar for coding agents

## Use when
Evaluating on-device or air-gapped agent runtimes, or comparing sparse-MoE streaming inference claims against GGUF/llama.cpp baselines.
