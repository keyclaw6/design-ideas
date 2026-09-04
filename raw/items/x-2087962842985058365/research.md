# Research

## What it is
Glenn Sonna pushing PrismML Bonsai-1.7B decode from 64 → 90 tok/s on the same Android phone, CPU only (no NPU/GPU), ~3× faster than the llama.cpp reference.

## How it works
- Small on-device LM; the news is the runtime, not a new architecture.
- CPU-only path matters for phones/SBCs where NPU drivers are locked.
- Baseline named: llama.cpp. If reproducing, compare against that, not against cloud APIs.
- Pair with Edge8 (huge sparse MoE on iPhone) and Qwen GGUF (desktop 27B) as three rungs of local inference.

## Why saved
Local agents on cheap hardware (site tablets, offline laptops) need a realistic tok/s number. 90 tok/s for 1.7B CPU-only is a calibration point.

## Topics
`agent-skills`

## Related
- `x-2087562269807030754` — Edge8-35B iPhone sparse MoE
- `x-2088281537427235320` — Qwen3.8-27B Unsloth GGUF
- `x-2087240056037908509` — cloud free-tier alternative (AMD Token Factory)

## Use when
Budgeting on-device agent UX (voice, sidecar, offline SEO checks) or benchmarking a custom Android/llama.cpp build against a published 90 tok/s CPU number.
