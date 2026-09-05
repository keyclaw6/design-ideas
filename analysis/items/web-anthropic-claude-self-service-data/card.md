# Anthropic self-service analytics playbook: semantic layer, skills, and evals

`web-anthropic-claude-self-service-data` · website · article · en · [source](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) · [raw](../../../raw/items/web-anthropic-claude-self-service-data/)
**Author:** Anthropic (@—) · **Published:** 2026-06-03 · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** example, technique · **Platforms:** claude-code, mcp

**Summary.** Anthropic engineering post on automating business analytics with Claude by mapping questions to governed entities—not raw SQL generation. Canonical datasets, semantic layers, skills, freshness checks, and evals address ambiguity, staleness, and retrieval misses.
**Question it answers.** How did Anthropic automate most business analytics queries without agents inventing metric definitions?

**Claims.**
- `web-anthropic-claude-self-service-data#c1` (benchmark, stated) Anthropic reports roughly 95% of business analytics queries automated at about 95% aggregate accuracy. — evidence: "~95% of business analytics queries automated via Claude" [linked-page]
- `web-anthropic-claude-self-service-data#c2` (result, stated) Auto-generating metric definitions from raw tables failed evals because definitions stayed plausible but ambiguous. — evidence: "Auto-generating metric defs from raw tables **failed evals** (plausible but ambiguous defs)" [linked-page]
- `web-anthropic-claude-self-service-data#c3` (availability, demonstrated) leftover29 unused claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions 517,319 B titles Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions. Visible extract is a large product-nav shell around that title. leftover29 does not replay a Slack Tag session. Neighbor Macomber / Gasquez pages stay on their own cards. — evidence: "leftover29 anthropic-slack 517319 B. Title: Claude Tag for ad-hoc questions." [note]
- `web-anthropic-claude-self-service-data#c4` (availability, demonstrated) leftover30 unused iandmacomber.com and davidgasquez.com neighbor essays are leftover29 on those READY cards. No new integers. — evidence: "leftover30-2026-09-05.json skip leftover29 neighbor essays." [note]
**Numbers.** business analytics queries automated: 95 % (linked-page); aggregate query accuracy: 95 % (linked-page)
**Recipe.** —
**Techniques.** [semantic-layer-contract](../../techniques/semantic-layer-contract.md), [context-etl](../../techniques/context-etl.md), [context-etl](../../techniques/context-etl.md)
**Tools.** —
**Links.** https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions, https://www.iandmacomber.com/blog/post-ai-data-stack, https://davidgasquez.com/context-engineering-is-a-data-problem
**Related items.** [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md), [web-iandmacomber-post-ai-data-stack](../web-iandmacomber-post-ai-data-stack/card.md), [web-chatgpt-training](../web-chatgpt-training/card.md), [web-graphed](../web-graphed/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md)
