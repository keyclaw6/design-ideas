# SERP & AI-answer visibility (SEO / AEO / GEO) (serp-ai-visibility)

## serp-ai-visibility — scope

Getting a site or brand ranked or cited: classic SEO tooling and audits, AEO/GEO citation outreach, directory/backlink DR plays, indexing submissions (Brave/Bing/IndexNow/GSC), topical maps, free-tool pages, Reddit/LinkedIn ranking hacks, AI-crawler user-agent handling, visibility tracking (CrowdReply, OpenSEO, DataforSEO).

Exclusion: Outbound prospecting and cold email → outbound-gtm-agents. MCP wiring of SEO tools stays here (tool role).

Priority `now`. Owner aliases: syrups, SERP optimization, SEO, AEO, GEO.
Expected primary range [28, 45]. This roster has **28** primary and **7** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## serp-ai-visibility — what the owner is trying to decide

The owner called this lane “syrups” / SERP optimization. A later judge should decide which mix of classic SEO (audits, directories, IndexNow/GSC) and AEO/GEO (citation outreach, AI-crawler prompts, Brave/Bing submit) actually moves a brand into assistant answers — and which items are just directory spam.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## serp-ai-visibility — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=10, technique=13, example=9, claim-source=14, reference=9.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (9):
- [iannuttall/seo CLI and MCP for local SEO audits](../../items/github-iannuttall-seo/card.md) — tool, reference — Apache-licensed npm CLI (seoskill.dev) that runs technical SEO audits, Search Console and GA4 reports, competitor research, and IndexNow…
- [Brave Search submit-URL page for manual index refresh](../../items/web-brave-submit-url/card.md) — tool, reference — Brave Search public submit-url form where operators paste a URL to request re-fetch for index inclusion; capture notes…
- [CrowdReply — AI search visibility and citation-outreach platform](../../items/web-crowdreply/card.md) — tool, example — SaaS for tracking and improving brand citations in assistant answers (ChatGPT, Grok, Perplexity), with citation-outreach workflows and a…
- [nqz.ai free AI Search Prompt Generator for GEO pre-awareness queries](../../items/web-nqz-ai-search-prompt-generator/card.md) — tool, technique — Free nqz.ai tool that fetches one public URL and outputs four topics times three natural-language buyer prompts each for ChatGPT,…
- [TinyLaunch Directories — paid SaaS directory submission for DR lift](../../items/web-tinylaunch-directories/card.md) — tool, technique — TinyLaunch sells done-for-you manual submissions to a vetted list of launch directories, promising Domain Rating lifts with tiered…
- [TinyShelf: human-reviewed software directory for launch backlinks](../../items/web-tinyshelf/card.md) — tool, reference — TinyShelf is a curated, human-reviewed software directory with 19 categories and Google OAuth submission
- [OpenSEO plus DataforSEO API as open-source SEMrush replacement](../../items/x-2093013941412852083/card.md) — tool, example — Brendan O'Connell describes canceling SEMrush for DataforSEO API plus OpenSEO, a self-hostable open-source SEO stack on Cloudflare Workers
- [Ian Nuttall asks if his SEO CLI/skill is useful in production](../../items/x-2095055297949610427/card.md) — tool, claim-source — Ian Nuttall solicits feedback on his Apache-2.0 seo CLI and MCP server (70+ audit tools, local crawl plus GSC/GA4) linked from…
- [Blogr.ai topical maps versus one-keyword-at-a-time SEO](../../items/x-2095130625976176754/card.md) — tool, example — Serg introduces Blogr.ai topical maps built from live keyword data: hubs and subtopics with search volume, difficulty, intent, position,…

