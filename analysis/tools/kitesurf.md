# Kitesurf

**Slug:** `kitesurf` · **Kind:** library · **URL:** https://blog.cloudflare.com/kitesurf/ · **Canonical item:** [web-cloudflare-kitesurf](../items/web-cloudflare-kitesurf/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md), [serp-ai-visibility](../subjects/serp-ai-visibility/brief.md)
**Referenced by (1):**
- [Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)](../items/web-cloudflare-kitesurf/card.md) — tool, claim-source — mcp-and-agent-browsers

<!-- NOTES:START -->

Fetched 2026-09-04 https://blog.cloudflare.com/kitesurf/ + https://developers.cloudflare.com/browser-run/limits/

Port of **Obscura** (Rust, no Chrome) onto Workers / V8 isolates. Free **Browser Run beta** with per-account limits. CDP works with Puppeteer, Playwright, chrome-remote-interface, MCP. Blog “not yet”: play video, WebGL, bot-challenge TLS fingerprints, ~10-minute authenticated persistent sessions.

Workers Free Browser Run (docs 2026-08-20): **10 minutes/day**, 3 concurrent sessions, 1 new instance / 20s, 60s idle timeout (keep_alive up to 10 min), Quick Actions 1/10s, crawl 5 jobs/day / 100 pages. Workers Paid: no daily hour cap (priced), 200 concurrent, 3 new/s, 30 Quick Actions/s.

<!-- NOTES:END -->
