# Research

## What it is
Cursor/Codex skill pack that renders Mermaid diagrams to SVG or ASCII art with no browser DOM, so agents can ship diagrams from a terminal session.

## How it works
- Repo: https://github.com/imxv/Pretty-mermaid-skills
- Skill takes a Mermaid source string and emits SVG (vector, restyleable) or ASCII (chat/log-friendly) without spinning up a headless browser.
- Zero-DOM claim means the renderer does not depend on a live page or Chromium; useful inside agent sandboxes that cannot open a window.
- Fits the same lane as editorial diagram skills: agent writes the graph, skill produces the artifact, human pastes into docs or a landing page.
- Complementary to HTML+SVG diagram kits that reject “Mermaid-slop” styling; this one keeps Mermaid as the authoring language and upgrades the output.

## Why saved
KB keeps diagram-as-content tools for architecture notes, BESS explainer graphics, and agent-authored docs. A Mermaid skill that does not need a browser is a practical default in Cursor/Codex loops.

## Topics
`infographics`, `agent-skills`, `design`

## Related
- `github-cathrynlavery-diagram-design` — 29 editorial HTML+SVG diagram types (anti-Mermaid-slop)
- `github-antvis-infographic` — AntV infographic generation
- `web-flint-chart` — viz language for agents
- `x-2088016749849682120` — Claude drawing live codebase diagrams
- `x-2088590355440476343` — harness canvas worker that draws diagrams in chat

## Use when
An agent needs to emit architecture or pipeline diagrams from Mermaid without a browser, or you are choosing between Mermaid-in-agent vs self-contained HTML/SVG diagram skills.
