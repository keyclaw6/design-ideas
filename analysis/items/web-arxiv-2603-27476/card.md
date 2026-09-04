# PeopleSearchBench: open benchmark for AI people-search platforms

`web-arxiv-2603-27476` · website · paper · en · [source](https://arxiv.org/abs/2603.27476) · [raw](../../../raw/items/web-arxiv-2603-27476/)
**Author:** Tianyu Shi et al. (@—) · **Published:** 2026-08-30 · **Captured:** 2026-09-02T20:15:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [outbound-gtm-agents](../../subjects/outbound-gtm-agents/brief.md) · **Also:** — · **Roles:** reference, technique · **Platforms:** other

**Summary.** EMNLP 2026 Industry Track paper presenting PeopleSearchBench: 119 multilingual queries across recruiting, B2B sales, expert search, and influencer discovery, with Criteria-Grounded Verification via live web search (kappa 0.84).
**Question it answers.** How should AI people-search platforms be evaluated beyond subjective LLM-as-judge scoring?

**Claims.**
- `web-arxiv-2603-27476#c1` (benchmark, stated) PeopleSearchBench comprises 119 multilingual queries across four people-search scenarios. — evidence: "We present PeopleSearchBench, an open-source benchmark comprising 119 multilingual queries across four scenarios: corporate recruiting, B2B sales prospecting, expert search, and influencer discovery." [linked-page]
- `web-arxiv-2603-27476#c2` (result, stated) Criteria-Grounded Verification uses live web search to verify each returned person, achieving Cohen's kappa 0.84 with human annotators. — evidence: "each returned individual is verified via live web search, producing factual relevance judgments rather than subjective LLM-as-judge scores (Cohen's kappa = 0.84 with human annotators)." [linked-page]
**Numbers.** benchmark queries: 119  (linked-page); human agreement kappa: 0.84  (linked-page)
**Recipe.** —
**Techniques.** [outbound-agent-pipeline](../../techniques/outbound-agent-pipeline.md), [people-search-eval](../../techniques/people-search-eval.md)
**Tools.** [people-search-bench](../../tools/people-search-bench.md)
**Links.** repo (https://github.com/LessieAI/people-search-bench), paper (https://arxiv.org/pdf/2603.27476), product (https://treg.to/people-search), https://arxiv.org/html/2603.27476v3
**Related items.** [github-LessieAI-people-search-bench](../github-LessieAI-people-search-bench/card.md), [web-treg-people-search](../web-treg-people-search/card.md), [github-superdesigndev-treg](../github-superdesigndev-treg/card.md), [github-romangojiberryAI-gojiberryai-sales-os](../github-romangojiberryAI-gojiberryai-sales-os/card.md), [github-iannuttall-seo](../github-iannuttall-seo/card.md)
**Media.** —
**Judge hints.** must_read: [] · compare with: [github-LessieAI-people-search-bench](../github-LessieAI-people-search-bench/card.md)
