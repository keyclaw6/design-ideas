# Context Engineering Is a Data Problem — David Gasquez essay

`web-davidgasquez-context-engineering` · website · article · en · [source](https://davidgasquez.com/context-engineering-is-a-data-problem) · [raw](../../../raw/items/web-davidgasquez-context-engineering/)
**Author:** David Gasquez (@davidgasquez) · **Published:** — · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** reference, claim-source · **Platforms:** —

**Summary.** Essay arguing organizational context should be built like a data warehouse: extract raw sources, transform into org-specific models, and publish curated text artifacts for agents. Treats knowledge bases as compilers and curated files as materialized views optimized for LLM consumption.
**Question it answers.** Why should agent context be modeled like a data warehouse instead of stuffing every raw source into prompts?

**Claims.**
- `web-davidgasquez-context-engineering#c1` (opinion, stated) Context engineering is extract-filter-curate-model-publish work, analogous to analytics ETL. — evidence: "Context engineering is that same work: extracting, filtering, curating, modeling, and publishing artifacts to help the organization make better decisions." [linked-page]
- `web-davidgasquez-context-engineering#c2` (recipe, stated) A knowledge base should compile raw sources into LLM-optimized representations via extract, transform, publish stages. — evidence: "Knowledge base as **compiler for agents** — raw sources → LLM-optimized representations." [linked-page]
- `web-davidgasquez-context-engineering#c3` (capability, stated) Teams need per-area marts rather than one universal company context package. — evidence: "Build **marts** per area/team — no universal "company context" package" [linked-page]
- `web-davidgasquez-context-engineering#c4` (capability, demonstrated) Gasquez’s public handbook vault (davidgasquez/handbook) is 159 topic .md files in a flat wiki-link tree, including Context Engineering.md and Company Knowledge Management.md. It is a personal published vault, not a company Slack extract. — evidence: "Git trees/main: 164 blobs / 159 md. Context Engineering.md 5989 B restates extract/transform/publish and no single company brain." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [context-etl](../../techniques/context-etl.md), [context-etl](../../techniques/context-etl.md)
**Tools.** —
**Links.** https://x.com/medriscoll/status/2094558408259272998, https://x.com/davidgasquez/status/2085803390391460099, https://www.cerebras.ai/blog/how-we-built-our-knowledge-base, https://www.iandmacomber.com/blog/post-ai-data-stack, https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude, https://www.context.ai/blog/a-filesystem-for-context
**Related items.** [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md), [web-anthropic-claude-self-service-data](../web-anthropic-claude-self-service-data/card.md), [web-chatgpt-training](../web-chatgpt-training/card.md), [web-blume-codes](../web-blume-codes/card.md)
**Media.** —
**Judge hints.** must_read: True · compare with: [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md)
