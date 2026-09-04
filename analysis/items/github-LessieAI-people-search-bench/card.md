# People Search Bench — open eval for AI people-search agents

`github-LessieAI-people-search-bench` · github · dataset · en · [source](https://github.com/LessieAI/people-search-bench) · [raw](../../../raw/items/github-LessieAI-people-search-bench/)
**Author:** LessieAI (@—) · **Published:** — · **Captured:** 2026-09-02T20:15:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [outbound-gtm-agents](../../subjects/outbound-gtm-agents/brief.md) · **Also:** — · **Roles:** reference, tool · **Platforms:** cli

**Summary.** MIT Python benchmark with 119 multilingual people-search queries scored on live web evidence (not LLM-as-judge). Reports relevance, coverage, and utility for Lessie, Exa, Claude Code, and Juicebox.
**Question it answers.** How do you evaluate AI people-search agents with reproducible, web-verified scoring?

**Claims.**
- `github-LessieAI-people-search-bench#c1` (benchmark, stated) Lessie leads the published overall score at 65.2 versus Exa 55.0 and Claude Code 46.0. — evidence: "| Lessie | 70.2 | 69.1 | 56.4 | 65.2 |" [linked-page]
- `github-LessieAI-people-search-bench#c2` (capability, stated) Scoring uses Tavily web search verification with Cohen's kappa 0.84 against human annotators. — evidence: "Verification uses live web search (Tavily API), not LLM-as-judge. Cohen's kappa = 0.84 with human annotators (per arXiv abstract)." [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** [people-search-eval](../../techniques/people-search-eval.md)
**Tools.** [lessie](../../tools/lessie.md), [exa](../../tools/exa.md), [juicebox-peoplegpt](../../tools/juicebox-peoplegpt.md)
**Links.** paper (https://arxiv.org/abs/2603.27476), product (https://lessie.ai), https://treg.to/people-search
**Related items.** [web-arxiv-2603-27476](../web-arxiv-2603-27476/card.md), [web-treg-people-search](../web-treg-people-search/card.md), [github-superdesigndev-treg](../github-superdesigndev-treg/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
