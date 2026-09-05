# Judgment worksheet: SERP & AI-answer visibility (serp-ai-visibility)

Owner alias: “syrups.” This file scores a short stack on the brief’s axes. It does not pick a product.

## serp-ai-visibility — short stack to try

Four jobs showed up in the 28 primary items. Treat them as separate loops, not one SaaS.

1. **First-party audit (agent-callable).** [iannuttall/seo](../../items/github-iannuttall-seo/card.md) + the author’s later note that he is drifting toward single-purpose tools ([x-2095055297949610427](../../items/x-2095055297949610427/card.md)). OpenSEO + DataforSEO is the self-host path ([x-2093013941412852083](../../items/x-2093013941412852083/card.md)).
2. **Index surfaces that are not Google.** Brave submit-url ([web-brave-submit-url](../../items/web-brave-submit-url/card.md), playbooks [x-2093964632562253866](../../items/x-2093964632562253866/card.md) and [x-2094688982940741816](../../items/x-2094688982940741816/card.md)). Pair with IndexNow on the CLI, not instead of GSC.
3. **Directory / free-tool pages (classic DR).** TinyShelf ([web-tinyshelf](../../items/web-tinyshelf/card.md), DR claim [x-2094328961522397530](../../items/x-2094328961522397530/card.md)), Sami’s 15 free directories ([x-2094684433546985907](../../items/x-2094684433546985907/card.md)), Bing-driven one-page tools ([x-2094770895021572502](../../items/x-2094770895021572502/card.md)). TinyLaunch is the paid variant of the same job.
4. **Citation / AEO tracking.** CrowdReply + MCP ([web-crowdreply](../../items/web-crowdreply/card.md), Grok-bot recipe [x-2094553318031024285](../../items/x-2094553318031024285/card.md)). nqz.ai is a prompt generator for unbranded queries, not a tracker ([web-nqz-ai-search-prompt-generator](../../items/web-nqz-ai-search-prompt-generator/card.md)).

Do not put Known Agency, SEO Wins, or the $25k / $100k AEO case-study posts in a first build. They are vendor copy or attributed revenue with no worksheet attached.

## serp-ai-visibility — axis scores

Scores are `high` / `mid` / `low` / `unknown` against the brief axes. `unknown` means the card only has a `stated` claim.

| item | time-to-first-index-or-citation | paid API/SaaS | first-party GSC/crawl | AEO/GEO not only SERP | agent-callable | evidence |
|---|---|---|---|---|---|---|
| github-iannuttall-seo | mid (audit, not citation) | low (local; Google APIs) | high | low | high (CLI/MCP) | README fetched: `seo` + `seo mcp install` ([seo-skill-cli](../../tools/seo-skill-cli.md)) |
| OpenSEO + DataforSEO | mid | mid (API usage) | mid | mid (AI Visibility named) | high (OpenSEO MCP + Search Console MCP) | openseo.so **63,307 B**; DataForSEO first-party ([openseo-so](../../tools/openseo-so.md)) |
| Brave submit-url | mid (index request only) | low | low | mid (Brave answers) | low (form; CAPTCHA) | stated; form not exercised |
| TinyShelf | high if badge accepted | low (free + badge) | low | low | low | directory live: 19 cats / ~657 listings (2026-09-04); DR 11→46 still tweet-only |
| TinyLaunch directories | mid (~10 days) | high | low | low | low | stated DR-band guarantee |
| Sami 15 directories | mid (48h claim) | low | low | low | low | stated; full sheet DM-gated |
| free one-page tools (Bing) | low (weeks of flat metrics) | low | mid (Bing WM) | low | mid (you ship HTML) | GSC 1.01M tweet-only; live hosts are ext/platform/arcade |
| CrowdReply | unknown | high | low | high | high (MCP) | homepage **1,136,240 B**; marketplace **40,000+** publishers / **5,000+** brands; MCP docs **58** snake ids vs **18**-row table; 4%→40% now in X article body, still not a tracker export |
| nqz.ai prompt generator | n/a (research aid) | low | low | high | low | stated 4×3 prompts, 10/hour |
| llms.txt nudge | mid (fetch rate, not rank) | low | n/a | high | low | stated 10/10; screenshot only |
| press-wire unbranded Qs | mid (weeks) | mid (wire fees) | low | high | low | stated 108 citations / +21% |
| Reddit SERP comments | mid | low | low | mid | low | stated; Filip counters shadowban risk |
| $25k / $100k AEO posts | unknown | unknown | unknown | high (claimed) | low | stated; no ledger |

