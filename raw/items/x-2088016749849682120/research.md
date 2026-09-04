# Research

## What it is
FleetingBits having Claude turn a codebase into an interactive visual diagram so they can discuss architecture with the model; moving dots are inspectable data snippets.

## How it works
- Screenshot (media/media_0.jpg) shows “Rivers of Empire — The Evolution Harness”: isometric schematic of an evolution loop (archive → parent selection → doctrine writers → games → rating → write-up → embed/file).
- Hover/inspect on the moving dots = data-plane debugging, not a static PNG.
- Workflow: ask Claude to emit a custom HTML/canvas diagram of modules and dataflow, then use that artifact as the shared language for the next refactor.
- Distinct from Mermaid-in-Markdown: this is a bespoke explorable, closer to a canvas worker (see related item in this batch).

## Why saved
Architecture talk with agents fails when both sides only have files. A generated, inspectable diagram is a pattern for this idea bank itself (graphify) and for BESS software/control-stack explainers.

## Topics
`infographics`, `agent-skills`, `design`

## Related
- `github-cathrynlavery-diagram-design` — editorial HTML+SVG types
- `x-2087329201451855933` — Pretty-Mermaid skill
- `x-2088590355440476343` — harness canvas worker drawing in chat
- `github-antvis-infographic` — AntV infographics
- `web-flint-chart` — viz language for agents

## Use when
Onboarding an agent (or a human) onto a messy repo and you need a shared living diagram of modules and dataflow, not a one-shot Mermaid paste.
