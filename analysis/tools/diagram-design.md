# Diagram Design

**Slug:** `diagram-design` · **Kind:** repo · **URL:** https://github.com/cathrynlavery/diagram-design/tree/main · **Canonical item:** [github-cathrynlavery-diagram-design](../items/github-cathrynlavery-diagram-design/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [infographics-diagrams](../subjects/infographics-diagrams/brief.md)
**Referenced by (1):**
- [Diagram Design: 39 editorial HTML+SVG diagram types for agents](../items/github-cathrynlavery-diagram-design/card.md) — tool, technique — infographics-diagrams

<!-- NOTES:START -->
**2026-09-04 capture — 39 types, HTML+SVG tokens.** Clone `cathrynlavery/diagram-design`. README “39 editorial diagram types” matches **exactly 39** `skills/diagram-design/references/type-*.md` files: architecture, bar, data-flow, db-schema, dependency, deployment, dp-integration, dp-security-matrix, er, fishbone, flowchart, gantt, high-level, it-state, journey, kanban, layers, line, loop, medallion, nested, org-chart, polar, process, pyramid, quadrant, radar, sankey, scatter, sequence, state, story-map, swimlane, timeline, tree, treemap, uml-class, venn, wardley.

Tree also has extra *example* stems without a `type-*.md` (beeswarm, bubble, bump, datalake, ridgeline, slopegraph, plus import-drawio / import-mermaid). **155** `example-*.html` files (light / dark / full variants). **87** `*.svg` files are vendor icons under `scripts/vendor/icons/`, not exported diagrams.

**Opened sample.** `skills/diagram-design/assets/example-architecture.html`: `:root` tokens `--color-paper #f5f5f5`, `--color-ink #2d3142`, `--color-muted #4f5d75`, `--color-accent #eb6c36`, plus `--font-sans/serif/mono`. Inline SVG (`viewBox="0 0 1000 480"`) also hardcodes the same hex on fills/markers. CSS variables are editable; many SVG paints are duplicated as hex. Five slash commands: doctor, export-diagram, import-drawio, import-mermaid, profile.

**2026-09-05 leftover27.** Unused `littlemight.com` **61,395 B** is *Business & life strategies for ambitious millennials* — host-string collision, not this library. Receipt `leftover27-2026-09-05.json`.
<!-- NOTES:END -->