## serp-ai-visibility — claims that need a receipt

These are load-bearing if someone acts on “syrups,” and every one is still `stated`:

- TinyShots DR 11→46 from TinyShelf alone ([x-2094328961522397530#c1](../../items/x-2094328961522397530/card.md)). Need an Ahrefs/Moz export, not a tweet.
- 108 repeating AI citations and +21% on unbranded prompts ([x-2094148909253943322](../../items/x-2094148909253943322/card.md)). Need the prompt set and the tracker.
- CrowdReply 4%→40% in 11 weeks ([x-2094553318031024285#c2](../../items/x-2094553318031024285/card.md)). **Now in the X article body** (14,763 chars via fxtwitter carrier `dawoodkhan254/2094451439573881015`): 847 domains / ~10% closed / 85 mentions; 76→127 of 847; 2→9 of 17 ChatGPT sources. Still first-party copy, not a tracker export. Do not collapse with `/features` “4% on Perplexity.”
- $100k traffic and $25k revenue AEO stories ([x-2093729321131368744](../../items/x-2093729321131368744/card.md), [x-2094450512938856802](../../items/x-2094450512938856802/card.md)). Treat as marketing until a property + date range shows up.
- llms.txt 10/10 fetch ([x-2088046188037902579](../../items/x-2088046188037902579/card.md)). Re-run the ten models; the screenshot is the only evidence.
- Brave 1,190 sessions / 1.34% ([x-2094688982940741816#c2](../../items/x-2094688982940741816/card.md)). Screenshot exists; property is unnamed.

The one claim that already has a useful counter-claim: Reddit comment SEO is capped by Filip at “1 of 5 comments” and warns about archived threads ([x-2094742312433684496#c2](../../items/x-2094742312433684496/card.md)).

## serp-ai-visibility — do not treat as load-bearing

- Grok “SEO bot / GEO bot” bundle ([x-2095231184531828762](../../items/x-2095231184531828762/card.md)) — capability copy, no audit artifact.
- SEO Wins $79 lifetime library ([web-seowins-io](../../items/web-seowins-io/card.md)) — paywalled tactics, not a runnable loop.
- Blogr LTD ladder **$199 / $399 / $499 · next $799** (3/10 left this pass). Topical authority is copy, not a map export ([blogr-ai](../../tools/blogr-ai.md)).
- Sami “reply LIST” sheet — the 15 names are in the post; the gated sheet is not in this bank.
- Hasan’s DR 71/75/50/57 workflow ([x-2093713466955649145](../../items/x-2093713466955649145/card.md)) — numbers without URLs or a date window. leftover12 product host is **elvixai.com** (**191,152 B**): $19/14d then $99/mo, 30 emails/day, 8% of 6,258. DR quartet is **not** on that page ([x-2093624705030959554#c4](../../items/x-2093624705030959554/card.md)).

## serp-ai-visibility — next capture work

1. CrowdReply homepage is live (**1,136,240 B**; quote-only “#1”). Marketplace **40,000+** publishers / **5,000+** brands. `/docs/mcp` names OAuth + **58** snake_case tool ids (not the 18-row marketing table). Features “4% on Perplexity” is a cross-model gap. X article **2094451432208711681** body is now on [crowdreply-mcp](../../tools/crowdreply-mcp.md) (4%→40% / 11 weeks + 847 / 85). Remaining: a keyed MCP session.
2. leftover21: GSC t.co loops to sibling tweet `2094338304070004768` (`#c10`). leftover19 FixMeBot is a writing assistant, not GSC proof. **1.01M / 16.3K** still tweet-screenshot only.
3. TinyShots listing is live on TinyShelf (`/tools/tinyshots` **7,594 B**). Product page **$39** early-bird / **97** spots / then **$49** ([tinyshots](../../tools/tinyshots.md)). DR 11→46 still tweet-only — need Ahrefs/Moz.
4. Exercise Brave submit-url in a headed browser; this pass got HTTP 429 on the form URL.
5. TinyShelf homepage listing counts are on [tinyshelf](../../tools/tinyshelf.md). DR receipt still missing. Sami’s 15 named directories this pass: SaaSHub / SourceForge / Indie Hackers / Wellfound **200**; six hosts **403**; StackShare **429** — do not hammer ([x-2094684433546985907#c4](../../items/x-2094684433546985907/card.md)). DR tiers and 48-hour approval stay tweet-only.
6. seoskill.dev is live (**120,656 B**; `npm i -g seo` + MCP). Homepage has **no “70+”**; that count stays on GitHub `iannuttall/seo` Apache-2.0 **463★** ([seo-skill-cli](../../tools/seo-skill-cli.md)).
7. leftover12 Hasan agent t.co → ElvixAI. First-party pricing + 8%/6,258 table are on the cards. Remaining: a GSC/Ahrefs export for 43+ / 145.9K / 484 and the tweet DR quartet.
8. leftover16: hidden `llms.txt` 10/10 leftover is not treg’s catalog `llms.txt` ([x-2088046188037902579#c3](../../items/x-2088046188037902579/card.md)). Publisher UA leftover is not Obscura ([x-2090837707069014224#c2](../../items/x-2090837707069014224/card.md)). leftover17: `seowins.io` **403** is now on the Reddit leftover and the $100k AEO leftover ([x-2094742312433684496#c3](../../items/x-2094742312433684496/card.md), [x-2093729321131368744#c2](../../items/x-2093729321131368744/card.md)). leftover18: Brave submit-url **429 / 73,802 B** and help **429 / 2,404 B** are now on the stub + two playbook leftovers — do not hammer ([web-brave-submit-url#c3](../../items/web-brave-submit-url/card.md)). LinkedIn 24h quoted t.co is X article **404 / 28,622 B**; neighbor known.agency **965,519 B** is vendor copy, not GSC proof ([x-2093990583576486268#c2](../../items/x-2093990583576486268/card.md)). Press-wire 108: coreyhaines.com TLS / .co EOF / GH **404**; conversionalchemy.com **2,487 B** is Shopify CRO — do not collapse ([x-2094148909253943322#c3](../../items/x-2094148909253943322/card.md)).
9. leftover22 unused first-party: TinyLaunch directories **106,620 B** / **691** listed / **$279** for 110 ([tinyshots](../../tools/tinyshots.md) `#c5`); keep.md **$10/mo** + ian.is ([seo-skill-cli](../../tools/seo-skill-cli.md) `#c4`); nqz generator **36,810 B** ([nqz-ai-search-prompt-generator](../../tools/nqz-ai-search-prompt-generator.md)); hridoyreh.com **77,652 B** vendor copy (`#c4`). DR 11→46 and Brave 1,190 stay tweet-screenshot only.
10. leftover23 unused `npmjs.com/package/seo` **403 / 5,650 B** Cloudflare — do not hammer ([seo-skill-cli](../../tools/seo-skill-cli.md); [x-2095055297949610427#c5](../../items/x-2095055297949610427/card.md)).
11. leftover24 unused GitHub `iannuttall/seo` Apache-2.0 **463★** first-party **70+** ([x-2095055297949610427#c6](../../items/x-2095055297949610427/card.md)). leftover24 unused CrowdReply citation-outreach **396,104 B**: **5,000+** / **1,860+** / **22,400+**; MCP stays keyed ([crowdreply-mcp](../../tools/crowdreply-mcp.md); [x-2094553318031024285#c6](../../items/x-2094553318031024285/card.md)).
