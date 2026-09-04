# MCP servers, tool routers, agent browsers, computer-use (mcp-and-agent-browsers)

## mcp-and-agent-browsers — scope

MCP server catalogs, tool routers (treg), headless/agent browsers (Obscura, Kitesurf, Kernel), mock stacks (aimock), screen parsers (OmniParser), free search/fetch APIs for agents, open Grok-Bot alternatives.

Exclusion: Domain MCPs (Blender MCP, CrowdReply MCP, Fusion MCP) are primary in their domain subject with mcp platform tag; this subject is secondary for them.

Priority `standard`. Owner aliases: MCP, agent browser, computer use.
Expected primary range [9, 16]. This roster has **11** primary and **22** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## mcp-and-agent-browsers — what the owner is trying to decide

Decide a default MCP + agent-browser kit (catalogs, routers, Obscura/Kitesurf). Domain MCPs (Blender, CrowdReply, Fusion) stay primary in their domain subject.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## mcp-and-agent-browsers — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=10, technique=1, example=0, claim-source=5, reference=5.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (9):
- [Obscura — Apache-2.0 Rust headless browser for agent automation](../../items/github-h4ckf0r0day-obscura/card.md) — tool, reference — Apache-2.0 Rust headless browser (~24k stars) for AI agents and scraping: V8 JS, CDP on port 9222, Puppeteer/Playwright drop-in, native…
- [treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints](../../items/github-superdesigndev-treg/card.md) — tool, claim-source — treg is a Python tools registry and proxy: one token routes agents to thousands of catalogued SEO, people-search, ads, and scraping APIs…
- [Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)](../../items/web-cloudflare-kitesurf/card.md) — tool, claim-source — Cloudflare blog introducing Kitesurf, an agent-first browser on Workers ported from Obscura
- [Obscura — Rust headless browser for agent-scale automation](../../items/web-obscura-sh/card.md) — tool, reference — Marketing site for an open-source Rust headless browser aimed at agents: sub-50ms session boot, fresh sandboxes, lower memory than…
- [CopilotKit aimock — single-port mock stack for LLM, MCP, and search](../../items/x-2087151521121419648/card.md) — tool — Launch post for @copilotkit/aimock, an open-source npm package that mocks LLM APIs, MCP, A2A, AG-UI, vector databases, and search on one…
- [KERNEL agent browsers add custom proxy CA bundle install](../../items/x-2087555254757757116/card.md) — tool, claim-source — KERNEL cloud agent browsers now accept a custom proxy with a CA bundle at creation time, automatically installing the certificate into…
- [Rakazo: Apache-2.0 open-source Grok Bot on pi harness](../../items/x-2087898602890744089/card.md) — tool, reference — Elie Steinbock announces Rakazo, an Apache-2.0 Grok Bot alternative using the pi harness with swappable LLMs and sandboxes (including…
- [Free agent web search and fetch pitched against Exa and Tavily pricing](../../items/x-2093050916953903451/card.md) — tool, claim-source — Pitch that agents can search and fetch any webpage for free with zero subscriptions, contrasting seven dollars per thousand searches on…
- [OmniParser: screenshot UI parsing so general LLMs can click screens](../../items/x-2093153416214114558/card.md) — tool, technique — OmniParser parses screenshots into labeled UI elements so general-purpose models (GPT-4o, DeepSeek R1, Qwen2.5VL) can click accurately…

First role `claim-source` (1):
- [Viral Obscura tweet — Rust agent browser at 30MB RAM, Puppeteer-compatible](../../items/x-2094427822064279870/card.md) — claim-source, reference — High-reach Spanish-language amplification of Obscura: claims a Rust headless browser for agents using 30MB RAM, 85ms loads, built-in…

First role `reference` (1):
- [awesome-mcp-servers curated MCP index (~94k stars) with Glama sync](../../items/github-punkpeye-awesome-mcp-servers/card.md) — reference, tool — Community-maintained awesome list of Model Context Protocol servers (~94k stars) with categorized README index, language/scope legend,…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints](../../items/github-superdesigndev-treg/card.md)
- [Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)](../../items/web-cloudflare-kitesurf/card.md)