First role `technique` (11):
- [Hidden llms.txt anchor nudge raises model fetch rate to 10/10 runs](../../items/x-2088046188037902579/card.md) — technique, example — King Bootoshi shares a near-invisible /llms.txt link whose title tells browsing LLMs to read the file; after adding it every model…
- [Hasan Cagli five-step playbook for AI search SaaS mentions](../../items/x-2093624705030959554/card.md) — technique, claim-source — Hasan Cagli lists five long-term AEO tactics—money-keyword content, backlinks, third-party mentions, indexed LinkedIn/Reddit posts, and…
- [Hasan Cagli AI-agent workflow for DR 50–75 SEO backlinks](../../items/x-2093713466955649145/card.md) — technique, claim-source — Thread opener where Hasan Cagli says AI agents now automate most of his daily SEO backlink prospecting that used to take 2–3 hours…
- [Three-step Brave Search URL submission for site indexing](../../items/x-2093964632562253866/card.md) — technique, reference — Short X thread listing three steps to submit a website URL to Brave Search via search.brave.com/submit-url so the site can appear in…
- [Weekly unbranded press-wire releases earned 108 AI answer citations](../../items/x-2094148909253943322/card.md) — technique, claim-source — Corey Haines describes a weekly newswire press-release program written around unbranded buyer questions for AI citation; in weeks it…
- [TinyShelf free dofollow directory drove TinyShots DR 11 to 46 in days](../../items/x-2094328961522397530/card.md) — technique, claim-source — Christopher Woggon reports listing tinyshots.app on tinyshelf.co raised TinyShots DR from 11 to 46 in a few days with no other SEO work,…
- [CrowdReply Grok Bot setup for AI-answer citation outreach via MCP](../../items/x-2094553318031024285/card.md) — technique, tool — CrowdReply amplifies Dawood's X article as a three-step Grok Bot workflow: install a Chief of AI Visibility bot, connect CrowdReply MCP,…
- [Sami directory backlink tiers: 15 free DR sites for founders](../../items/x-2094684433546985907/card.md) — technique, reference — Sami | SEO AI note-tweet tiers 15 free directory backlinks (Crunchbase, G2, Product Hunt, Capterra, Clutch, etc.) that founders can…
- [Brave Search URL submit playbook with analytics referral proof](../../items/x-2094688982940741816/card.md) — technique, claim-source — Hridoy Reh advocates submitting sites to Brave Search via search.brave.com/submit-url and shows a GA table where search.brave.com…
- [Hridoy Reh six-step Reddit SERP comment SEO play with caveats](../../items/x-2094742312433684496/card.md) — technique, claim-source — Hridoy Reh outlines a six-step Reddit comment SEO tactic: find page-one Reddit threads, leave helpful comments with brand mentions, and…
- [Free one-page tools SEO playbook via Bing keyword research](../../items/x-2094770895021572502/card.md) — technique, claim-source — Founder Artyom Shimanski explains programmatic SEO via free browser-only one-page tools: find demand in Bing Webmaster keyword research,…

First role `example` (1):
- [LinkedIn article hits Google page one for SEO in 2026 in 24h](../../items/x-2093990583576486268/card.md) — example, claim-source — Jake Zward reports a LinkedIn article targeting the query SEO in 2026 reached Google page one within 24 hours, attributing fast ranking…

First role `claim-source` (5):
- [Practitioner switched from Ahrefs to OpenSEO after audit credit walls](../../items/x-2087827123331383751/card.md) — claim-source, example — Practitioner rant about dropping a paid Ahrefs plan for OpenSEO.so after site audits stalled on credit limits, crawls failed, and MCP…
- [Publishers return different HTML to AI crawler user-agents](../../items/x-2090837707069014224/card.md) — claim-source, reference — Security researcher notes sites negotiate content by AI crawler User-Agent strings such as Claude-User or OpenAI File Downloader, with…
- [AEO case study: $100k+ traffic lift from AI search citations](../../items/x-2093729321131368744/card.md) — claim-source, example — alexgroberman claims a business added over $100,000 in ChatGPT, Google, and broader AI-search traffic after following article…
- [AEO case study claims $25k from ChatGPT, Google, and Perplexity](../../items/x-2094450512938856802/card.md) — claim-source, example — SEO practitioner cites a brand that followed his article advice and attributed more than $25,000 revenue to ChatGPT, Google, and…
- [Five layers of SEO in 2026 framework (Known.agency)](../../items/x-2094771557864292784/card.md) — claim-source, reference — Jake Ward argues 2026 SEO spans Google ranking, AI Overviews, ChatGPT recommendations, comparison SERPs, and influencing third-party…

First role `reference` (2):
- [Known Agency: Search Everywhere Optimisation for Google and AI answers](../../items/web-known-agency/card.md) — reference, example — Known positions as a Search Everywhere Optimisation agency covering AI answer citations, classic SEO, content, technical fixes, link…
- [SEO Wins paid database of 150+ SEO and AI-SEO tactics](../../items/web-seowins-io/card.md) — reference — Lifetime-access playbook library listing 150+ tested SEO and AI-SEO strategies for rankings, traffic, and LLM citations across Google,…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Free one-page tools SEO playbook via Bing keyword research](../../items/x-2094770895021572502/card.md)

Secondary membership (7), not in the primary count:
- [awesome-mcp-servers curated MCP index (~94k stars) with Glama sync](../../items/github-punkpeye-awesome-mcp-servers/card.md) — primary `mcp-and-agent-browsers`
- [treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints](../../items/github-superdesigndev-treg/card.md) — primary `mcp-and-agent-browsers`
- [Cloudflare Kitesurf agent-first browser on Workers (Browser Run beta)](../../items/web-cloudflare-kitesurf/card.md) — primary `mcp-and-agent-browsers`
- [Graphed FDE marketing agents on warehouse plus MCP access](../../items/web-graphed/card.md) — primary `outbound-gtm-agents`
- [avoid-ai-writing CLI audits and rewrites AI prose patterns](../../items/x-2092656414351118647/card.md) — primary `design-agent-skills`
- [Paolo Trivellato three-part LinkedIn lead-magnet viral recipe](../../items/x-2095060844547592437/card.md) — primary `outbound-gtm-agents`
- [Nine Grok bots pitched as a full marketing stack including SEO and GEO](../../items/x-2095231184531828762/card.md) — primary `outbound-gtm-agents`

