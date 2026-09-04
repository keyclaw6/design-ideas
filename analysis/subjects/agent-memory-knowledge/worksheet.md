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
| Ryven RAW/WIKI | files | ETL-ish (immutable RAW) | markdown + CLAUDE.md | yes | high (git) |
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
| EP Hermes prompt | markdown + memory layer | prompt-boot | unknown | yes | low (prompt only) |

## agent-memory-knowledge — claims that need a receipt

- gbrain “97.6% R@5” tweet vs **gbrain-evals README (2026-09-02, v0.48.2.0)**: official `recall_all@5` **93.19%** reranker off (438/470) / **95.32%** with Voyage rerank-2.5 (448/470). No generative LLM in the retrieval loop; reranker row adds one Voyage call. Different metric than the tweet.
- Cerebras 15,000+ questions/day — internal metric.
- OpenViking “Viking protocol” — docs table: L0 256 chars / L1 4000 chars / L2 unlimited; directory sidecars, not per-file ([openviking](../../tools/openviking.md)). FAQ “~100 / ~2000 tokens” is the gloss.
- ReasoningBank stores failures as well as successes — paper tables now on the tool NOTES (WebArena Flash 48.8 vs 40.5; SWE Flash 38.8 vs 34.2; MaTTS Shopping 55.1 at k=5). **Demo-only, not an official Google product**. Chinese post EN gloss + author compression rule (≤3 experiences, 1–3 sentences) on [reasoning-bank](../../tools/reasoning-bank.md). `translation-needed` dropped; thread still partial.
- Slite “nine architectures” / Gorgias 12,000 nodes — **tweet infographic only**. Public ebook page is a gated form; it states 149 teams surveyed, 10+ builders interviewed, four shared technical components, and (on the product blog) **55%** of self-built brains abandoned on upkeep ([filesystem-context-memory](../../techniques/filesystem-context-memory.md)).

## agent-memory-knowledge — do not treat as load-bearing

- Type product pitch — scopes without a schema.
- Driscoll / Lieberman “intelligence layer” collage — argument, not a store.
- Stanford Control Plane (secondary) — harness, not memory.

## agent-memory-knowledge — next capture work

1. Gasquez extract/transform/publish plus the public `davidgasquez/handbook` vault (**159** topic `.md` files, including Context Engineering.md) are on [context-etl](../../techniques/context-etl.md). Slite `/ebooks/company-brain` public TOC is “The Ontology of the Company Brain” plus four beats; the PDF is still a name/email form and the nine architecture names stay tweet-only ([filesystem-context-memory](../../techniques/filesystem-context-memory.md)). Remaining: a company-prod extract (Slack/CRM), not just the personal handbook.
2. gbrain-evals official rows are 93.19% / 95.32% `recall_all@5`, not 97.6%. Keep the tweet as marketing.
3. Obsidian Mind tree + `/om-*` commands are on [obsidian-mind](../../tools/obsidian-mind.md). It is **not** Ryven’s RAW/WIKI + five automations (those stay tweet-only; `@imryven` has no public GitHub user).
4. OpenViking MCP docs name **15 tools** on `:1933/mcp` — [openviking](../../tools/openviking.md). Local pip is **0.4.17.1**. A written `ov.conf` (local vectordb + `bge-small-zh-v1.5-f16`) makes doctor Config/dev-auth **PASS**; Embedding fails without `openviking[local-embed]`; VLM still needs a section. Studio is a JS shell; remaining: install the extra + one `ov ls viking://…`.
