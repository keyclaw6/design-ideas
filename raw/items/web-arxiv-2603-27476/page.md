# PeopleSearchBench

**URL:** https://arxiv.org/abs/2603.27476  
**PDF:** https://arxiv.org/pdf/2603.27476  
**HTML:** https://arxiv.org/html/2603.27476v3  
**DOI:** https://doi.org/10.48550/arXiv.2603.27476

**Authors:** Tianyu Shi, Wei Wang, Zequn Xie, Shuai Zhang, Boyang Xia, Chenyu Zeng, Qi Zhang, Lynn Ai, Yaqi Yu, Kaiming Zhang, Feiyue Tang, Zhenyu Yu, Lei Ding

**Subjects:** cs.AI, cs.LG · **Comments:** 25 pages  
**Venue (GitHub citation):** EMNLP 2026 Industry Track, Budapest

## Abstract

AI-powered people search platforms are increasingly deployed for recruiting, sales prospecting, and professional networking, yet no standardized benchmark exists for their rigorous evaluation. We present **PeopleSearchBench**, an open-source benchmark comprising **119 multilingual queries** across four scenarios: corporate recruiting, B2B sales prospecting, expert search, and influencer discovery.

A central contribution is **Criteria-Grounded Verification**: each query decomposes into explicit, independently checkable criteria; each returned individual is verified via **live web search**, producing factual relevance judgments rather than subjective LLM-as-judge scores (**Cohen's kappa = 0.84** with human annotators).

Four architecturally diverse platforms are evaluated along three dimensions — **Relevance Precision**, **Effective Coverage**, and **Information Utility**. Multi-source search agents significantly outperform single-domain systems, particularly in influencer discovery.

Platform rankings are robust across ablations on scoring thresholds, dimension weights, and judge models. All code, queries, and evaluation prompts are publicly available.

## Submission history

| Version | Date |
|---------|------|
| v1 | 2026-03-29 |
| v2 | 2026-07-27 |
| v3 | 2026-08-30 |

## Links

- Code: https://github.com/LessieAI/people-search-bench
- treg marketing cites bench: https://treg.to/people-search
