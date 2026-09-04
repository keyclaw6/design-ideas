# Research

## What it is
@mfpiccolo had the harness build a canvas worker so the agent draws architecture diagrams in chat (and a console-injectable UI) instead of screenshot-pasting from an external diagramming app.

## How it works
- Problem: architecting in Lucid/FigJam/Excalidraw means constant screenshot ↔ chat.
- Solution: a worker inside the harness that renders a canvas; agent draws; human sees it in the transcript and can inject the UI in the console.
- Same destination as FleetingBits’ explorable codebase diagrams, but as a reusable harness worker rather than a one-off HTML file.
- Pattern: give the agent a drawing tool, not only a markdown/Mermaid tool.

## Why saved
This idea bank and BESS control-stack docs are diagram-heavy. A canvas worker is the missing tool next to Mermaid skills and editorial SVG kits.

## Topics
`infographics`, `agent-skills`, `design`

## Related
- `x-2088016749849682120` — Claude-generated explorable codebase diagram
- `github-cathrynlavery-diagram-design` — static editorial SVG types
- `x-2087329201451855933` — Pretty-Mermaid skill
- `web-flint-chart` — viz language for agents
- `github-antvis-infographic` — AntV infographics

## Use when
Adding a draw tool to a coding harness, or replacing screenshot-from-FigJam architecture reviews with in-chat canvases.
