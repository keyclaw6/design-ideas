# Viral Obscura tweet — Rust agent browser at 30MB RAM, Puppeteer-compatible

`x-2094427822064279870` · x · thread · es · [source](https://x.com/0xJokker/status/2094427822064279870) · [raw](../../../raw/items/x-2094427822064279870/)
**Author:** Jokker (@0xJokker) · **Published:** 2026-08-31T14:11:20Z · **Captured:** 2026-09-02T18:33:15Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** — · **Roles:** claim-source, reference · **Platforms:** browser, cli

**Summary.** High-reach Spanish-language amplification of Obscura: claims a Rust headless browser for agents using 30MB RAM, 85ms loads, built-in anti-detect, native rendering without Chromium, and Puppeteer/Playwright compatibility; self-reply links the GitHub repo.
**Question it answers.** What performance and anti-detect claims drove Obscura's viral agent-browser tweet?

**Claims.**
- `x-2094427822064279870#c1` (benchmark, stated) Tweet claims Obscura consumes 30MB RAM, loads pages in 85ms, and blocks 3,500+ trackers automatically. — evidence: "> Consume 30MB de RAM
> Las paginas cargan en 85ms
> Bloquea +3.500 trackers automaticamente" [post]
- `x-2094427822064279870#c2` (capability, stated) Author positions Obscura as a direct Puppeteer and Playwright replacement with no Node.js dependencies in one binary. — evidence: "Es un reemplazo directo de Puppeteer y Playwright

Sin Nodejs. Sin dependencias. Un solo binario" [post]
- `x-2094427822064279870#c3` (availability, demonstrated) Immediate self-reply points to github.com/h4ckf0r0day/obscura as the repo behind the claims. — evidence: "> https://github.com/h4ckf0r0day/obscura" [author-thread]
- `x-2094427822064279870#c4` (counter-claim, demonstrated) Local 0.2.1 serve RSS is 25,108 KB idle, 37,856 KB with example.com, and 73,080 KB with tinyshelf.co — above the tweet's 30 MB RAM line. Do not treat 30 MB as a page-loaded session. — evidence: "Idle 25108 kB; example.com CDP 37856 kB; tinyshelf CDP 73080 kB. README/tweet 30 MB not collapsed. See obscura NOTES." [note]
- `x-2094427822064279870#c5` (capability, demonstrated) leftover24 unused obscura.sh 11,965 B titles Obscura · Give every agent its own browser. First-party: Star 16.2k; <50ms session start; 10× leaner memory vs Chrome; zero-state isolated sessions; CDP/Playwright. docs.obscura.sh 926,821 B is a GitBook SPA. Do not collapse 16.2k with local 0.2.1 RSS 25/37/73 MB or the tweet 30 MB line. — evidence: "leftover24 obscura-home 11965 B. Quote: <50ms Session start time 10× leaner Memory vs. Chrome." [note]
**Numbers.** GitHub stars at capture: 23982 stars (linked-page)
**Recipe.** —
**Techniques.** [agent-browser-isolation](../../techniques/agent-browser-isolation.md)
**Tools.** [obscura](../../tools/obscura.md)
**Links.** repo (https://github.com/h4ckf0r0day/obscura), product (https://obscura.sh), https://docs.obscura.sh, https://obscura.sh
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md)
**Media.**
`raw/items/x-2094427822064279870/media/photo.png` (image, carries_technique=false) — README crop showing Obscura wordmark, Trendshift number-one badge, and comparison table versus headless Chrome on memory, binary size, anti-detect, and page-load metrics.
**Thread.** captured_partial · reported 46 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../web-obscura-sh/card.md)
