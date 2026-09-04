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
- `github-h4ckf0r0day-obscura#c3` (result, demonstrated) Obscura 0.2.1 x86_64-linux fetch of example.com wrote a 17,130-byte 1280x720 PNG. Idle serve RSS was 24.5–25.1 MB; /json/version reports Chrome/145 CDP 1.3. — evidence: "screenshot PNG magic + 1280x720. serve --port 19222 RSS 24480–25068 KB. Binary 105616672 B. README 30 MB / 70 MB not collapsed with these." [note]
- `github-h4ckf0r0day-obscura#c4` (result, demonstrated) Obscura 0.2.1 serve RSS with example.com loaded over CDP was 37,856 KB (~37.0 MB), versus 24.5–25.1 MB idle on the same binary. Runtime.evaluate returned title Example Domain. — evidence: "serve --port 19233; Target.createTarget + attachToTarget; VmRSS 37856 kB x3; threads 9. See obscura NOTES." [note]
- `github-h4ckf0r0day-obscura#c5` (result, demonstrated) Obscura 0.2.1 fetch CLI of www.tinyshelf.co wrote a 73,559-byte 1280×720 PNG; eval returned title TinyShelf and body text length 13,883 with scrollHeight 3158. This is fetch, not serve RSS. — evidence: "fetch --eval title|body.innerText.length --screenshot analysis/_work/captures/obscura-tinyshelf.png; PNG 73559 B; scrollHeight 3158." [note]
- `github-h4ckf0r0day-obscura#c6` (result, demonstrated) Obscura 0.2.1 serve RSS with www.tinyshelf.co loaded over CDP was 73,080 KB (~71.4 MB) versus 25,108 KB idle on the same binary; Runtime.evaluate returned title TinyShelf, bodyLen 13883, scrollHeight 3158, 20 threads. — evidence: "serve --port 19255; Target.createTarget + attach; VmRSS 73080 kB x3 idle 25108 kB x3. Bank analysis/_work/captures/obscura-tinyshelf-cdp.json." [note]
**Numbers.** GitHub stars: 23989 stars (linked-page); claimed page load: 85 ms (linked-page)
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md)
**Tools.** [obscura](../../tools/obscura.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), product (https://obscura.sh), https://docs.obscura.sh, https://docs.obscura.sh/llms.txt
**Related items.** [web-obscura-sh](../web-obscura-sh/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md), [x-2094427822064279870](../x-2094427822064279870/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: [web-obscura-sh](../web-obscura-sh/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md)
