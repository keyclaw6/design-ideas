# Graphed

**URL:** https://www.graphed.com/  
**MCP docs:** https://www.graphed.com/mcp  
**MCP endpoint:** https://mcp.graphed.com/mcp

Forward-deployed engineers embed with your team to build and manage **marketing agents**. Handles data pipelines, warehouse, and production hosting.

## Agent library (examples)

| Agent | Sample outcome |
|-------|----------------|
| Facebook Ads | Shifted $2.4k from cold prospecting to retargeting |
| Google Ads | Cut $1.8k/day from 23 keywords below 2x ROAS |
| SEO / AI Search | Found 42 long-tail pages with low competition |
| Cold Email | Generated 3 new sequences for CFO personas |
| LinkedIn Ads, Competitor Ads, Keyword Research, Blog Writing, Link Building, LinkedIn/Instagram DMs, TAM Mapping | … |

## Platform (Graphed Cloud)

1. **Connect channels** — Meta, Google, Shopify, GA4, HubSpot, **750+ sources** → warehouse
2. **Agent deployment** — FDEs wire stack; agents scoped to channels/goals
3. **Agent management** — 24/7 runs; actions logged to warehouse (`marketing.agent_actions`)

Components: managed data pipeline, modeled warehouse (Postgres), cloud runtime (agents, web servers, cron jobs), built-in agent tools (Seedance, Nano Banana, Apollo.io, MillionVerifier, DataForSEO, etc.).

## Graphed MCP

Query warehouse from Cursor, Claude Code, Windsurf:

```json
{
  "mcpServers": {
    "graphed": {
      "url": "https://mcp.graphed.com/mcp"
    }
  }
}
```

```bash
claude mcp add --transport http graphed https://mcp.graphed.com/mcp
```

**Capabilities:** explore schema, run read-only ClickHouse SQL, publish live data endpoints, build embedded dashboards.

## CTA

Book demo: https://www.graphed.com/register?returnTo=%2Fbook-demo
