# Research

## What it is
Follow-on to Autoquant: Hyperspace v3 makes the Karpathy autoresearch loop generic so a plain-English goal spins up a P2P swarm, plus a cross-domain Research DAG and declarative “Warps” that reconfigure a node.

## How it works
- Autoswarms: `hyperspace swarm new "<goal>"` → LLM writes sandboxed experiment code, dry-runs locally, publishes to P2P; peers mutate → evaluate in WASM; a playbook curator explains winning mutations to cold joiners.
- Research DAG: observations/experiments/syntheses from ML, search, finance, skills, infra share a knowledge graph; AutoThinker reads across domains and proposes unprogrammed hypotheses.
- Warps: stacked config presets (power-mode, privacy-mode, GPU sentinel, vault, custom NL-forged warps) that change what the agent does overnight.
- Claimed 237 agents / 14k+ experiments; GitHub auto-publish, TUI, 100+ CLI commands, OpenAI-compatible local API.

## Why saved
Reusable template for “describe a goal, swarm it, keep a DAG of what worked” — closer to KB’s agent stack than the finance-only prior post.

## Topics
- `agent-skills`

## Related
- `x-2032330665081839791` — finance-specific predecessor
- `x-2080856252687745093` — architecture primer (proposer/evaluator/controller)
- `x-2086790895538700379` — loop-library of copy-paste agent loops
- `x-2087151807965401320` — Ouroboros (self-modifying coding agent)

## Use when
Standing up a multi-agent research loop, a playbook of mutations, or comparing DAG memory vs session-only skills. Not for BESS/3D work.
