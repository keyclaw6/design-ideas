# Obscura — Rust headless browser for agent-scale automation

`web-obscura-sh` · website · product · en · [source](https://obscura.sh) · [raw](../../../raw/items/web-obscura-sh/)
**Author:** Obscura (@obscura_sh) · **Published:** — · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** browser, mcp

**Summary.** Marketing site for an open-source Rust headless browser aimed at agents: sub-50ms session boot, fresh sandboxes, lower memory than Chrome, Playwright/CDP compatible, with docs and MCP server guides.
**Question it answers.** Why use a purpose-built headless browser instead of Chrome per agent session?

**Claims.**
- `web-obscura-sh#c1` (capability, stated) Obscura claims agent sessions boot in under 50 milliseconds on demand. — evidence: "Sessions boot in **<50 ms**" [linked-page]
- `web-obscura-sh#c2` (capability, stated) Existing Playwright and Puppeteer scripts can target Obscura via CDP compatibility. — evidence: "Playwright + CDP compatible — point existing scripts at Obscura" [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md)
**Tools.** [obscura](../../tools/obscura.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), https://docs.obscura.sh, https://docs.obscura.sh/llms.txt
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
