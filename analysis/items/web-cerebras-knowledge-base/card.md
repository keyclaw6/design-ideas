# Cerebras enterprise knowledge base: Slack distillation and hybrid retrieval

`web-cerebras-knowledge-base` · website · article · en · [source](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base) · [raw](../../../raw/items/web-cerebras-knowledge-base/)
**Author:** Cerebras (@—) · **Published:** — · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** example, technique · **Platforms:** other

**Summary.** Cerebras engineering post on Cerebras Knowledge: an internal KB serving 15,000+ questions/day by extracting Slack, docs, GitHub, and Jira in place. Core design is one Postgres embeddings table, LLM thread distillation, hybrid retrieval, and CocoIndex incremental code embeddings.
**Question it answers.** How did Cerebras build a company knowledge base that agents and humans query at scale?

**Claims.**
- `web-cerebras-knowledge-base#c1` (benchmark, stated) Cerebras Knowledge handled 15,000+ internal questions per day within about three months of launch. — evidence: "Claim at publish: **15,000+ questions/day**, widely adopted within ~3 months of launch." [linked-page]
- `web-cerebras-knowledge-base#c2` (recipe, stated) Slack ingestion re-fetches the entire thread on any new message and distills structured fields before embedding. — evidence: "re-fetch **entire thread** on any new message (parent + all replies as one row)" [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** https://x.com/medriscoll/status/2094558408259272998, https://x.com/cerebras/status/2077822555159945507, https://davidgasquez.com/context-engineering-is-a-data-problem, https://www.iandmacomber.com/blog/post-ai-data-stack
**Related items.** [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md), [web-anthropic-claude-self-service-data](../web-anthropic-claude-self-service-data/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md), [web-chatgpt-training](../web-chatgpt-training/card.md), [web-blume-codes](../web-blume-codes/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
