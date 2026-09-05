# Agent memory, second brains, company knowledge bases (agent-memory-knowledge)

## agent-memory-knowledge — scope

Memory systems (GBrain, Memoria, ReasoningBank, Obsidian Mind, Type), company-brain/KB essays, context-engineering-as-ETL, semantic-layer analytics, enterprise knowledge connectors, post-AI data stack, intelligence-layer arguments.

Exclusion: Harness/loop mechanics → agent-harness-loops.

Priority `standard`. Owner aliases: second brain, GBrain, context engineering.
Expected primary range [12, 18]. This roster has **16** primary and **2** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## agent-memory-knowledge — what the owner is trying to decide

Decide a memory/KB stack: filesystem/Obsidian vaults vs semantic-layer/ETL vs ReasoningBank-style traces. Harness mechanics stay in agent-harness-loops.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## agent-memory-knowledge — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=7, technique=6, example=4, claim-source=6, reference=9.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (7):
- [ReasoningBank: Google Research memory from success and failure traces](../../items/x-2087143369181114868/card.md) — tool, reference — Chinese explainer thread for Google Research ReasoningBank: an open agent memory that stores reasoning trajectories from both successes…
- [Memoria — git-like snapshots and branches for AI agent memory](../../items/x-2087208634493095978/card.md) — tool, reference — Tom Dörr shares Memoria (matrixorigin/Memoria): a persistent agent memory layer with git-like snapshots, branches, merges, and rollbacks…
- [Sentrux Rust binary scores codebase architecture for agent sessions](../../items/x-2087239769877295158/card.md) — tool, technique — Sentrux is a pure-Rust architectural sensor that scans repo structure and dependencies into a live treemap and folds five root-cause…
- [Obsidian Mind vault gives Claude Code and Codex persistent project memory](../../items/x-2088231655177924993/card.md) — tool, example — Promotion of Obsidian Mind, an open-source Obsidian vault template that gives Claude Code, Codex CLI, and Gemini CLI persistent markdown…
- [PipesHub OSS governed context layer for enterprise RAG and agents](../../items/x-2088623462109593792/card.md) — tool, reference — Tom Doerr points to PipesHub (pipeshub-ai), an open-source governed context layer connecting enterprise knowledge for agents, RAG apps,…
- [OpenViking: ByteDance agent memory with filesystem-style context search](../../items/x-2091169290661838965/card.md) — tool, claim-source — Hype post for OpenViking (volcengine/OpenViking): a Viking-protocol memory layer where agents explore context with ls/tree/find at three…
- [Garry Tan gbrain-evals: SOTA memory retrieval without LLM-in-loop](../../items/x-2094462971598754010/card.md) — tool, claim-source — Garry Tan announces new gbrain-evals benchmarks showing gbrain retrieval at 97.6% R@5 on LongMemEval without an LLM in the retrieval…

First role `technique` (2):
- [EP Hermes agent prompt for four-layer personal second-brain OS](../../items/x-2086920236079681607/card.md) — technique, reference — Poster summarizes EP's single Hermes-agent prompt that boots four connected layers: a markdown knowledge base, a persistent memory…
- [Self-maintaining second brain: RAW, WIKI, CLAUDE.md, five automations](../../items/x-2093677274641969390/card.md) — technique, claim-source — Ryven describes a self-maintaining knowledge compiler replacing manual second brains: immutable RAW ingest, model-written WIKI, central…

First role `example` (3):
- [Anthropic self-service analytics playbook: semantic layer, skills, and evals](../../items/web-anthropic-claude-self-service-data/card.md) — example, technique — Anthropic engineering post on automating business analytics with Claude by mapping questions to governed entities—not raw SQL generation
- [Cerebras enterprise knowledge base: Slack distillation and hybrid retrieval](../../items/web-cerebras-knowledge-base/card.md) — example, technique — Cerebras engineering post on Cerebras Knowledge: an internal KB serving 15,000+ questions/day by extracting Slack, docs, GitHub, and…
- [Type product pitch: individual, team, and company agent memory layers](../../items/x-2087955721732460791/card.md) — example, reference — Type advertises a hosted company brain with separate memory scopes for individuals, teams, and the whole company that improves as people…

First role `claim-source` (1):
- [Driscoll essay on AI-native company intelligence layer with Ramp/Cerebras refs](../../items/x-2094558408259272998/card.md) — claim-source, reference — Michael Driscoll amplifies Lieberman's AI-native company feature #3—a centralized queryable intelligence layer—with a Da Vinci collage…