Secondary membership (22), not in the primary count:
- [iannuttall/seo CLI and MCP for local SEO audits](../../items/github-iannuttall-seo/card.md) — primary `serp-ai-visibility`
- [GojiberryAI Sales OS — 13-agent outbound stack on hosted MCP](../../items/github-romangojiberryAI-gojiberryai-sales-os/card.md) — primary `outbound-gtm-agents`
- [AIDesigner remote MCP for in-repo HTML/Tailwind UI design](../../items/web-aidesigner-mcp/card.md) — primary `design-agent-skills`
- [CrowdReply — AI search visibility and citation-outreach platform](../../items/web-crowdreply/card.md) — primary `serp-ai-visibility`
- [DESIGNMD: Hyperbrowser-powered DESIGN.md extractor for any URL](../../items/web-design-md-hyperbrowser/card.md) — primary `design-agent-skills`
- [Microsoft Flint chart IL: compact specs compile to Vega, ECharts, Plotly](../../items/web-flint-chart/card.md) — primary `infographics-diagrams`
- [Originkit: 363+ free animated components with MCP import](../../items/web-originkit-dev/card.md) — primary `landing-ui-motion`
- [treg people-search: one-token B2B enrichment across 60 providers](../../items/web-treg-people-search/card.md) — primary `outbound-gtm-agents`
- [Cloudflare OS repo — Workers-based agent workspace](../../items/x-2087178722420171020/card.md) — primary `agent-harness-loops`
- [Orca design mode — on-page annotate and send to any AI agent](../../items/x-2087708050002239702/card.md) — primary `design-agent-skills`
- [Practitioner switched from Ahrefs to OpenSEO after audit credit walls](../../items/x-2087827123331383751/card.md) — primary `serp-ai-visibility`
- [Fusion MCP agents querying assemblies like a CAD database](../../items/x-2088296314484162719/card.md) — primary `ai-cad-hardware`
- [LangChain managed deep agent folder architecture (MDA)](../../items/x-2088345102540587356/card.md) — primary `agent-harness-loops`
- [Publishers return different HTML to AI crawler user-agents](../../items/x-2090837707069014224/card.md) — primary `serp-ai-visibility`
- [Spanish roundup of six trending GitHub AI agent repos](../../items/x-2091157554919280688/card.md) — primary `agent-harness-loops`
- [Higgsfield in Blender: prompt blockout, animate camera, reblock shots](../../items/x-2092255768770920506/card.md) — primary `blockout-to-video-flythrough`
- [GojiberryAI MCP plus GrokBot: 97 prospects and 1 demo in 24h](../../items/x-2094326291906310180/card.md) — primary `outbound-gtm-agents`
- [AIDesigner MCP clones site HTML and CSS into Claude Code projects](../../items/x-2094467179320119498/card.md) — primary `design-agent-skills`
- [treg people-search: metered GTM enrichment at $0.0089 per lead](../../items/x-2094740953554932149/card.md) — primary `outbound-gtm-agents`
- [Gojiberry CEO launch — 13-agent outbound tree on hosted MCP for Grok Bot](../../items/x-2094892848042725416/card.md) — primary `outbound-gtm-agents`
- … 2 more in items.jsonl

## mcp-and-agent-browsers — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [agent-browser-isolation](../../techniques/agent-browser-isolation.md) — Headless/isolated browsers and free search/fetch so an agent can hit the live web.
- [session-hardening](../../techniques/session-hardening.md) — Secrets, session migration, blast-radius, and worker isolation for long-running agents.

## mcp-and-agent-browsers — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [obscura](../../tools/obscura.md)
- [treg](../../tools/treg.md)
- [kitesurf](../../tools/kitesurf.md)
- [browser-run](../../tools/browser-run.md)
- [copilotkit-aimock](../../tools/copilotkit-aimock.md)
- [kernel-browser](../../tools/kernel-browser.md)
- [tiny-fish](../../tools/tiny-fish.md)
- [monidhq](../../tools/monidhq.md)

