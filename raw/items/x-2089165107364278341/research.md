## What it is

Pointer to Anthropic's cost_optimization.ipynb cookbook: a real agent task cut from ~$0.29 to ~90% less without accuracy loss, with model downgrade as the last lever.

## How it works

- Source: anthropics/claude-cookbooks `cost_optimization/cost_optimization.ipynb`.
- Claimed order of operations: prompt/cache/tool-shape first, cheaper model last.
- Framed around a production-like agent loop, not a toy completion.
- Useful checklist when BESS/SEO/design agents burn tokens on retries and verbose tool dumps.
- Pairs with cheap-inference vendor posts (RunInfra, Unsloth GGUF) as the 'spend less' lane.

## Why saved

KB runs long agent loops; this is the official playbook for cost without dumping Opus on day one.

## Topics

`agent-skills`

## Related

`web-anthropic-claude-self-service-data`, `x-2088594942482374759`, `web-cerebras-knowledge-base`, `x-2090103470015828184`

## Use when

An agent workflow is too expensive per task, or when designing caching, prompt compaction, and model routing before switching providers.
