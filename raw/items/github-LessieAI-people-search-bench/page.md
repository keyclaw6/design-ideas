# People Search Bench

**Repo:** LessieAI/people-search-bench  
**Paper:** https://arxiv.org/abs/2603.27476  
**Stars:** 132 · **License:** MIT · **Language:** Python

The first open benchmark for evaluating AI-powered people search agents: 119 queries, 4 scenarios, 3 scoring dimensions, all graded against web evidence — not LLM opinion.

## Leaderboard (overall)

| Platform | Relevance Precision | Effective Coverage | Information Utility | Overall |
|----------|:-------------------:|:------------------:|:-------------------:|:-------:|
| Lessie | 70.2 | 69.1 | 56.4 | 65.2 |
| Exa | 53.8 | 58.1 | 53.1 | 55.0 |
| Claude Code | 54.3 | 41.1 | 42.7 | 46.0 |
| Juicebox (PeopleGPT) | 44.7 | 41.8 | 50.9 | 45.8 |

## Methodology

```
Query → Extract checkable criteria → Verify each person via web search → Grade → Aggregate
```

- **Relevance Precision** — padded nDCG@10 over per-person relevance grades
- **Effective Coverage** — task completion rate × qualified yield (capped at K=10)
- **Information Utility** — completeness, evidence quality, actionability
- **Overall** — equal-weight mean of the three

Verification uses live web search (Tavily API), not LLM-as-judge. Cohen's kappa = 0.84 with human annotators (per arXiv abstract).

## Query design

119 multilingual queries (EN, PT, ES, NL):

| Category | n | What it tests |
|----------|:-:|---------------|
| Recruiting | 30 | Skills + experience + location |
| B2B Prospecting | 32 | Decision-makers at target companies |
| Expert / Deterministic | 28 | Verifiable correct answers |
| Influencer / KOL | 29 | Cross-platform creator discovery |

Queries in [`data/queries/`](https://github.com/LessieAI/people-search-bench/tree/main/data/queries/).

## Platforms evaluated

| Platform | Type |
|----------|------|
| Lessie | AI Agent |
| Exa | Search API |
| Juicebox | AI Recruiting (800M+ profiles) |
| Claude Code | General AI Agent |

## Disclosure

Maintained by LessieAI (also an evaluated platform). Scoring uses external web verification; submission guide at `docs/submission_guide.md`.

## Links

- Paper: https://arxiv.org/abs/2603.27476
- Product: https://lessie.ai
- treg people-search page cites this bench: https://treg.to/people-search
