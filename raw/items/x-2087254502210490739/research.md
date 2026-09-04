# Research

## What it is
Hype summary of a Stanford AI Systems Lab paper: why multi-agent pipelines fail, and a Control Plane Pattern for autonomous research. Claims 4 weeks → 30 min investigation latency and ~10× less tokens with no handoff decay.

## How it works
- Failure mode: specialized agents pass context down a chain; each hop loses signal (example: synthesis agent recommends field visits for a payer-tier issue).
- Replacement: deterministic signal queues, a single centralized reasoning agent, knowledge-graph control plane.
- Agentic analytics as a bounded, graph-constrained OS rather than a brittle pipeline.
- Paper/article URLs not in `post.md` (“read below”); treat as pattern, re-search “Control Plane Pattern autonomous research Stanford” if citing.

## Why saved
Counterweight to “just add 1,000 subagents.” Matches KB’s graphify/knowledge-graph instinct.

## Topics
- `agent-skills`

## Related
- `x-2087026930323247306` — official Claude fan-out (use with this caution)
- `x-2080856252687745093` — harness/controller vocabulary
- `x-2032671842230501729` — Research DAG (related graph idea)
- `web-cerebras-knowledge-base` — production knowledge layer

## Use when
Designing multi-agent research (SEO, harvest, BESS analysis). Prefer a control plane + KG over a long specialist chain.
