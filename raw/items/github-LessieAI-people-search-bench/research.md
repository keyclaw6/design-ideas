# Research

## What it is

MIT-licensed Python benchmark (LessieAI) for AI people-search agents: 119 multilingual queries, four job scenarios, and three scores graded against live web evidence rather than LLM-as-judge.

## How it works

- Pipeline: query → extract checkable criteria → verify each returned person via Tavily web search → grade → aggregate.
- Scenarios: recruiting (30), B2B prospecting (32), expert/deterministic (28), influencer/KOL (29) in EN/PT/ES/NL.
- Metrics: Relevance Precision (padded nDCG@10), Effective Coverage (task completion × qualified yield, K=10), Information Utility (completeness, evidence, actionability); overall is the equal-weight mean.
- Leaderboard at capture: Lessie 65.2, Exa 55.0, Claude Code 46.0, Juicebox 45.8 — Cohen's kappa 0.84 vs humans.
- Maintainer also sells Lessie; scoring still uses external web verification. Submission guide lives in `docs/submission_guide.md`.

## Why saved

Outbound and GEO work needs a factual eval for “find the right human,” not another RAG quiz. This is the library’s ground truth for people-search agents and for whether treg/tool catalogs actually lift Claude Code.

## Topics

`seo-agents`, `agent-skills`

## Related

`web-arxiv-2603-27476`, `web-treg-people-search`, `github-superdesigndev-treg`, `github-iannuttall-seo`, `github-romangojiberryAI-gojiberryai-sales-os`

## Use when

Evaluating or pitching people-search / enrichment agents; comparing treg vs naked Claude Code; designing recruiting or B2B prospecting evals that cannot be gamed by LLM-as-judge.
