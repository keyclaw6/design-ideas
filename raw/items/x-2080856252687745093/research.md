# Research

## What it is
Aman’s primer on autoresearch and harness engineering (`autoresearch.aman.ai`): agents that propose changes, run experiments, evaluate, and learn — including optimizing the system *around* the model (Meta-Harness).

## How it works
- Loop: propose → run → evaluate → repeat (AlphaEvolve / Evolution-through-LLMs lineage).
- Architecture: frozen infra vs editable code; proposer, evaluator, controller; filesystem experiment memory; validation gates and Pareto selection.
- Harness search: prompts, retrieval, memory/state, tool routing, DSPy-style pipelines — not just weights.
- Eval/safety: held-out sets, quality/cost/latency tradeoffs, sandboxing, leakage and reward-hacking controls, multi-agent parallelism.
- Pointers to Self-Refine, GEPA, TextGrad, ADAS, Meta-Harness.

## Why saved
Canonical vocabulary for every other “self-improving agent” bookmark in this library. Maps directly onto skill packs, SEO crawls, and design lints as eval targets.

## Topics
- `agent-skills`

## Related
- `x-2074912810803560497` — measured Codex kernel loop
- `x-2032671842230501729` — Hyperspace swarm + DAG
- `x-2086790895538700379` — copy-paste loops that “worked in the real world”
- `x-2087026930323247306` — Anthropic Dynamic Workflows (1k subagents)

## Use when
Designing an experiment harness, skill eval, or meta-optimizer. Start here before cloning any swarm repo.