First role `reference` (3):
- [Context Engineering Is a Data Problem — David Gasquez essay](../../items/web-davidgasquez-context-engineering/card.md) — reference, claim-source — Essay arguing organizational context should be built like a data warehouse: extract raw sources, transform into org-specific models, and…
- [Ian Macomber essay on post-AI data stack and company reality](../../items/web-iandmacomber-post-ai-data-stack/card.md) — reference, technique — Ramp Head of Data essay arguing AI makes analysis cheap but consensus expensive: post-AI teams build a data-agent harness, governed…
- [Slite company-brain ebook compares nine memory architectures](../../items/x-2092918452423983363/card.md) — reference, claim-source — Slite thread and free ebook survey nine company-brain implementations — GBrain, mem0, Letta, Zep/Graphiti, Sylph, DIY git markdown,…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Context Engineering Is a Data Problem — David Gasquez essay](../../items/web-davidgasquez-context-engineering/card.md)
- [ReasoningBank: Google Research memory from success and failure traces](../../items/x-2087143369181114868/card.md)
- [OpenViking: ByteDance agent memory with filesystem-style context search](../../items/x-2091169290661838965/card.md)
- [Slite company-brain ebook compares nine memory architectures](../../items/x-2092918452423983363/card.md)
- [Self-maintaining second brain: RAW, WIKI, CLAUDE.md, five automations](../../items/x-2093677274641969390/card.md)

Secondary membership (2), not in the primary count:
- [Stanford Control Plane Pattern: replace brittle multi-agent handoff chains](../../items/x-2087254502210490739/card.md) — primary `agent-harness-loops`
- [system-atlas skill builds explorable isometric maps from one data file](../../items/x-2091559663833924082/card.md) — primary `infographics-diagrams`

## agent-memory-knowledge — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [semantic-layer-contract](../../techniques/semantic-layer-contract.md) — A semantic layer or reasoning-trace store the agent queries instead of raw tables.
- [context-etl](../../techniques/context-etl.md) — Treat context as an ETL job: canonical datasets, llms.txt products, company-brain taxonomy.
- [filesystem-context-memory](../../techniques/filesystem-context-memory.md) — Memory as a git-backed vault, transcript save, or markdown second brain.
- [agent-harness-ops](../../techniques/agent-harness-ops.md) — Harness, control plane, folder-as-agent, and multi-agent ops that a later judge can rerun.
- [autoresearch-loop](../../techniques/autoresearch-loop.md) — Self-improving research swarms with an eval, not a single long chat.

## agent-memory-knowledge — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [reasoning-bank](../../tools/reasoning-bank.md)
- [memoria](../../tools/memoria.md)
- [sentrux](../../tools/sentrux.md)
- [type](../../tools/type.md)
- [obsidian-mind](../../tools/obsidian-mind.md)
- [pipeshub](../../tools/pipeshub.md)
- [openviking](../../tools/openviking.md)
- [gbrain](../../tools/gbrain.md)
- [gbrain-evals](../../tools/gbrain-evals.md)

