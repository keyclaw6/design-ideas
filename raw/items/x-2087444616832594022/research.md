# Research

## What it is
Tencent Hunyuan survey of self-evolving agents: how agents that rewrite themselves should be evaluated so an update cannot be its own only evidence.

## How it works
- Paper: Diving into Reliable Self-Evolving Agents (OpenReview `CGO1hDTHNe`).
- Companion catalog: https://github.com/wkqdzkd/Awesome-Reliable-Self-Evolving-Agents (549 works) and project site https://wkqdzkd.github.io/Awesome-Reliable-Self-Evolving-Agents/
- Defines an L0–L4 taxonomy for how far an agent may modify its own prompts, tools, or weights.
- Introduces a reliability ladder: what evidence is required before accepting an update (held-out evals, human review, independent judges).
- Core principle: no update should control the only evidence used to accept itself — relevant to loops that rewrite skills, AGENTS.md, or harness code in-repo.

## Why saved
KB already tracks Ouroboros-style self-improving agents and autoresearch loops. This is the evaluation map for whether those loops are actually getting better vs. overfitting to their own traces.

## Topics
`agent-skills`

## Related
- `x-2087151807965401320` — Ouroboros self-improving coding agent
- `x-2080856252687745093` — primer on autoresearch / harness engineering
- `web-davidgasquez-context-engineering` — treat agent memory as a data pipeline
- `github-punkpeye-awesome-mcp-servers` — tool surface that self-evolving agents would rewrite

## Use when
Designing or auditing an agent that edits its own skills, prompts, or tools; need a reliability checklist before letting a loop commit those edits.
