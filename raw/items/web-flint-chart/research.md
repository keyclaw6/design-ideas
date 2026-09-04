# Research

## What it is

Microsoft Flint (flint-chart): visualization intermediate language for the agent era. Compact semantic chart specs compile to Vega-Lite, ECharts, Chart.js, Plotly, or Excel. Hosted MCP at flint.data-formulator.ai/mcp.

## How it works

- Agent writes a small spec; Flint derives scales, axes, spacing from spec + data + optional theme (NYT, Economist, Swiss, McKinsey).
- `flint-chart-mcp` exposes the compiler to Cursor/Claude.
- v0.5.1 extends themes to Plotly. GitHub microsoft/flint-chart; arXiv paper linked from repo.
- Complements AntV (template infographics) and Lavery (editorial diagrams): Flint is *charts from data*, not narrative SVG scenes.

## Why saved

Agent-native chart contract for SEO/content and internal data essays (Macomber). MCP means coding agents can emit Flint instead of guessing ECharts JSON.

## Topics

`infographics`, `mcp`, `agent-skills`

## Related

`github-antvis-infographic`, `github-cathrynlavery-diagram-design`, `web-iandmacomber-post-ai-data-stack`, `github-punkpeye-awesome-mcp-servers`, `web-aidesigner-mcp`

## Use when

An agent must produce publication-styled charts from a table; targeting Vega/ECharts/Plotly from one spec; wiring chart MCP.
