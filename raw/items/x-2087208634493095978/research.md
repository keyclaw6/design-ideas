# Research

## What it is
Tom Dörr sharing Memoria (https://github.com/matrixorigin/Memoria): version control for AI agent memory — snapshots, branches, and merges. Pitch: integrity, less hallucination, consistent long-term context.

## How it works
- Git metaphors on the memory store: snapshot a state, branch a hypothesis, merge or abandon.
- Aimed at long-running agents that would otherwise clobber a single blob of memory.
- Tweet is a one-liner + screenshot; repo is the spec.

## Why saved
Pairs with ReasoningBank (what to store) and Hermes life-OS (where the vault lives). Branching memory is useful for parallel research (SEO tests, camera path variants).

## Topics
- `agent-skills`

## Related
- `x-2087143369181114868` — ReasoningBank traces
- `x-2086920236079681607` — four-layer markdown OS
- `web-cerebras-knowledge-base` — enterprise KB
- `web-davidgasquez-context-engineering` — ETL framing

## Use when
Agent memory needs experiments in parallel without destroying the main vault. Evaluate Memoria vs a plain git-backed markdown KB.
