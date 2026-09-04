# Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)

`web-cloudflare-kitesurf` · website · article · en · [source](https://blog.cloudflare.com/kitesurf/) · [raw](../../../raw/items/web-cloudflare-kitesurf/)
**Author:** Cloudflare (@—) · **Published:** 2026-08-06 · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** linked-page-unfetched
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** [serp-ai-visibility](../../subjects/serp-ai-visibility/brief.md) · **Roles:** tool, claim-source · **Platforms:** mcp, browser

**Summary.** Cloudflare blog introducing Kitesurf, an agent-first browser on Workers ported from Obscura. CDP-compatible Engine, PageScript, and PageRenderer run in Wasm with per-page isolation, stateless burst components, and free Browser Run beta access.
**Question it answers.** How does Cloudflare host an agent browser without per-session Chromium overhead?

**Claims.**
- `web-cloudflare-kitesurf#c1` (capability, stated) Kitesurf originated as an Obscura port to Workers and shipped after a twelve-week production build. — evidence: "Cloudflare ported Obscura to Workers with AI assistance; after a detailed success plan, prototype worked → 12-week build." [linked-page]
- `web-cloudflare-kitesurf#c2` (capability, stated) The Engine exposes CDP WebSocket and HTTP REST compatible with Puppeteer, Playwright, and DevTools clients. — evidence: "Engine — public CDP WebSocket + HTTP REST; session state; Puppeteer/Playwright/DevTools compatible." [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** [kitesurf](../../tools/kitesurf.md), [browser-run](../../tools/browser-run.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), product (https://developers.cloudflare.com/browser-run/), https://developers.cloudflare.com/browser-run/cdp/, https://developers.cloudflare.com/dynamic-workers/
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md), [github-punkpeye-awesome-mcp-servers](../github-punkpeye-awesome-mcp-servers/card.md), [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [web-aidesigner-mcp](../web-aidesigner-mcp/card.md)
**Media.** —
**Judge hints.** must_read: True · compare with: [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md)
