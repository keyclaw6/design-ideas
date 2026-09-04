# Reasoning Bank

**Slug:** `reasoning-bank` · **Kind:** repo · **URL:** https://github.com/google-research/reasoning-bank · **Canonical item:** [x-2087143369181114868](../items/x-2087143369181114868/card.md)
**Subjects:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Referenced by (1):**
- [ReasoningBank: Google Research memory from success and failure traces](../items/x-2087143369181114868/card.md) — tool, reference — agent-memory-knowledge

<!-- NOTES:START -->

Fetched 2026-09-04 README https://github.com/google-research/reasoning-bank

Memory from **success and failure** trajectories; “memory-aware test-time scaling” (MaTTS). Runnable code for **WebArena** (browsergym + docker) and **SWE-Bench** (mini-swe-agent). Paper: Ouyang et al., ICLR 2026, arXiv:2509.25140 (OpenReview forum gated this pass). Disclaimer: **not an official Google product**, demo-only, not for production. Failures-as-memory is in the README, not just the tweet.

Paper Table 1 WebArena overall SR / steps (684 tasks; Map excluded): Gemini-2.5-flash ReasoningBank **48.8 / 8.3** vs No Memory 40.5 / 9.7 (+8.3 SR). Gemini-2.5-pro **53.9 / 7.4** vs 46.7 / 8.8 (+7.2). Claude-3.7-sonnet **46.3 / 7.3** vs 41.7 / 8.0 (+4.6). Table 2 SWE-Bench-Verified: Flash **38.8** resolve / 27.5 steps vs 34.2 / 30.3; Pro **57.4** / 19.8 vs 54.0 / 21.1. MaTTS parallel on WebArena-Shopping: 49.7 (`k=1`) → **55.1** (`k=5`). Failures-as-memory ablation (Shopping, Flash): success-only 46.5 → with failures **49.7**; Synapse/AWM do not gain the same way. Google Research blog restates +8.3 WebArena / +4.6 SWE vs memory-free (Flash).

<!-- NOTES:END -->
