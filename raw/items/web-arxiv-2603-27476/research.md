# Research

## What it is

arXiv:2603.27476 PeopleSearchBench (EMNLP 2026 Industry Track): academic write-up of the 119-query, four-scenario people-search benchmark with Criteria-Grounded Verification via live web search (kappa 0.84). Same artifact as github-LessieAI-people-search-bench.

## How it works

- Each query decomposes into independently checkable criteria; each returned person is verified on the live web — not LLM-as-judge.
- Dimensions: Relevance Precision, Effective Coverage, Information Utility.
- Multi-source search agents beat single-domain systems, especially influencer discovery; rankings hold under scoring ablations (per abstract).
- Authors include Lessie-affiliated names; treat as industry-track paper with vendor overlap, still the only open protocol.
- PDF/HTML on arXiv; GitHub holds queries and submission guide.

## Why saved

Citeable methodology when claiming people-search quality (e.g. treg + Claude vs Claude alone). Keep paper and repo as separate items: paper for method, repo for running the bench.

## Topics

`seo-agents`, `agent-skills`

## Related

`github-LessieAI-people-search-bench`, `web-treg-people-search`, `github-superdesigndev-treg`, `github-romangojiberryAI-gojiberryai-sales-os`, `github-iannuttall-seo`

## Use when

Citing evaluation methodology; writing about people-search agent quality; checking whether a vendor’s leaderboard matches the paper protocol.
