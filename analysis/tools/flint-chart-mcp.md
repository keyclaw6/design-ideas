# Flint Chart Mcp

**Slug:** `flint-chart-mcp` · **Kind:** product · **URL:** https://microsoft.github.io/flint-chart/ · **Canonical item:** [web-flint-chart](../items/web-flint-chart/card.md)
**Subjects:** [infographics-diagrams](../subjects/infographics-diagrams/brief.md), [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md)
**Referenced by (1):**
- [Microsoft Flint chart IL: compact specs compile to Vega, ECharts, Plotly](../items/web-flint-chart/card.md) — tool, technique — infographics-diagrams

<!-- NOTES:START -->
**2026-09-04 capture — compile + hosted MCP.** Clone `microsoft/flint-chart`. `packages/flint-js` **flint-chart 0.5.1** MIT. README assemblers: Vega-Lite, ECharts, Chart.js, Plotly, Excel. Paper badge **arXiv:2607.20775**. `shared/test-data/` has **705** case directories. Theme preset files under `packages/flint-js/src/core/theme/presets/`: cartoon, datawrapper, economist, icons, mckinsey, nature, nyt, pop, powerbi, powerbi-light, swiss (**11**). Docs say ThemeSpec currently applies to Vega-Lite output. Python package is source preview; “PyPI planned.”

**Local compile (npm `flint-chart@0.5.1`).** Getting-started monthly-signups spec (`Line Chart`, 5 rows, YearMonth/Quantity). `assembleVegaLite` → `mark: "line"`, encoding `x`/`y`, 5 data values. `assembleECharts` → `series: [{ type: "line" }]`. Same input, two backends. No PNG/SVG screenshot this pass (assemble returns JSON specs).

**Hosted MCP** `https://flint.data-formulator.ai/mcp`: GET → JSON-RPC **-32600** “method not allowed; use POST”. Unauthed `initialize` **200**, `serverInfo.name` `flint-chart-mcp` v0.5.1. Instructions: hosted server cannot read local files or remote URLs — inline `data.values` only. `tools/list` names **6** tools: `render_chart`, `compile_chart`, `validate_chart`, `list_chart_types`, `list_themes`, `create_chart_view`. `render_chart` backend enum is **vegalite | echarts | chartjs** (no Plotly/Excel on that tool). Do not collapse JS five-assembler list with the MCP render enum.
<!-- NOTES:END -->