## serp-ai-visibility — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [serp-keyword-research](../../techniques/serp-keyword-research.md) — Classic keyword, topical-map, GSC/GA4, and recency-filter work that still feeds AEO briefs.
- [citation-outreach](../../techniques/citation-outreach.md) — Asking publishers and answer engines to cite a brand, then tracking whether ChatGPT/Perplexity/Grok actually do.
- [geo-prompt-testing](../../techniques/geo-prompt-testing.md) — Prompting AI crawlers and answer engines with unbranded questions to see if a domain is cited.
- [directory-submission](../../techniques/directory-submission.md) — Placing a site on dofollow / DR-tier directories and free-tool lists as an indexing and backlink play.
- [alternate-engine-indexing](../../techniques/alternate-engine-indexing.md) — Manual or API URL submit to Brave, Bing, IndexNow — not only Google Search Console.
- [grok-marketing-bot-stack](../../techniques/grok-marketing-bot-stack.md) — Bundles of Grok bots aimed at ads and outbound copy, usually thin wrappers.

## serp-ai-visibility — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [seo-skill-cli](../../tools/seo-skill-cli.md)
- [indexnow](../../tools/indexnow.md)
- [crowdreply-mcp](../../tools/crowdreply-mcp.md)
- [nqz-ai-search-prompt-generator](../../tools/nqz-ai-search-prompt-generator.md)
- [tinyshelf](../../tools/tinyshelf.md)
- [openseo-so](../../tools/openseo-so.md)
- [brave-submit-url](../../tools/brave-submit-url.md)
- [seo-cli](../../tools/seo-cli.md)
- [seoskill-dev](../../tools/seoskill-dev.md)
- [blogr-ai](../../tools/blogr-ai.md)

## serp-ai-visibility — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-iannuttall-seo#c1` | The repo provides a local CLI and MCP server for SEO audits using your crawl, Search Console, and GA4. | stated | [iannuttall/seo CLI and MCP for local …](../../items/github-iannuttall-seo/card.md) |
| `github-iannuttall-seo#c2` | MCP tools install into Cursor via seo mcp install. | stated | [iannuttall/seo CLI and MCP for local …](../../items/github-iannuttall-seo/card.md) |
| `web-brave-submit-url#c1` | Brave exposes a public page prompting operators to insert a URL to be re-fetched for indexing. | stated | [Brave Search submit-URL page for manu…](../../items/web-brave-submit-url/card.md) |
| `web-brave-submit-url#c2` | The jina capture warned the live form may require CAPTCHA or full client load and was not exercised. | stated | [Brave Search submit-URL page for manu…](../../items/web-brave-submit-url/card.md) |
| `web-crowdreply#c1` | CrowdReply exposes a remote MCP with 18+ tools for agent workflows. | stated | [CrowdReply — AI search visibility and…](../../items/web-crowdreply/card.md) |
| `web-known-agency#c1` | Services span AI search optimization for citations in answer engines plus SEO, content, technical, authority links, a… | stated | [Known Agency: Search Everywhere Optim…](../../items/web-known-agency/card.md) |
| `web-known-agency#c2` | First 30 days promise a visibility baseline across Google and AI surfaces, then opportunity-driven sprints rather tha… | stated | [Known Agency: Search Everywhere Optim…](../../items/web-known-agency/card.md) |
| `web-nqz-ai-search-prompt-generator#c1` | The generator returns four distinct topics with three intents each: discovery, comparison, and decision. | stated | [nqz.ai free AI Search Prompt Generato…](../../items/web-nqz-ai-search-prompt-generator/card.md) |
| `web-nqz-ai-search-prompt-generator#c2` | Visitors are limited to ten generations per hour with no account and no stored crawl data. | stated | [nqz.ai free AI Search Prompt Generato…](../../items/web-nqz-ai-search-prompt-generator/card.md) |
| `web-seowins-io#c1` | The product bundles 150+ step-by-step SEO and AI SEO strategies. | stated | [SEO Wins paid database of 150+ SEO an…](../../items/web-seowins-io/card.md) |
| `web-seowins-io#c2` | Lifetime license was $79 at capture (down from $179). | stated | [SEO Wins paid database of 150+ SEO an…](../../items/web-seowins-io/card.md) |
| `web-tinylaunch-directories#c1` | The 110-directory package guarantees minimum DR bands such as 15–20 when starting from DR 0–10. | stated | [TinyLaunch Directories — paid SaaS di…](../../items/web-tinylaunch-directories/card.md) |
| `web-tinylaunch-directories#c2` | Turnaround is roughly ten days from purchase through submissions and a full report. | stated | [TinyLaunch Directories — paid SaaS di…](../../items/web-tinylaunch-directories/card.md) |
| `web-tinyshelf#c1` | Every TinyShelf listing is reviewed before it goes live. | stated | [TinyShelf: human-reviewed software di…](../../items/web-tinyshelf/card.md) |
| `web-tinyshelf#c2` | Submit flow at /submit requires Google OAuth sign-in before a listing can be submitted. | stated | [TinyShelf: human-reviewed software di…](../../items/web-tinyshelf/card.md) |

