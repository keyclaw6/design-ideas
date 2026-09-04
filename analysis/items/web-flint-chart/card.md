# Microsoft Flint chart IL: compact specs compile to Vega, ECharts, Plotly

`web-flint-chart` · website · product · en · [source](https://microsoft.github.io/flint-chart/) · [raw](../../../raw/items/web-flint-chart/)
**Author:** Microsoft (@—) · **Published:** — · **Captured:** 2026-09-02T17:15:42Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [infographics-diagrams](../../subjects/infographics-diagrams/brief.md) · **Also:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Roles:** tool, technique · **Platforms:** mcp, cursor

**Summary.** Microsoft Flint is a visualization intermediate language where agents write compact chart specs that compile to Vega-Lite, ECharts, Chart.js, Plotly, or Excel with publication themes. Hosted flint-chart-mcp exposes the compiler to coding agents.
**Question it answers.** How can an agent emit one chart spec that compiles to multiple visualization backends with styled themes?

**Claims.**
- `web-flint-chart#c1` (capability, stated) Flint derives scales, axes, and spacing from a semantic spec plus data and optional theme. — evidence: "Flint derives scales, axes, spacing from semantic spec + data + optional theme." [linked-page]
- `web-flint-chart#c2` (availability, stated) A hosted MCP server at flint.data-formulator.ai/mcp exposes Flint to agent clients. — evidence: "Hosted MCP: `https://flint.data-formulator.ai/mcp`" [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** [chart-theme-presets](../../techniques/chart-theme-presets.md), [chart-theme-presets](../../techniques/chart-theme-presets.md)
**Tools.** [flint-chart-mcp](../../tools/flint-chart-mcp.md)
**Links.** repo (https://github.com/microsoft/flint-chart), product (https://flint.data-formulator.ai/mcp), https://www.npmjs.com/package/flint-chart
**Related items.** [github-antvis-infographic](../github-antvis-infographic/card.md), [github-cathrynlavery-diagram-design](../github-cathrynlavery-diagram-design/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
**Media.**
`raw/items/web-flint-chart/media/favicon.svg` (other, carries_technique=false) — Flint site favicon: geometric folded-paper mark in gray tones used on the project docs homepage.
**Judge hints.** must_read: False · compare with: [github-antvis-infographic](../github-antvis-infographic/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
