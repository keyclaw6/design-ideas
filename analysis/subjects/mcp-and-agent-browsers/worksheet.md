# Judgment worksheet: MCP, routers, agent browsers (mcp-and-agent-browsers)

Owner aliases: MCP, agent browser, computer use. Domain MCPs (Blender, CrowdReply, Fusion, AIDesigner) stay primary on their domain worksheets.

## mcp-and-agent-browsers — short stack to try

1. **One catalog, then one router.** awesome-mcp-servers ([github-punkpeye-awesome-mcp-servers](../../items/github-punkpeye-awesome-mcp-servers/card.md)). treg as the metered proxy (must-read) ([github-superdesigndev-treg](../../items/github-superdesigndev-treg/card.md)) — 2,896 endpoints stated.
2. **An isolated browser, not a shared Chrome profile.** Obscura Rust headless ([github-h4ckf0r0day-obscura](../../items/github-h4ckf0r0day-obscura/card.md), [web-obscura-sh](../../items/web-obscura-sh/card.md)). Kitesurf on Workers is the Cloudflare port (must-read) ([web-cloudflare-kitesurf](../../items/web-cloudflare-kitesurf/card.md)). KERNEL if you need a custom proxy CA ([x-2087555254757757116](../../items/x-2087555254757757116/card.md)).
3. **Mocks and parsers around the loop.** aimock single-port mocks ([x-2087151521121419648](../../items/x-2087151521121419648/card.md)). OmniParser for screenshot → click targets ([x-2093153416214114558](../../items/x-2093153416214114558/card.md)).
4. **Search/fetch without a SERP invoice.** The “free search vs Exa/Tavily” pitch ([x-2093050916953903451](../../items/x-2093050916953903451/card.md)) — treat as a cost argument until the endpoint is named.

Rakazo is an open Grok-Bot on the Pi harness ([x-2087898602890744089](../../items/x-2087898602890744089/card.md)), not a browser.

## mcp-and-agent-browsers — axis scores

| item | catalog vs runnable | isolation | auth / secrets | search/fetch without paid SERP | computer-use vs HTTP |
|---|---|---|---|---|---|
| awesome-mcp-servers | catalog | n/a | n/a | n/a | index |
| treg | runnable proxy | process, not browser | one token; BYO keys optional | routes *to* paid APIs | HTTP tools |
| Obscura | runnable browser | high (fresh sandbox, CDP) | local | can fetch pages | computer-use-ish (CDP) |
| Kitesurf | runnable (Workers beta) | Workers isolation | CF account | page fetch on CF | agent-first browser |
| KERNEL + CA bundle | hosted browsers | mid (cloud + your proxy) | CA install at create | via your proxy | browser |
| aimock | mock stack | n/a (localhost) | none | mocks search | HTTP mocks |
| OmniParser | parser | n/a | n/a | n/a | computer-use (clicks) |
| free search pitch | unknown endpoint | unknown | unknown | claimed | HTTP |
| Rakazo | Grok-Bot alt | sandboxes stated | unknown | n/a | harness, not browser |
| viral 30MB/85ms tweet | restates Obscura | claimed | n/a | n/a | browser |

## mcp-and-agent-browsers — claims that need a receipt

- treg 2,896 endpoints — must-read; count the catalog, do not trust the README integer.
- Obscura ~24k stars, sub-50ms boot, 30MB RAM, 85ms loads — marketing + viral restatement; time a session locally.
- Kitesurf “ported from Obscura” — Cloudflare blog; note what the Workers beta cannot do (downloads, extensions).
- Free search “$0 vs $7/1k” — name the API or drop the claim.
- OmniParser accuracy on GPT-4o / DeepSeek / Qwen — paper numbers, not in this capture.

## mcp-and-agent-browsers — do not treat as load-bearing

- Secondary domain MCPs — judge them on serp / outbound / design / CAD / blockout worksheets.
- fini-style shared-profile blast radius lives on the harness worksheet; it applies here if someone points Obscura at a logged-in cookie jar.

## mcp-and-agent-browsers — next capture work

1. `wc` the treg endpoint catalog.
2. Boot Obscura once; record RAM and a CDP screenshot of example.com.
3. Read the Kitesurf blog for Browser Run limits and write them on the card.
