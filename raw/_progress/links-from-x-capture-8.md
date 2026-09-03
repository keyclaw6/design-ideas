# Links from X Capture 8 — Ingest Manifest

Captured: 2026-09-02T20:38:00Z  
Source tweets: [derrickcchoi training](https://x.com/derrickcchoi/status/2095133695480873023), [robinstetic AIDesigner MCP](https://x.com/robinstetic/status/2094467179320119498), [medriscoll AI-native #3](https://x.com/medriscoll/status/2094558408259272998), [0xJokker Obscura](https://x.com/0xJokker/status/2094427822064279870)  
Fetch: HTTP + gh API + r.jina.ai + curl (llms.txt, npm registry)

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | web-chatgpt-training | https://learn.chatgpt.com/training | complete | 6 walkthroughs + 2 hands-on labs; llms.txt in related_urls |
| 2 | web-aidesigner-mcp | https://www.aidesigner.ai/ai-ui-design-mcp | complete | Landing + /docs/mcp + website-cloner; 21 tools; @aidesigner/agent-skills 0.1.4 |
| 3 | github-h4ckf0r0day-obscura | https://github.com/h4ckf0r0day/obscura | complete | 23,989★ Apache-2.0 Rust; README high-level only (no evasion procedures) |
| 4 | web-obscura-sh | https://obscura.sh | complete | Marketing + docs.obscura.sh intro; docs.obscura.sh/llms.txt in related_urls |
| 5 | web-iandmacomber-post-ai-data-stack | https://www.iandmacomber.com/blog/post-ai-data-stack | complete | Post-AI data stack essay (2026-08-30); Ramp |
| 6 | web-cerebras-knowledge-base | https://www.cerebras.ai/blog/how-we-built-our-knowledge-base | complete | 15k Q/day KB; hybrid Slack + CocoIndex code; jina origin 500 but body OK |
| 7 | web-anthropic-claude-self-service-data | https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude | complete | ~95% automated queries; foundations + semantic layer + skills |
| 8 | web-davidgasquez-context-engineering | https://davidgasquez.com/context-engineering-is-a-data-problem | complete | Context = ETL/ELT; Knowledge Build System |
| 9 | web-cloudflare-kitesurf | https://blog.cloudflare.com/kitesurf/ | partial | Origin + architecture captured; PageRenderer section truncated |

## Skipped (per brief)

| URL | Reason |
|-----|--------|
| https://cal.com/obscura/quick-chat | cal.com booking — skip |
| Splat2Mesh zip / `web-arcana-splat2mesh` | Already in library — not edited |

## Already in library (linked only, not edited)

- `x-2095133695480873023` (ChatGPT training)
- `x-2094467179320119498` (AIDesigner MCP)
- `x-2094558408259272998` (AI-native #3 infographic)
- `x-2094427822064279870` (Obscura)
- `x-2094648474377839018` (Splat2Mesh — no new folder)
- `web-arcana-splat2mesh`

## Summary

- **9/9** required item folders created
- **8/9** complete captures; **1/9** partial (Cloudflare Kitesurf long post truncated)
- **9/9** source.json + page.md + research.md
- **0** comments.md
- **0** media saved
- Catalog not touched; X bookmarks not unsaved

## related_urls graph (high level)

```
x-capture-8 posts
  ├─► web-chatgpt-training (+ llms.txt, 6 walkthroughs, hands-on work/codex)
  ├─► web-aidesigner-mcp ◄──► /docs/mcp, /website-cloner, npm @aidesigner/agent-skills
  ├─► github-h4ckf0r0day-obscura ◄──► web-obscura-sh (+ docs.obscura.sh)
  │         └─► web-cloudflare-kitesurf (Obscura → Workers port)
  └─► medriscoll data/context cluster
        ├─► web-iandmacomber-post-ai-data-stack
        ├─► web-cerebras-knowledge-base
        ├─► web-anthropic-claude-self-service-data
        └─► web-davidgasquez-context-engineering
```
