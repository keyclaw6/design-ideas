# Outbound / GTM agent stacks (outbound-gtm-agents)

## outbound-gtm-agents — scope

Prospecting, people search, lead data, cold email/call sequencing, sales-OS agent teams, LinkedIn lead magnets, marketing agent bundles (Grok bots for ads/outbound).

Exclusion: Anything whose goal is ranking/citation → serp-ai-visibility.

Priority `standard`. Owner aliases: outbound, GTM, cold email, sales OS.
Expected primary range [12, 22]. This roster has **15** primary and **2** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## outbound-gtm-agents — what the owner is trying to decide

Decide whether people-search benches, sales-OS agent stacks, and Grok marketing bots are a workable outbound system or three disconnected promos. Ranking and citation work stays in serp-ai-visibility.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## outbound-gtm-agents — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=7, technique=7, example=4, claim-source=9, reference=2.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (6):
- [GojiberryAI Sales OS — 13-agent outbound stack on hosted MCP](../../items/github-romangojiberryAI-gojiberryai-sales-os/card.md) — tool, example — Open-source MIT sales department for Grok Bot and Claude Code: thirteen role agents from signal hunting through meeting qualification,…
- [Graphed FDE marketing agents on warehouse plus MCP access](../../items/web-graphed/card.md) — tool, example — Graphed embeds forward-deployed engineers to build marketing agents on a managed pipeline into Postgres, with agents for ads, SEO, cold…
- [treg people-search: one-token B2B enrichment across 60 providers](../../items/web-treg-people-search/card.md) — tool — treg people-search exposes 1B+ contacts via routed endpoints across 60 data providers with prepaid per-answer pricing and optional BYO keys
- [treg people-search: metered GTM enrichment at $0.0089 per lead](../../items/x-2094740953554932149/card.md) — tool, claim-source — Paul Mit amplifies Jason Zhou's treg people-search launch: an agent-facing catalog routing people enrichment across 60+ providers behind…
- [GojiberryAI open-sources 13-agent outbound sales OS for Grok Bot + MCP](../../items/x-2095081419202560010/card.md) — tool, technique — GojiberryAI published gojiberryai-sales-os: 13 markdown-defined sales agents (strategy, prospecting, intelligence, outreach) running in…
- [MapsData Google Maps lead scraping service pricing promo](../../items/x-2095214420398121034/card.md) — tool, claim-source — MapsData promo offering live Google Maps lead scraping at roughly thirty-three cents to ninety-eight cents per thousand leads, up to one…

First role `technique` (5):
- [Alex Vacca GTM channel-order playbook: warm-before-email lift](../../items/x-2094162743985308047/card.md) — technique, claim-source — Frontal founder Alex Vacca argues B2B GTM should sequence channels: exhaust one outbound motion, add founder LinkedIn, wire warm-content…
- [Cold-email IQ meme contrasts simple outreach vs infrastructure theater](../../items/x-2094893065202803014/card.md) — technique, claim-source — Cody Schneider's IQ-style thread argues effective cold email is a tight list, short problem-plus-offer copy, volume, and pipeline…
- [10k emails/day cold outbound stack: Instantly plus MapsData](../../items/x-2094927852399624557/card.md) — technique, claim-source — Levi Munneke posts a capacity formula for 10,000 cold emails per day using 500 inboxes across 167 domains with Instantly as sequencer…
- [Paolo Trivellato three-part LinkedIn lead-magnet viral recipe](../../items/x-2095060844547592437/card.md) — technique, claim-source — Starborn founder Paolo Trivellato breaks LinkedIn lead-magnet virality into thumbnail image, specific hook, and comment-gated…
- [Nine Grok bots pitched as a full marketing stack including SEO and GEO](../../items/x-2095231184531828762/card.md) — technique, claim-source — Thread pitching nine specialized Grok bots for marketing—ads, SEO audits that ship fixes, GEO ranking pages, Meta creative generation,…

First role `example` (2):
- [GojiberryAI MCP plus GrokBot: 97 prospects and 1 demo in 24h](../../items/x-2094326291906310180/card.md) — example, claim-source — GojiberryAI CEO case study wiring GrokBot to the Gojiberry MCP and LinkedIn to define ICP, enrich 97 prospects, personalize outreach,…
- [Gojiberry CEO launch — 13-agent outbound tree on hosted MCP for Grok Bot](../../items/x-2094892848042725416/card.md) — example, claim-source — Gojiberry CEO open-sources a 13-role outbound sales OS for Grok Bot: signal hunting through meeting qualification coordinated via hosted…

