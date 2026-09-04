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
| OpenViking | filesystem metaphor | unknown | ls/tree/find claimed | OSS claimed | mid |
| ReasoningBank | traces | success *and* failure | research retrieval | research | mid (trajectories) |
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

- gbrain 97.6% R@5 on LongMemEval without an LLM in retrieval — need the eval harness, not the tweet.
- Cerebras 15,000+ questions/day — internal metric.
- OpenViking “Viking protocol” + three-level search — hype post; read the repo tree.
- ReasoningBank stores failures as well as successes — explainer thread; confirm against the paper.
- Slite “nine architectures” — ebook; extract the comparison table into claims.

## agent-memory-knowledge — do not treat as load-bearing

- Type product pitch — scopes without a schema.
- Driscoll / Lieberman “intelligence layer” collage — argument, not a store.
- Stanford Control Plane (secondary) — harness, not memory.

## agent-memory-knowledge — next capture work

1. Pull the Gasquez essay’s ETL steps into technique NOTES on `context-etl`.
2. Save gbrain-evals numbers from the repo/README.
3. Diff Ryven’s five automations against Obsidian Mind’s template files.
