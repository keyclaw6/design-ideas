# People Search Bench

**Slug:** `people-search-bench` · **Kind:** library · **URL:** https://arxiv.org/abs/2603.27476 · **Canonical item:** [web-arxiv-2603-27476](../items/web-arxiv-2603-27476/card.md)
**Subjects:** [outbound-gtm-agents](../subjects/outbound-gtm-agents/brief.md)
**Referenced by (1):**
- [PeopleSearchBench: open benchmark for AI people-search platforms](../items/web-arxiv-2603-27476/card.md) — reference, technique — outbound-gtm-agents

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/LessieAI/people-search-bench + paper arXiv:2603.27476

**119 queries**, 4 scenarios (recruiting, B2B, expert, influencer), 3 dimensions graded on **web evidence (Tavily)**, not LLM-as-judge. MIT. Leaderboard Overall: Lessie 65.2, Exa 55.0, Claude Code 46.0, Juicebox 45.8. Relevance uses padded nDCG@10 (ideal assumes 10 perfect hits). treg is **not** on this table. Run the bench against treg before treating the router as measured.

**2026-09-04 capture — submission guide.** `docs/submission_guide.md` HTTP 200: run `data/queries/` JSONL through the platform; one CSV per category (`query_id`, `agent_name`, `name`, required `person_data`); up to **15** results/query; PR into `data/results/<platform>/`; maintainers re-run the eval. “Do not fabricate.” treg is still absent because nobody submitted those CSVs here.

**2026-09-05 leftover23.** Unused abs `arxiv.org/abs/2603.27476` **43,633 B** (v3 30 Aug 2026) folded onto the treg leftover. **119** queries / four scenarios / κ=**0.84**. Does not name treg #1. Receipt `leftover23-2026-09-05.json`.

**2026-09-05 leftover30.** Unused HTML `arxiv.org/html/2603.27476v3` **229,610 B** restates leftover23 **119** / κ=**0.84** and leftover27 Lessie **65.2 ± 1.5**. Does not name treg. Receipt `leftover30-2026-09-05.json`.
<!-- NOTES:END -->
