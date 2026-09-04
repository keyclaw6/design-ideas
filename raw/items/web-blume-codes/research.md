# Research

## What it is

Blume Sidecar (blume.codes): desktop app that watches Codex, Claude Code, and Cursor — the graph of rules, skills, hooks, and hidden config — and flags when setup drifts from intent.

## How it works

- Today: agent overview (finished/working/needs approval), hidden files/rules tracking, usage (plan limits, token burn) for Claude Code + Codex.
- Soon: auto-fixes for setup vs chat-instruction mismatch, analytics on whether setup is improving, local domain model as project-intent source of truth.
- Local-first conversation history; review evidence + diff before apply/dismiss/defer.
- Roadmap: team domain model, conflict resolution, auto-improve with tests against domain.
- Example drifts on homepage: Codex ticket handling, Claude catalog sync, Cursor billing-settings flow.

## Why saved

Skills/rules sprawl is the operational problem behind Taste/Impeccable/MengTo packs. Blume is the maintenance plane, not another skill.

## Topics

`agent-skills`, `mcp`

## Related

`web-chatgpt-training`, `github-pbakaus-impeccable`, `github-mengto-skills`, `web-opale-ui-taste`, `web-davidgasquez-context-engineering`

## Use when

Harness config is drifting across agents; auditing which skills actually fire; planning a domain model for a repo’s agent setup.
