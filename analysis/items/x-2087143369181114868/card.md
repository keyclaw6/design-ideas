# ReasoningBank: Google Research memory from success and failure traces

`x-2087143369181114868` · x · repo · zh · [source](https://x.com/yibie/status/2087143369181114868) · [raw](../../../raw/items/x-2087143369181114868/)
**Author:** yibie (@yibie) · **Published:** — · **Captured:** 2026-09-04T06:35:35Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** other

**Summary.** Chinese explainer thread for Google Research ReasoningBank: an open agent memory that stores reasoning trajectories from both successes and failures and pairs with memory-aware test-time scaling on SWE-Bench and WebArena.
**Question it answers.** How does ReasoningBank treat failed trajectories as memory and scale test-time search?

**Claims.**
- `x-2087143369181114868#c1` (capability, stated) ReasoningBank stores reasoning process from both successful and failed trajectories, framing experience memory as a third scaling axis beside parameters and test-time compute. — evidence: "失败的轨迹同样进记忆——推理过程（怎么走到那一步的）才是记忆的载体，而不只是结果" [post]
- `x-2087143369181114868#c2` (recipe, demonstrated) Author follow-up: do not dump raw failure traces; judge success/fail first, then compress to at most 3 reusable experiences of 1–3 sentences each. — evidence: "EN gloss of captured author reply (handle yibie): raw trajectory is evidence; the reflected strategy is the retrievable memory." [note]
- `x-2087143369181114868#c3` (benchmark, demonstrated) arXiv:2509.25140v2 (13 pages) Table 1 WebArena overall (684 tasks): Flash ReasoningBank 48.8 / 8.3 vs No Memory 40.5 / 9.7 (+8.3 SR). Pro 53.9 / 7.4 vs 46.7 / 8.8 (+7.2). Claude-3.7 46.3 / 7.3 vs 41.7 / 8.0 (+4.6). Table 2 SWE-Verified: Flash 38.8 / 27.5 vs 34.2 / 30.3; Pro 57.4 / 19.8 vs 54.0 / 21.1. MaTTS parallel Shopping 49.7 (k=1) → 55.1 (k=5). — evidence: "pdfminer extract of 2509.25140v2.pdf (5,545,249 B). Prose: improves overall SR on WebArena by +8.3, +7.2, and +4.6. Table 2 rows match. MaTTS parallel 49.7 to 55.1." [note]
- `x-2087143369181114868#c4` (availability, demonstrated) Live github.com/google-research/reasoning-bank is Apache-2.0, 561 stars / 66 forks, description null, README 5,783 B. Disclaimer: not an official Google product; demo-only. OpenReview forum jL7fwchScm was challenge-gated (307) this pass. — evidence: "GitHub API 2026-09-04: license Apache-2.0, stargazers_count 561, forks_count 66, description null. OpenReview Location=/challenge." [note]
- `x-2087143369181114868#c5` (availability, demonstrated) leftover20: live github.com/google-research/reasoning-bank is still Apache-2.0, now 562★ / 66 forks (prior pass 561★). README still 5,783 B and demo-only / not an official Google product. Guessed research.google/blog/reasoningbank* URLs are 404 this pass. OpenReview forum stays challenge-gated. Paper tables stay on #c3. — evidence: "leftover20-2026-09-05.json gh-reasoning-bank 562 Apache-2.0; rb-blog-a/b 404 132088 B; README 5783 B." [note]
- `x-2087143369181114868#c6` (availability, demonstrated) leftover24 unused arXiv 2509.25140 abs 45,267 B is still ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (Ouyang et al.; ICLR 2026; v2 16 Mar 2026; PDF 3,953 KB). Abstract names MaTTS and success+failure memory; Table 1 / Table 2 integers stay on earlier notes. OpenReview still gated. — evidence: "leftover24 reasoningbank-abs 45267 B. Title: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [semantic-layer-contract](../../techniques/semantic-layer-contract.md), [semantic-layer-contract](../../techniques/semantic-layer-contract.md)
**Tools.** [reasoning-bank](../../tools/reasoning-bank.md)
**Links.** repo (https://github.com/google-research/reasoning-bank), paper (https://arxiv.org/abs/2509.25140), https://github.com/google-research/reasoning-bank, https://arxiv.org/abs/2509.25140
**Related items.** [x-2087208634493095978](../x-2087208634493095978/card.md), [x-2086920236079681607](../x-2086920236079681607/card.md)
**Media.** —
**Thread.** captured_partial · reported 39 · captured 2 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2087208634493095978](../x-2087208634493095978/card.md), [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md)
