# Research

## What it is
A write-up of Autoquant: a distributed swarm of ~135 agents that mutates multi-factor trading strategies against 10 years of market data using Karpathy's autoresearch loop.

## How it works
- Each agent runs a four-layer pipeline: Macro (regime), Sector (momentum rotation), Alpha (8-factor scoring), plus an adversarial Risk Officer that can veto low-conviction trades.
- Layer weights evolve by Darwinian selection: ~30 mutations compete per round; winning strategies gossip across the swarm.
- Agents independently dropped dividend/growth/trend factors and switched to risk-parity sizing (claimed Sharpe 1.04 → 1.32).
- Later gates: 70/30 out-of-sample split, crisis stress tests (GFC, COVID, 2022 hikes), composite scoring for drawdown not just Sharpe, RSS sentiment into factors.
- Same evolutionary loop is claimed to compound across ML, search ranking, skill invention, and finance in one AGI repo.

## Why saved
KB is collecting agent self-improvement loops, not a quant desk. This is a concrete mutate → backtest → propagate recipe that later generalizes in the Hyperspace post.

## Topics
- `agent-skills`

## Related
- `x-2032671842230501729` — same author, generic Autoswarms / Research DAG
- `x-2080856252687745093` — Aman Chadha primer on autoresearch + meta-harness
- `x-2074912810803560497` — Codex auto-kerneling write-up (same loop, GPU kernels)
- `x-2087151807965401320` — Ouroboros self-improving coding agent

## Use when
Designing an unsupervised experiment loop (propose, evaluate, share) or comparing swarm vs single-agent research for SEO/design evals. Ignore the finance claims; steal the pipeline shape.
