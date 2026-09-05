# Publishers return different HTML to AI crawler user-agents

`x-2090837707069014224` · x · thread · en · [source](https://x.com/_can1357/status/2090837707069014224) · [raw](../../../raw/items/x-2090837707069014224/)
**Author:** _can1357 (@@_can1357) · **Published:** — · **Captured:** 2026-09-04T08:05:19Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [serp-ai-visibility](../../subjects/serp-ai-visibility/brief.md) · **Also:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Roles:** claim-source, reference · **Platforms:** browser, mcp

**Summary.** Security researcher notes sites negotiate content by AI crawler User-Agent strings such as Claude-User or OpenAI File Downloader, with LinkedIn serving less paywalled chrome to Claude-User. Attached table scores major sites across AI bots vs browsers.
**Question it answers.** Do major publishers serve different pages to AI crawlers than to normal browsers?

**Claims.**
- `x-2090837707069014224#c1` (result, stated) LinkedIn may strip clickbait or paywall chrome when the request uses Claude-User. — evidence: "Some sites like LinkedIn even remove their click-bait/paywall garbage if you're Claude-User" [post]
- `x-2090837707069014224#c2` (counter-claim, demonstrated) Neighbor in-bank Obscura is an Apache-2.0 Rust headless browser (v0.2.1; fetch CLI + CDP serve). TinyShelf CDP loaded RSS ~71.4 MB. That is an agent browser, not publisher User-Agent negotiation (Claude-User / GPTBot vs Chrome). The attached site×bot table stays screenshot-only. Do not collapse the two. — evidence: "obscura NOTES v0.2.1 fetch/CDP. This leftover is publisher UA HTML variance. leftover16 attach." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** [obscura](../../tools/obscura.md)
**Links.** —
**Related items.** [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/card.md), [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/card.md), [web-obscura-sh](../web-obscura-sh/card.md), [web-crowdreply](../web-crowdreply/card.md)
**Media.**
`raw/items/x-2090837707069014224/media/media_0.jpg` (image, carries_technique=false) — Table comparing NYTimes, LinkedIn, Reddit, and 30+ sites across Claude, GPTBot, Chrome, and curl access outcomes.
**Thread.** captured_partial · reported 68 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