## agent-memory-knowledge — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `web-anthropic-claude-self-service-data#c1` | Anthropic reports roughly 95% of business analytics queries automated at about 95% aggregate accuracy. | stated | [Anthropic self-service analytics play…](../../items/web-anthropic-claude-self-service-data/card.md) |
| `web-anthropic-claude-self-service-data#c2` | Auto-generating metric definitions from raw tables failed evals because definitions stayed plausible but ambiguous. | stated | [Anthropic self-service analytics play…](../../items/web-anthropic-claude-self-service-data/card.md) |
| `web-cerebras-knowledge-base#c1` | Cerebras Knowledge handled 15,000+ internal questions per day within about three months of launch. | stated | [Cerebras enterprise knowledge base: S…](../../items/web-cerebras-knowledge-base/card.md) |
| `web-cerebras-knowledge-base#c2` | Slack ingestion re-fetches the entire thread on any new message and distills structured fields before embedding. | stated | [Cerebras enterprise knowledge base: S…](../../items/web-cerebras-knowledge-base/card.md) |
| `web-davidgasquez-context-engineering#c1` | Context engineering is extract-filter-curate-model-publish work, analogous to analytics ETL. | stated | [Context Engineering Is a Data Problem…](../../items/web-davidgasquez-context-engineering/card.md) |
| `web-davidgasquez-context-engineering#c2` | A knowledge base should compile raw sources into LLM-optimized representations via extract, transform, publish stages. | stated | [Context Engineering Is a Data Problem…](../../items/web-davidgasquez-context-engineering/card.md) |
| `web-davidgasquez-context-engineering#c3` | Teams need per-area marts rather than one universal company context package. | stated | [Context Engineering Is a Data Problem…](../../items/web-davidgasquez-context-engineering/card.md) |
| `web-iandmacomber-post-ai-data-stack#c1` | Post-AI data teams must enable self-serve AI analysis and champion one singular company reality. | stated | [Ian Macomber essay on post-AI data st…](../../items/web-iandmacomber-post-ai-data-stack/card.md) |
| `web-iandmacomber-post-ai-data-stack#c2` | Agent-readable dashboards should ship per-data-product llms.txt with owners, filters, and provenance instructions. | stated | [Ian Macomber essay on post-AI data st…](../../items/web-iandmacomber-post-ai-data-stack/card.md) |
| `web-iandmacomber-post-ai-data-stack#c3` | Semantic layer plus dbt tests act as the contract layer so agents do not invent metric definitions. | stated | [Ian Macomber essay on post-AI data st…](../../items/web-iandmacomber-post-ai-data-stack/card.md) |
| `x-2086920236079681607#c1` | Layer one is a markdown knowledge base that acts as the source of truth. | stated | [EP Hermes agent prompt for four-layer…](../../items/x-2086920236079681607/card.md) |
| `x-2086920236079681607#c2` | Layer two is a persistent memory pointer so every future session knows where the vault lives. | stated | [EP Hermes agent prompt for four-layer…](../../items/x-2086920236079681607/card.md) |
| `x-2087143369181114868#c1` | ReasoningBank stores reasoning process from both successful and failed trajectories, framing experience memory as a t… | stated | [ReasoningBank: Google Research memory…](../../items/x-2087143369181114868/card.md) |
| `x-2087143369181114868#c3` | arXiv:2509.25140v2 Table 1 WebArena Flash 48.8 vs 40.5; SWE Flash 38.8 vs 34.2; MaTTS Shopping 55.1 at k=5. | demonstrated | [ReasoningBank: Google Research memory…](../../items/x-2087143369181114868/card.md) |
| `x-2087208634493095978#c1` | Memoria versions AI agent memory with snapshots, branches, and merges. | stated | [Memoria — git-like snapshots and bran…](../../items/x-2087208634493095978/card.md) |
| `x-2087208634493095978#c2` | README positions Memoria as the first git for AI agent memory with zero-copy branching on MatrixOne. | stated | [Memoria — git-like snapshots and bran…](../../items/x-2087208634493095978/card.md) |

Full set: claims.jsonl (52 rows)

## agent-memory-knowledge — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- store type (files, vault, DB, traces)
- write path is ETL vs chat residue
- retrieval is semantic-layer or grep
- works without a paid memory SaaS
- auditability of what the agent remembers

## agent-memory-knowledge — thread coverage

X items in primary roster: 12. captured_full=1, captured_partial=11, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2086920236079681607](../../items/x-2086920236079681607/thread.md) | captured_partial | 33 | 3 | 2 |
| [x-2087143369181114868](../../items/x-2087143369181114868/thread.md) | captured_partial | 39 | 2 | 1 |
| [x-2087208634493095978](../../items/x-2087208634493095978/thread.md) | captured_partial | 4 | 3 | 2 |
| [x-2087239769877295158](../../items/x-2087239769877295158/thread.md) | captured_partial | 5 | 1 | 1 |
| [x-2087955721732460791](../../items/x-2087955721732460791/thread.md) | captured_partial | 17 | 3 | 2 |
| [x-2088231655177924993](../../items/x-2088231655177924993/thread.md) | captured_partial | 8 | 3 | 1 |
| [x-2088623462109593792](../../items/x-2088623462109593792/thread.md) | captured_full | 2 | 2 | 1 |
| [x-2091169290661838965](../../items/x-2091169290661838965/thread.md) | captured_partial | 4 | 1 | 0 |
| [x-2092918452423983363](../../items/x-2092918452423983363/thread.md) | captured_partial | 97 | 3 | 2 |
| [x-2093677274641969390](../../items/x-2093677274641969390/thread.md) | captured_partial | 17 | 3 | 2 |
| [x-2094462971598754010](../../items/x-2094462971598754010/thread.md) | captured_partial | 101 | 3 | 3 |
| [x-2094558408259272998](../../items/x-2094558408259272998/thread.md) | captured_partial | 7 | 3 | 2 |

## agent-memory-knowledge — gaps and open questions

Primary readiness: ready=5, ready-with-gaps=11. Gap tags: thread-partial=5, translation-needed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Is a git-backed markdown vault enough, or is a semantic layer required?
- Which memory write path an agent can audit after a week of sessions?

If this subject drops below 6 primary items after a future reclass, merge it into `agent-harness-loops` and delete the folder.

## agent-memory-knowledge — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [agent-harness-loops](../agent-harness-loops/brief.md)
- [infographics-diagrams](../infographics-diagrams/brief.md)

