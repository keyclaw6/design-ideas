# Research

## What it is
Chinese explainer of Google Research’s ReasoningBank: an agent memory that stores *reasoning traces* from both successes and failures, plus memory-aware test-time scaling. Repo: https://github.com/google-research/reasoning-bank

## How it works
- Most memories store facts or only wins; ReasoningBank stores how the agent got there, including failed trajectories.
- Memory-aware test-time scaling: memory makes search cheaper (don’t repeat pits); extra test-time compute writes new experiences back.
- Authors frame experience memory as a third scaling axis beside parameters and test-time compute.
- Reference impls: SWE-Bench + WebArena; GPT-family; LLM-as-judge on WebArena; community experiment, not a Google Cloud product.
- Run path sketched: clone, `cd reasoning-bank/SWE-Bench && ./run.sh` after Vertex config.

## Why saved
Directly usable when building agent memory for this idea bank / coding agents: log failures, not just green tests.

## Topics
- `agent-skills`

## Related
- `x-2087208634493095978` — Memoria (branch/merge memory)
- `x-2086920236079681607` — Hermes four-layer personal memory
- `web-cerebras-knowledge-base` — production KB
- `x-2087151807965401320` — Ouroboros (self-modifying agent that needs memory)

## Use when
Designing memory that should include failed SEO tests, bad camera paths, or rejected UI. Don’t only store winners.
