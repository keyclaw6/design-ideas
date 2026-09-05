# Reasoning Bank

**Slug:** `reasoning-bank` · **Kind:** repo · **URL:** https://github.com/google-research/reasoning-bank · **Canonical item:** [x-2087143369181114868](../items/x-2087143369181114868/card.md)
**Subjects:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Referenced by (1):**
- [ReasoningBank: Google Research memory from success and failure traces](../items/x-2087143369181114868/card.md) — tool, reference — agent-memory-knowledge

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/google-research/reasoning-bank

Memory from **success and failure** trajectories; “memory-aware test-time scaling” (MaTTS). Runnable code for **WebArena** (browsergym + docker) and **SWE-Bench** (mini-swe-agent). Paper: Ouyang et al., ICLR 2026, arXiv:2509.25140 (OpenReview forum gated this pass). Disclaimer: **not an official Google product**, demo-only, not for production. Failures-as-memory is in the README, not just the tweet.

Paper Table 1 WebArena overall SR / steps (684 tasks; Map excluded): Gemini-2.5-flash ReasoningBank **48.8 / 8.3** vs No Memory 40.5 / 9.7 (+8.3 SR). Gemini-2.5-pro **53.9 / 7.4** vs 46.7 / 8.8 (+7.2). Claude-3.7-sonnet **46.3 / 7.3** vs 41.7 / 8.0 (+4.6). Table 2 SWE-Bench-Verified: Flash **38.8** resolve / 27.5 steps vs 34.2 / 30.3; Pro **57.4** / 19.8 vs 54.0 / 21.1. MaTTS parallel on WebArena-Shopping: 49.7 (`k=1`) → **55.1** (`k=5`). Failures-as-memory ablation (Shopping, Flash): success-only 46.5 → with failures **49.7**; Synapse/AWM do not gain the same way. Google Research blog restates +8.3 WebArena / +4.6 SWE vs memory-free (Flash).

**2026-09-04 capture — Chinese post EN gloss** (`raw/items/x-2087143369181114868/post.md`). Agent memory should not store only successes; failed trajectories are also valuable; the **reasoning process** is the memory carrier, not just the outcome. ReasoningBank is framed as a third scaling axis beside parameters and test-time compute. MaTTS: memory makes test-time scaling more efficient; test-time exploration writes new experience back. Runnable code: SWE-Bench + WebArena; GPT 3.5/4/4o; WebArena llm-as-judge; **not an official Google product**. Author reply (captured; `is_author` is wrongly false in `thread.json` but the handle is `yibie`): do not dump raw failure traces; judge success/fail first, compress to **at most 3** reusable experiences of **1–3 sentences** each. Raw trajectory is evidence; the reflected strategy is retrievable memory. `translation-needed` dropped on the card; thread stays `captured_partial`.

**2026-09-04 recapture — paper PDF + live repo.** `GET https://arxiv.org/pdf/2509.25140` **200 / 5,545,249 B**, filename `2509.25140v2.pdf`, **13** pages (`analysis/_work/captures/reasoning-bank-arxiv-2509.25140v2.json`). pdfminer extract confirms Table 1 / Table 2 / MaTTS integers already on this page. GitHub API: Apache-2.0, **561** stars, **66** forks, `description` null, README **5,783** B, disclaimer still “not an officially supported Google product.” OpenReview `forum?id=jL7fwchScm` **307 → /challenge** this pass.

**2026-09-05 leftover20.** GitHub API now **562★** / 66 forks / Apache-2.0. README still **5,783 B**. Guessed `research.google/blog/reasoningbank*` **404**. Do not collapse 562 with 561.
<!-- NOTES:END -->
