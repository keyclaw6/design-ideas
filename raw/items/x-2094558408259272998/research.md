## What they are actually doing

Michael Driscoll (Rill Data) is excerpting item **#3** from Alex Lieberman’s 30-feature “AI native company” list and treating it as a data-platform problem: one queryable layer over structured + unstructured data, documents, and business logic, with agents on top. He points at three public write-ups rather than announcing a Rill feature.

**Ramp — Ian Macomber**, “The Shape and Feel of the Post-AI Data Stack” (https://www.iandmacomber.com/blog/post-ai-data-stack). Tweet 2094161204579098774. Argument: the modern data stack’s reachable boundary expands to unstructured sources; a **data agent harness** (tools including MCPs, models, skills) sits on Snowflake (structured) + Turbopuffer (unstructured) with company context (semantic layer, lineage, domain docs, activity metadata) and a feedback loop of artifacts/evals. That diagram is the right-hand panel of Driscoll’s collage.

**Cerebras** — X article “How we built our knowledge base” (id 2077808214062825472) plus https://www.cerebras.ai/blog/how-we-built-our-knowledge-base, authors @hi_im_isaac_, @learnwdaniel, @gaozenghao. Preview: employees ask an internal KB 15,000+ times; interactive version on the blog. Left-hand collage panel matches a RAG funnel (sources → LLM extractors → embeddings/pgvector → six-list retrieval → RRF k=60 + LLM rerank → cited synthesis).

**Anthropic** — https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude (via @ClaudeDevs / @clementpzy): skills, data foundations, and evals for analysis agents.

Finlay’s reply frames the build vs buy question (Glean-like SaaS vs company-owned). David Gasquez maps #3 onto “context engineering is a data problem.”

Linked X statuses are **related_urls only** — no extra `x-*` folders in this capture.

## Open questions

- How much of Cerebras’s KB vs Ramp’s stack vs Anthropic’s analytics is the same “intelligence layer” vs three different products.
- RMB’s unread nested reply.
- Whether Rill’s own BI-for-agents work is meant as an implementation of #3 (not stated in the tweet).
