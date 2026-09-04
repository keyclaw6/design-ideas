# Context Etl

**Slug:** `context-etl` · **Owner subject:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Subjects:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md), [infographics-diagrams](../subjects/infographics-diagrams/brief.md)
**Referenced by (5):**
- [Anthropic self-service analytics playbook: semantic layer, skills, and evals](../items/web-anthropic-claude-self-service-data/card.md) — example, technique — agent-memory-knowledge
- [Context Engineering Is a Data Problem — David Gasquez essay](../items/web-davidgasquez-context-engineering/card.md) — reference, claim-source — agent-memory-knowledge
- [Ian Macomber essay on post-AI data stack and company reality](../items/web-iandmacomber-post-ai-data-stack/card.md) — reference, technique — agent-memory-knowledge
- [OpenViking: ByteDance agent memory with filesystem-style context search](../items/x-2091169290661838965/card.md) — tool, claim-source — agent-memory-knowledge
- [Slite company-brain ebook compares nine memory architectures](../items/x-2092918452423983363/card.md) — reference, claim-source — agent-memory-knowledge

<!-- NOTES:START -->
Treat context as an ETL job: canonical datasets, llms.txt products, company-brain taxonomy.
Owner subject: `agent-memory-knowledge`. Referenced by 5 item(s): web-anthropic-claude-self-service-data, web-davidgasquez-context-engineering, web-iandmacomber-post-ai-data-stack, x-2091169290661838965, x-2092918452423983363.
Score items that use this method on the owner brief's comparison axes. Do not treat the slug as a product name.
If a later pass splits this slug, file a registry alias — do not edit cards by hand.

Gasquez essay fetched 2026-09-04 (https://davidgasquez.com/context-engineering-is-a-data-problem, 2026-08-02):
1. **Extract** raw sources into a filesystem/DB, keep original shape (Slack JSON, Slides PDF).
2. **Transform** into org-specific artifacts (summarize, extract, clean) — no universal “correct” company knowledge.
3. **Publish** curated text files; embeddings only index those files (useful, expensive, disposable, optional).
A company brain is built/tested/released like a data product, not prompted by dumping every raw source into the agent. Direct raw access can beat a stale KB; the durable layer is the encoded definition of “truth” (like a dbt model for a key action).
<!-- NOTES:END -->