Full set: claims.jsonl (76 rows)

## serp-ai-visibility — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- time-to-first-index-or-citation
- requires paid API or SaaS
- works from first-party crawl/GSC data
- covers assistant answers (AEO/GEO) not only classic SERP
- agent-callable (CLI/MCP) vs dashboard-only
- evidence quality (demonstrated vs stated)

## serp-ai-visibility — thread coverage

X items in primary roster: 20. captured_full=1, captured_partial=19, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2087827123331383751](../../items/x-2087827123331383751/thread.md) | captured_partial | 18 | 3 | 1 |
| [x-2088046188037902579](../../items/x-2088046188037902579/thread.md) | captured_partial | 6 | 2 | 1 |
| [x-2090837707069014224](../../items/x-2090837707069014224/thread.md) | captured_partial | 68 | 1 | 1 |
| [x-2093013941412852083](../../items/x-2093013941412852083/thread.md) | captured_partial | 57 | 3 | 2 |
| [x-2093624705030959554](../../items/x-2093624705030959554/thread.md) | captured_partial | 9 | 1 | 0 |
| [x-2093713466955649145](../../items/x-2093713466955649145/thread.md) | captured_partial | 10 | 1 | 0 |
| [x-2093729321131368744](../../items/x-2093729321131368744/thread.md) | captured_partial | 9 | 3 | 2 |
| [x-2093964632562253866](../../items/x-2093964632562253866/thread.md) | captured_partial | 18 | 1 | 0 |
| [x-2093990583576486268](../../items/x-2093990583576486268/thread.md) | captured_partial | 24 | 3 | 2 |
| [x-2094148909253943322](../../items/x-2094148909253943322/thread.md) | captured_partial | 22 | 3 | 2 |
| [x-2094328961522397530](../../items/x-2094328961522397530/thread.md) | captured_partial | 21 | 1 | 0 |
| [x-2094450512938856802](../../items/x-2094450512938856802/thread.md) | captured_full | 2 | 2 | 2 |
| [x-2094553318031024285](../../items/x-2094553318031024285/thread.md) | captured_partial | 8 | 3 | 2 |
| [x-2094684433546985907](../../items/x-2094684433546985907/thread.md) | captured_partial | 23 | 3 | 1 |
| [x-2094688982940741816](../../items/x-2094688982940741816/thread.md) | captured_partial | 13 | 3 | 1 |
| [x-2094742312433684496](../../items/x-2094742312433684496/thread.md) | captured_partial | 8 | 3 | 2 |
| [x-2094770895021572502](../../items/x-2094770895021572502/thread.md) | captured_partial | 26 | 3 | 2 |
| [x-2094771557864292784](../../items/x-2094771557864292784/thread.md) | captured_partial | 42 | 3 | 1 |
| [x-2095055297949610427](../../items/x-2095055297949610427/thread.md) | captured_partial | 38 | 3 | 2 |
| [x-2095130625976176754](../../items/x-2095130625976176754/thread.md) | captured_partial | 4 | 1 | 1 |

## serp-ai-visibility — gaps and open questions

Primary readiness: ready=7, ready-with-gaps=21. Gap tags: thread-partial=12, linked-page-unfetched=2, thread-failed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which citation-outreach vendors show a before/after in assistant answers, not just a dashboard screenshot?
- Is Brave submit-url still load-bearing once IndexNow + GSC are in the loop?
- How much of the “syrups” lane is directory DR vs actual AEO?

If this subject drops below 6 primary items after a future reclass, merge it into `a neighbour` and delete the folder.

## serp-ai-visibility — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [outbound-gtm-agents](../outbound-gtm-agents/brief.md)
- [mcp-and-agent-browsers](../mcp-and-agent-browsers/brief.md)
- [infographics-diagrams](../infographics-diagrams/brief.md)

