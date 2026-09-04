# Obscura — Apache-2.0 Rust headless browser for agent automation

`github-h4ckf0r0day-obscura` · github · repo · en · [source](https://github.com/h4ckf0r0day/obscura) · [raw](../../../raw/items/github-h4ckf0r0day-obscura/)
**Author:** h4ckf0r0day (@h4ckf0r0day) · **Published:** 2026-04-13T10:31:41Z · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** browser, mcp, cli

**Summary.** Apache-2.0 Rust headless browser (~24k stars) for AI agents and scraping: V8 JS, CDP on port 9222, Puppeteer/Playwright drop-in, native screenshot/PDF without Chromium, plus docs and MCP server guide.
**Question it answers.** What open-source headless browser replaces Chromium for agent sessions with CDP compatibility?

**Claims.**
- `github-h4ckf0r0day-obscura#c1` (benchmark, stated) README claims Obscura uses about 30 MB RAM versus 200+ MB for headless Chrome. — evidence: "Memory | 30 MB | 200+ MB" [linked-page]
- `github-h4ckf0r0day-obscura#c2` (capability, stated) Obscura is a drop-in replacement for Puppeteer and Playwright with native rendering and no Chromium dependency. — evidence: "acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright" [linked-page]
**Numbers.** GitHub stars: 23989 stars (linked-page); claimed page load: 85 ms (linked-page)
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md)
**Tools.** [obscura](../../tools/obscura.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), product (https://obscura.sh), https://docs.obscura.sh, https://docs.obscura.sh/llms.txt
**Related items.** [web-obscura-sh](../web-obscura-sh/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md), [x-2094427822064279870](../x-2094427822064279870/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: [web-obscura-sh](../web-obscura-sh/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md)
