# Judgment worksheet: agent memory & company brains (agent-memory-knowledge)

Owner aliases: second brain, GBrain, context engineering. Harness mechanics stay in [agent-harness-loops](../agent-harness-loops/worksheet.md).

## agent-memory-knowledge — short stack to try

Three store types. Pick one write path.

1. **Filesystem / vault (git-shaped).** Ryven RAW → WIKI → CLAUDE.md (must-read) ([x-2093677274641969390](../../items/x-2093677274641969390/card.md)). Obsidian Mind vault template ([x-2088231655177924993](../../items/x-2088231655177924993/card.md)). Memoria snapshots/branches ([x-2087208634493095978](../../items/x-2087208634493095978/card.md)). OpenViking ls/tree/find memory (must-read) ([x-2091169290661838965](../../items/x-2091169290661838965/card.md)). EP Hermes four-layer prompt ([x-2086920236079681607](../../items/x-2086920236079681607/card.md)).
2. **Traces, not documents.** ReasoningBank success/failure trajectories (must-read) ([x-2087143369181114868](../../items/x-2087143369181114868/card.md)). gbrain-evals 97.6% R@5 without an LLM in the loop ([x-2094462971598754010](../../items/x-2094462971598754010/card.md)).
3. **Context as ETL / semantic layer.** Gasquez essay is the must-read contract ([web-davidgasquez-context-engineering](../../items/web-davidgasquez-context-engineering/card.md)). Anthropic self-service analytics ([web-anthropic-claude-self-service-data](../../items/web-anthropic-claude-self-service-data/card.md)). Cerebras Slack-distilled KB ([web-cerebras-knowledge-base](../../items/web-cerebras-knowledge-base/card.md)). Macomber post-AI data stack ([web-iandmacomber-post-ai-data-stack](../../items/web-iandmacomber-post-ai-data-stack/card.md)). Slite nine-architecture ebook (must-read map) ([x-2092918452423983363](../../items/x-2092918452423983363/card.md)).

PipesHub and Type are productized company brains. Sentrux scores a *codebase*, not a memory store.

## agent-memory-knowledge — axis scores

| item | store type | write path ETL vs chat residue | retrieval | works without paid memory SaaS | auditability |
|---|---|---|---|---|---|
| Ryven RAW/WIKI | files | ETL-ish (article: compile at ingest) | markdown + CLAUDE.md | no (Claude Desktop paid) | high (git) |
| Obsidian Mind | vault | template + chat residue | vault search | yes | high |
| Memoria | git-like DB | snapshots / branches | their API | OSS | high (rollback) |
| OpenViking | filesystem metaphor (`viking://`) | ingest → L0/L1 sidecars | find/search + L2 read | OSS AGPLv3 | high (traj + sidecars) |
| ReasoningBank | traces | success *and* failure | research retrieval | research / demo | mid (trajectories) |
| gbrain-evals | product + bench | unknown | 97.6% R@5 stated, no LLM-in-loop | unknown | bench, not the store |
| Gasquez essay | warehouse metaphor | ETL | semantic models | yes (method) | high (datasets) |
| Anthropic analytics | semantic layer | mapped entities, not raw SQL | governed metrics | Claude + warehouse | high if the layer is real |
| Cerebras KB | hybrid index | Slack/docs/GitHub extract | hybrid retrieval | internal | mid |
| Slite ebook | survey | n/a | n/a | n/a | comparison only |
| Type | hosted scopes | product writes | product | no | unknown |
| PipesHub | governed connectors | enterprise ingest | RAG + agents | OSS claimed | mid |
| Sentrux | codebase graph | scan | treemap | yes | architecture, not memory |
| EP Hermes prompt | markdown + memory layer | prompt-boot | unknown | yes | low (prompt only; LifeOS is a different product) |

## agent-memory-knowledge — claims that need a receipt