First role `reference` (2):
- [People Search Bench — open eval for AI people-search agents](../../items/github-LessieAI-people-search-bench/card.md) — reference, tool — MIT Python benchmark with 119 multilingual people-search queries scored on live web evidence (not LLM-as-judge)
- [PeopleSearchBench: open benchmark for AI people-search platforms](../../items/web-arxiv-2603-27476/card.md) — reference, technique — EMNLP 2026 Industry Track paper presenting PeopleSearchBench: 119 multilingual queries across recruiting, B2B sales, expert search, and…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Alex Vacca GTM channel-order playbook: warm-before-email lift](../../items/x-2094162743985308047/card.md)
- [GojiberryAI MCP plus GrokBot: 97 prospects and 1 demo in 24h](../../items/x-2094326291906310180/card.md)

Secondary membership (2), not in the primary count:
- [treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints](../../items/github-superdesigndev-treg/card.md) — primary `mcp-and-agent-browsers`
- [CrowdReply Grok Bot setup for AI-answer citation outreach via MCP](../../items/x-2094553318031024285/card.md) — primary `serp-ai-visibility`

## outbound-gtm-agents — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [people-search-eval](../../techniques/people-search-eval.md) — Benchmarks that score people-search tools on retrieval, not on marketing copy.
- [outbound-agent-pipeline](../../techniques/outbound-agent-pipeline.md) — Agent-run prospecting sequences across email/LinkedIn/call with a pipeline KPI, not vanity reply rate.
- [agent-browser-isolation](../../techniques/agent-browser-isolation.md) — Headless/isolated browsers and free search/fetch so an agent can hit the live web.
- [cold-email-sequence](../../techniques/cold-email-sequence.md) — Capacity math and simple sequences; warm the account before volume.
- [grok-marketing-bot-stack](../../techniques/grok-marketing-bot-stack.md) — Bundles of Grok bots aimed at ads and outbound copy, usually thin wrappers.

## outbound-gtm-agents — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [lessie](../../tools/lessie.md)
- [exa](../../tools/exa.md)
- [juicebox-peoplegpt](../../tools/juicebox-peoplegpt.md)
- [gojiberry-mcp](../../tools/gojiberry-mcp.md)
- [people-search-bench](../../tools/people-search-bench.md)
- [graphed-mcp](../../tools/graphed-mcp.md)
- [dataforseo](../../tools/dataforseo.md)
- [treg](../../tools/treg.md)
- [apollo-io](../../tools/apollo-io.md)
- [clay](../../tools/clay.md)
- [instantly](../../tools/instantly.md)
- [lemlist](../../tools/lemlist.md)
- [gojiberryai](../../tools/gojiberryai.md)
- [grok-bot](../../tools/grok-bot.md)
- [mapsdata](../../tools/mapsdata.md)

