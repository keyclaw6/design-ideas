# Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)

`web-cloudflare-kitesurf` · website · article · en · [source](https://blog.cloudflare.com/kitesurf/) · [raw](../../../raw/items/web-cloudflare-kitesurf/)
**Author:** Cloudflare (@—) · **Published:** 2026-08-06 · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** [serp-ai-visibility](../../subjects/serp-ai-visibility/brief.md) · **Roles:** tool, claim-source · **Platforms:** mcp, browser

**Summary.** Cloudflare blog introducing Kitesurf, an agent-first browser on Workers ported from Obscura. CDP-compatible Engine, PageScript, and PageRenderer run in Wasm with per-page isolation, stateless burst components, and free Browser Run beta access.
**Question it answers.** How does Cloudflare host an agent browser without per-session Chromium overhead?

**Claims.**
- `web-cloudflare-kitesurf#c1` (capability, stated) Kitesurf originated as an Obscura port to Workers and shipped after a twelve-week production build. — evidence: "Cloudflare ported Obscura to Workers with AI assistance; after a detailed success plan, prototype worked → 12-week build." [linked-page]
- `web-cloudflare-kitesurf#c2` (capability, stated) The Engine exposes CDP WebSocket and HTTP REST compatible with Puppeteer, Playwright, and DevTools clients. — evidence: "Engine — public CDP WebSocket + HTTP REST; session state; Puppeteer/Playwright/DevTools compatible." [linked-page]
- `web-cloudflare-kitesurf#c3` (capability, stated) Browser Run CDP docs expose WebSocket /devtools/browser plus HTTP session create/list/new/close endpoints and require a token with Browser Rendering - Edit. — evidence: "POST /devtools/browser; GET .../json/list; PUT .../json/new; DELETE close; clients Puppeteer, Playwright, MCP" [linked-page]
- `web-cloudflare-kitesurf#c4` (capability, demonstrated) leftover28 unused developers.cloudflare.com/browser-run/ 138,466 B is the Browser Run overview: /content /screenshot /pdf /markdown /snapshot /accessibilityTree /scrape /json /links /crawl plus Live View / Human in the Loop / Session recording / WebMCP (Beta). leftover24/25 already have limits NOTES. leftover28 does not start a live Browser Run session (needs a CF token). — evidence: "leftover28 cf-browser-run 138466 B. Named REST actions + Beta Live View / WebMCP." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** [kitesurf](../../tools/kitesurf.md), [browser-run](../../tools/browser-run.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), product (https://developers.cloudflare.com/browser-run/), https://developers.cloudflare.com/browser-run/cdp/, https://developers.cloudflare.com/dynamic-workers/, https://developers.cloudflare.com/browser-run/
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md), [github-punkpeye-awesome-mcp-servers](../github-punkpeye-awesome-mcp-servers/card.md), [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
**Media.** —
**Judge hints.** must_read: True · compare with: [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md)