## mcp-and-agent-browsers — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-h4ckf0r0day-obscura#c1` | README claims Obscura uses about 30 MB RAM versus 200+ MB for headless Chrome. | stated | [Obscura — Apache-2.0 Rust headless br…](../../items/github-h4ckf0r0day-obscura/card.md) |
| `github-h4ckf0r0day-obscura#c2` | Obscura is a drop-in replacement for Puppeteer and Playwright with native rendering and no Chromium dependency. | stated | [Obscura — Apache-2.0 Rust headless br…](../../items/github-h4ckf0r0day-obscura/card.md) |
| `github-punkpeye-awesome-mcp-servers#c1` | The README indexes MCP servers by category with legend for language, local vs cloud scope, and OS. | stated | [awesome-mcp-servers curated MCP index…](../../items/github-punkpeye-awesome-mcp-servers/card.md) |
| `github-punkpeye-awesome-mcp-servers#c2` | Glama.ai/mcp/servers mirrors the list as a browsable web directory. | stated | [awesome-mcp-servers curated MCP index…](../../items/github-punkpeye-awesome-mcp-servers/card.md) |
| `github-superdesigndev-treg#c1` | treg catalogs 2,896 endpoints across 60 providers, priced per call from about one cent. | stated | [treg: OpenRouter-style proxy for 2,89…](../../items/github-superdesigndev-treg/card.md) |
| `github-superdesigndev-treg#c2` | Team-registered API keys always override treg's catalog keys and are never metered. | stated | [treg: OpenRouter-style proxy for 2,89…](../../items/github-superdesigndev-treg/card.md) |
| `web-cloudflare-kitesurf#c1` | Kitesurf originated as an Obscura port to Workers and shipped after a twelve-week production build. | stated | [Cloudflare Kitesurf agent-first brows…](../../items/web-cloudflare-kitesurf/card.md) |
| `web-cloudflare-kitesurf#c2` | The Engine exposes CDP WebSocket and HTTP REST compatible with Puppeteer, Playwright, and DevTools clients. | stated | [Cloudflare Kitesurf agent-first brows…](../../items/web-cloudflare-kitesurf/card.md) |
| `web-obscura-sh#c1` | Obscura claims agent sessions boot in under 50 milliseconds on demand. | stated | [Obscura — Rust headless browser for a…](../../items/web-obscura-sh/card.md) |
| `web-obscura-sh#c2` | Existing Playwright and Puppeteer scripts can target Obscura via CDP compatibility. | stated | [Obscura — Rust headless browser for a…](../../items/web-obscura-sh/card.md) |
| `x-2087151521121419648#c1` | aimock exposes the full agent stack on one package and one port. | stated | [CopilotKit aimock — single-port mock …](../../items/x-2087151521121419648/card.md) |
| `x-2087151521121419648#c2` | Install is a single npm package command. | stated | [CopilotKit aimock — single-port mock …](../../items/x-2087151521121419648/card.md) |
| `x-2087555254757757116#c1` | KERNEL browsers support custom proxies with CA bundles passed at proxy creation. | stated | [KERNEL agent browsers add custom prox…](../../items/x-2087555254757757116/card.md) |
| `x-2087555254757757116#c2` | The supplied CA bundle is installed into the browser trust store automatically. | stated | [KERNEL agent browsers add custom prox…](../../items/x-2087555254757757116/card.md) |
| `x-2087898602890744089#c1` | Rakazo supports any LLM via pi harness and any sandbox provider or Docker. | stated | [Rakazo: Apache-2.0 open-source Grok B…](../../items/x-2087898602890744089/card.md) |

Full set: claims.jsonl (27 rows)

## mcp-and-agent-browsers — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- catalog vs runnable server
- isolation model (workers, headless browser)
- auth and secrets handling
- search/fetch without paid SERP API
- computer-use vs HTTP-only tools

## mcp-and-agent-browsers — thread coverage

X items in primary roster: 6. captured_full=0, captured_partial=5, empty=1, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2087151521121419648](../../items/x-2087151521121419648/thread.md) | empty | 0 | 0 | 0 |
| [x-2087555254757757116](../../items/x-2087555254757757116/thread.md) | captured_partial | 6 | 1 | 0 |
| [x-2087898602890744089](../../items/x-2087898602890744089/thread.md) | captured_partial | 61 | 3 | 1 |
| [x-2093050916953903451](../../items/x-2093050916953903451/thread.md) | captured_partial | 387 | 2 | 1 |
| [x-2093153416214114558](../../items/x-2093153416214114558/thread.md) | captured_partial | 7 | 1 | 1 |
| [x-2094427822064279870](../../items/x-2094427822064279870/thread.md) | captured_partial | 46 | 1 | 1 |

## mcp-and-agent-browsers — gaps and open questions

Primary readiness: ready=5, ready-with-gaps=6. Gap tags: linked-page-unfetched=1, thread-partial=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Obscura vs Kitesurf vs a headed Playwright MCP: isolation vs fidelity?
- Does awesome-mcp-servers help selection or only discovery?

If this subject drops below 6 primary items after a future reclass, merge it into `agent-harness-loops` and delete the folder.

## mcp-and-agent-browsers — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [agent-harness-loops](../agent-harness-loops/brief.md)
- [serp-ai-visibility](../serp-ai-visibility/brief.md)
- [outbound-gtm-agents](../outbound-gtm-agents/brief.md)

