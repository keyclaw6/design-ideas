## What it is

RunInfra launch post for full-BF16 DeepSeek V4 Flash inference at 278 tok/s and sub-dollar-per-million-token pricing.

## How it works

- Vendor claims fastest full-precision V4 Flash serving, not a quantized cut-down.
- Published rates: $0.13/1M input, $0.27/1M output, ~278 tokens/s.
- Sold as an inference API rather than a chat app; relevant as a drop-in model endpoint for coding/design agents.
- Tweet links a RunInfra model page (slug currently names a Qwen 3.8 MoE endpoint — verify the live catalog before wiring).
- Pairs with other cheap-gateway posts in this batch (Vercel AI Gateway / Wafer).

## Why saved

KB likely saved it as a cost/latency option for agent loops (DESIGN.md generation, Three.js iteration, SEO crawls) where DeepSeek-class models are good enough and volume is high.

## Topics

`agent-skills`

## Related

`x-2088695568474546387`, `x-2090103470015828184`, `x-2089165107364278341`, `github-superdesigndev-treg`

## Use when

An agent needs a cheap, fast chat/completions backend for high-volume skill runs, or when comparing inference vendors for the local agent stack.
