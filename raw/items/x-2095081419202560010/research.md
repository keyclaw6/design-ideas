## What they are actually doing

The post is a **Grok Bot plugin + hosted MCP funnel**, not a self-contained open-source outbound engine. “We open-sourced our entire outbound team” means markdown skills/agents/commands. Live prospecting, enrichment, LinkedIn sends, and Unibox replies require a **GojiberryAI account** and MCP auth. README: *“No MCP, no live pipeline.”*

**Repo** — `https://github.com/romangojiberryAI/gojiberryai-sales-os` (MIT, 69★ / 20 forks at capture)

- Install: `/plugin marketplace add romangojiberryAI/gojiberryai-sales-os` then `/plugin install sales-os@gojiberryai-sales-os` (Grok Bot or Claude Code). Cursor: copy `skills/sales-os/` and point MCP at `https://mcp.gojiberry.ai/mcp`.
- Default **propose, don’t send**. Autonomous mode needs an explicit instruction + score threshold.
- Slash commands: `/sales-os:outbound`, `find-leads`, `research`, `replies`, `pipeline`.
- Design: “No executable code. Pure markdown + a hosted MCP URL.” Honesty spine: don’t invent contacts.

**Product** — `https://gojiberry.ai/` (YC P26). Framer site: website → ICP → signal scoring → LinkedIn/email outreach. FAQ: AI GTM agent, not “just another LinkedIn tool.” Site copy “2,000+ sales & GTM teams”; X bio “5,000+ businesses.” Dollar prices not in static HTML (`#pricing` is JS). App: `https://app.gojiberry.ai/registration`.

**Comment “BOT”** is DM distribution. The repo is already public.

## Open questions

- Exact SaaS pricing (Framer `#pricing` not in HTTP text).
- Whether Grok Bot plugin install is live for all users or gated.
- Whether unique per-workspace MCP URLs differ from `mcp.gojiberry.ai/mcp`.