## outbound-gtm-agents — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-LessieAI-people-search-bench#c1` | Lessie leads the published overall score at 65.2 versus Exa 55.0 and Claude Code 46.0. | stated | [People Search Bench — open eval for A…](../../items/github-LessieAI-people-search-bench/card.md) |
| `github-LessieAI-people-search-bench#c2` | Scoring uses Tavily web search verification with Cohen's kappa 0.84 against human annotators. | stated | [People Search Bench — open eval for A…](../../items/github-LessieAI-people-search-bench/card.md) |
| `github-romangojiberryAI-gojiberryai-sales-os#c1` | The repo ships thirteen specialized outbound agents orchestrated through the GojiberryAI MCP. | stated | [GojiberryAI Sales OS — 13-agent outbo…](../../items/github-romangojiberryAI-gojiberryai-sales-os/card.md) |
| `github-romangojiberryAI-gojiberryai-sales-os#c2` | Cursor users can copy skills and point MCP at https://mcp.gojiberry.ai/mcp. | demonstrated | [GojiberryAI Sales OS — 13-agent outbo…](../../items/github-romangojiberryAI-gojiberryai-sales-os/card.md) |
| `web-arxiv-2603-27476#c1` | PeopleSearchBench comprises 119 multilingual queries across four people-search scenarios. | stated | [PeopleSearchBench: open benchmark for…](../../items/web-arxiv-2603-27476/card.md) |
| `web-arxiv-2603-27476#c2` | Criteria-Grounded Verification uses live web search to verify each returned person, achieving Cohen's kappa 0.84 with… | stated | [PeopleSearchBench: open benchmark for…](../../items/web-arxiv-2603-27476/card.md) |
| `web-graphed#c1` | Platform connects 750+ marketing data sources into a modeled warehouse. | stated | [Graphed FDE marketing agents on wareh…](../../items/web-graphed/card.md) |
| `web-graphed#c2` | Graphed MCP supports schema exploration and read-only ClickHouse SQL. | stated | [Graphed FDE marketing agents on wareh…](../../items/web-graphed/card.md) |
| `web-treg-people-search#c1` | Verified work email lookups start around $0.0089 per hit on catalog rates. | stated | [treg people-search: one-token B2B enr…](../../items/web-treg-people-search/card.md) |
| `web-treg-people-search#c2` | LessieAI bench cited: Claude Code + treg ~78.2% vs Claude alone ~43%. | stated | [treg people-search: one-token B2B enr…](../../items/web-treg-people-search/card.md) |
| `x-2094162743985308047#c1` | Repeating the same 1,000 cold emails tripled deals when the batch had already seen the sender's content 3+ times. | stated | [Alex Vacca GTM channel-order playbook…](../../items/x-2094162743985308047/card.md) |
| `x-2094162743985308047#c2` | Founder LinkedIn from a personal profile booked over 1,000 meetings in one year while the company page did little. | stated | [Alex Vacca GTM channel-order playbook…](../../items/x-2094162743985308047/card.md) |
| `x-2094162743985308047#c3` | Signal campaigns targeting account changes yield 5–11% reply rates versus 3–5% for title-based lists. | stated | [Alex Vacca GTM channel-order playbook…](../../items/x-2094162743985308047/card.md) |
| `x-2094326291906310180#c1` | Within 24 hours the GrokBot plus Gojiberry MCP stack contacted 97 prospects, saw 33 acceptances, 15+ replies, and boo… | stated | [GojiberryAI MCP plus GrokBot: 97 pros…](../../items/x-2094326291906310180/card.md) |
| `x-2094740953554932149#c1` | treg people-search charges $0.0089 per lead with no subscriptions. | stated | [treg people-search: metered GTM enric…](../../items/x-2094740953554932149/card.md) |

Full set: claims.jsonl (33 rows)

## outbound-gtm-agents — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- people-search precision vs recall documented
- requires paid data vendors
- agent-runnable sequence vs slideware
- channel coverage (email, LinkedIn, call)
- evaluation harness present

## outbound-gtm-agents — thread coverage

X items in primary roster: 10. captured_full=0, captured_partial=10, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2094162743985308047](../../items/x-2094162743985308047/thread.md) | captured_partial | 7 | 3 | 1 |
| [x-2094326291906310180](../../items/x-2094326291906310180/thread.md) | captured_partial | 12 | 1 | 0 |
| [x-2094740953554932149](../../items/x-2094740953554932149/thread.md) | captured_partial | 35 | 3 | 3 |
| [x-2094892848042725416](../../items/x-2094892848042725416/thread.md) | captured_partial | 197 | 1 | 0 |
| [x-2094893065202803014](../../items/x-2094893065202803014/thread.md) | captured_partial | 32 | 1 | 0 |
| [x-2094927852399624557](../../items/x-2094927852399624557/thread.md) | captured_partial | 13 | 3 | 1 |
| [x-2095060844547592437](../../items/x-2095060844547592437/thread.md) | captured_partial | 15 | 3 | 1 |
| [x-2095081419202560010](../../items/x-2095081419202560010/thread.md) | captured_partial | 157 | 1 | 0 |
| [x-2095214420398121034](../../items/x-2095214420398121034/thread.md) | captured_partial | 9 | 3 | 1 |
| [x-2095231184531828762](../../items/x-2095231184531828762/thread.md) | captured_partial | 24 | 1 | 0 |

## outbound-gtm-agents — gaps and open questions

Primary readiness: ready=5, ready-with-gaps=10. Gap tags: thread-partial=8, linked-page-unfetched=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Does PeopleSearchBench predict outbound reply rate or only retrieval F1?
- Are Grok marketing bots a channel or just wrappers around the same LLM?

If this subject drops below 6 primary items after a future reclass, merge it into `serp-ai-visibility` and delete the folder.

## outbound-gtm-agents — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [serp-ai-visibility](../serp-ai-visibility/brief.md)
- [agent-harness-loops](../agent-harness-loops/brief.md)
- [mcp-and-agent-browsers](../mcp-and-agent-browsers/brief.md)

