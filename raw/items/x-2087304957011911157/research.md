# Research

## What it is
dodo-reach’s `pi-clarify`: an npm extension for the Pi coding agent that rewrites your prompt before send so you spend fewer turns explaining intent. `pi install npm:pi-clarify`

## How it works
- Intercepts the user message, expands/clarifies it, then forwards to Pi.
- Goal: fewer clarification round-trips.
- Tweet says “here’s how it works” then the harvest truncates; no diagram in `post.md`/`comments.md`.
- Same ecosystem as pi-shepherdr and the ponytail/grill AGENTS.md stack.

## Why saved
Cheap quality-of-life for Pi. Complements grilling (ask the human) by also cleaning the prompt automatically.

## Topics
- `agent-skills`

## Related
- `x-2087232392209531166` — pi-shepherdr orchestration
- `x-2087263510090874911` — grill + /handoff workflow
- `github-leonxlnx-taste-skill` — quality/taste at output time
- `x-2085006701984698712` — human-review (quality at review time)

## Use when
Pi users send underspecified prompts. Install clarify; for the missing diagram, re-open the X post.
