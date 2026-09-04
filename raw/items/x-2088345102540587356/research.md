# Research

## What it is
LangChain “managed deep agent” architecture: your agent is a folder. Infographic + short URL https://langch.in/mda (MANAGED_DEEP_AGENT.md).

## How it works
- `agent/` with `agent.py`/`agent.ts`; surrounding dirs map to features: `instructions.md`, `skills/`, `memory.py`, `tools/`, `connectors/` (MCP), `middleware/`, `sandbox/`, `identity`, `channels/`, `schedules/`, `evals/`.
- CLI: `mda init` → add only the folders you need → `mda dev` → `mda deploy` (LangSmith-hosted runtime, persistence).
- Same composition model as Cursor skills + MCP + evals, packaged as a deployable unit.
- Screenshot title: “Your agent is a folder.”

## Why saved
Clean taxonomy for how KB already thinks about agents (skills, MCP, memory, evals). Use as the checklist when turning a local Cursor project into a hosted operator.

## Topics
`agent-skills`, `mcp`

## Related
- `github-punkpeye-awesome-mcp-servers` — what goes in `connectors/`
- `web-davidgasquez-context-engineering` — what goes in memory/instructions
- `x-2087026930323247306` — Anthropic dynamic workflows cookbook
- `github-emilkowalski-skills` — what goes in `skills/`
- `web-blume-codes` — control plane for local coding agents (contrast to hosted MDA)

## Use when
Structuring a new agent repo, mapping Cursor skills/MCP onto a LangChain managed runtime, or explaining agent composition as a folder tree.