- gbrain “97.6% R@5” tweet vs **gbrain-evals README (2026-09-02, v0.48.2.0)**: official `recall_all@5` **93.19%** reranker off (438/470) / **95.32%** with Voyage rerank-2.5 (448/470). No generative LLM in the retrieval loop; reranker row adds one Voyage call. Different metric than the tweet.
- Cerebras 15,000+ questions/day — internal metric.
- OpenViking “Viking protocol” — docs table: L0 256 chars / L1 4000 chars / L2 unlimited; directory sidecars, not per-file ([openviking](../../tools/openviking.md)). FAQ “~100 / ~2000 tokens” is the gloss.
- ReasoningBank stores failures as well as successes — paper tables now on the tool NOTES **and** card `#c3` (WebArena Flash 48.8 vs 40.5; SWE Flash 38.8 vs 34.2; MaTTS Shopping 55.1 at k=5), re-extracted from arXiv `2509.25140v2` (13 pages). Live repo Apache-2.0 / **561** stars / description null (`#c4`). **Demo-only, not an official Google product**. Chinese post EN gloss + author compression rule (≤3 experiences, 1–3 sentences) on [reasoning-bank](../../tools/reasoning-bank.md). OpenReview still challenge-gated; thread still partial.
- Slite “nine architectures” / Gorgias 12,000 nodes — **tweet infographic only**. Public ebook page is a gated form; it states 149 teams surveyed, 10+ builders interviewed, four shared technical components, and (on the product blog) **55%** of self-built brains abandoned on upkeep ([filesystem-context-memory](../../techniques/filesystem-context-memory.md)).

## agent-memory-knowledge — do not treat as load-bearing

- Type product pitch — homepage is a shared Claude/Codex workspace + “company brain” line, not a three-layer schema ([x-2087955721732460791#c2](../../items/x-2087955721732460791/card.md)).
- Driscoll / Lieberman “intelligence layer” collage — argument, not a store. leftover15 first-party: Macomber essay **67,426 B** (llms.txt / Snowflake; no Turbopuffer); Anthropic **565,721 B** (95% / ~95%; drift ~95%→~65%); Cerebras blog **HTTP 500** this pass — do not retry ([x-2094558408259272998#c3](../../items/x-2094558408259272998/card.md)).
- Stanford Control Plane (secondary) — harness, not memory.

## agent-memory-knowledge — next capture work

1. leftover21: Slite Agent **536,317 B** / Sylph **195★** / Pletor Brain **119,137 B** are now on `#c8` — still no Gorgias **12,000**. gbrain-evals official `recall_all@5` **93.19% / 95.32%** vs tweet **97.6%** ([gbrain-evals](../../tools/gbrain-evals.md); [x-2094462971598754010#c5](../../items/x-2094462971598754010/card.md)). Ebook PDF still gated. Remaining: the gated PDF or a company-prod extract — not more vendor homepages.
2. leftover21: official rows are now on the evals card `#c5` — **93.19% / 95.32%** `recall_all@5`, not tweet **97.6%**. Keep the tweet as a different row.
3. Obsidian Mind tree + `/om-*` commands are on [obsidian-mind](../../tools/obsidian-mind.md). It is **not** Ryven’s stack. Tweet/infographic still has five automations + **4,000** RAW notes; quoted X article **2090496192136290304** has four prompts, **50–100** source threshold, and Claude Desktop paid — [filesystem-context-memory](../../techniques/filesystem-context-memory.md). `@imryven` GitHub user still **404**.
4. leftover21: README LoCoMo **80–83%** / tokens **34.3–91.0%**; config guide names VLM providers and says L0/L1 degrade without VLM (`#c9`). Local `ov abstract` still not ready. Remaining: a keyed VLM-backed L0 abstract.
5. Sentrux is first-party on [sentrux](../../tools/sentrux.md): MIT **3,170★**; README **52** languages; public `plugins` tree **50** dirs this pass. Do not collapse. Tweet 52 matches the README, not the tree.
6. leftover12 EP Hermes prompt: reply pointed at Daniel Miessler LifeOS. First-party `danielmiessler/LifeOS` MIT **18,886★**, `ourlifeos.ai` **113,753 B**. README names a Hermes sidecar. Do not collapse the tweet prompt with LifeOS, Mushen’s Hermes layer, or Nous hermes-agent ([hermes](../../tools/hermes.md); [x-2086920236079681607#c4](../../items/x-2086920236079681607/card.md)).
7. leftover15 Driscoll-linked essays are now first-party on [context-etl](../../techniques/context-etl.md). Cerebras blog **500** this pass — do not retry. Remaining tweet-only SERP leftovers (llms.txt 10/10, $100k AEO, LinkedIn 24h, press-wire 108) have no first-party host after t.co loops.
8. leftover22 unused arXiv **2604.03927** is MatrixOne **data** VCS, not “git for AI agent memory” ([memoria](../../tools/memoria.md); [x-2087208634493095978#c4](../../items/x-2087208634493095978/card.md)).
