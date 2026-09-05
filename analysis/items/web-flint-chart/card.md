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
- `web-flint-chart#c3` (capability, demonstrated) flint-chart 0.5.1 assembleVegaLite and assembleECharts both accept the getting-started Line Chart spec; hosted flint-chart-mcp v0.5.1 lists six tools and render_chart backends are vegalite, echarts, and chartjs only. — evidence: "assembleVegaLite mark=line, 5 values; assembleECharts series type=line; tools/list: render_chart compile_chart validate_chart list_chart_types list_themes create_chart_view" [note]
- `web-flint-chart#c4` (result, demonstrated) assemblePlotly on the getting-started Line Chart returns one scatter trace. Hosted render_chart vegalite emitted a 17,393-byte SVG (428x416) and a 23,944-byte PNG. render_chart still has no Plotly backend. — evidence: "flint-chart@0.5.1 assemblePlotly {data:[{type:scatter}], layout.title}. MCP render_chart format=svg/png; PNG magic 89 50 4E 47. First call without data+chart_spec was -32602." [note]
- `web-flint-chart#c5` (availability, demonstrated) leftover30 unused flint.data-formulator.ai/mcp stays keyed — do not hammer. — evidence: "leftover30-2026-09-05.json skip keyed Flint MCP." [note]
**Numbers.** hosted MCP tools: 6  (note)
**Recipe.** —
**Techniques.** [chart-theme-presets](../../techniques/chart-theme-presets.md), [chart-theme-presets](../../techniques/chart-theme-presets.md)
**Tools.** [flint-chart-mcp](../../tools/flint-chart-mcp.md)
**Links.** repo (https://github.com/microsoft/flint-chart), product (https://flint.data-formulator.ai/mcp), https://www.npmjs.com/package/flint-chart, https://flint.data-formulator.ai/mcp
**Related items.** [github-antvis-infographic](../github-antvis-infographic/card.md), [github-cathrynlavery-diagram-design](../github-cathrynlavery-diagram-design/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
**Media.**
`raw/items/web-flint-chart/media/favicon.svg` (other, carries_technique=false) — Flint site favicon: geometric folded-paper mark in gray tones used on the project docs homepage.
**Judge hints.** must_read: False · compare with: [github-antvis-infographic](../github-antvis-infographic/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
