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
**Numbers.** —
**Recipe.** —
**Techniques.** [semantic-layer-contract](../../techniques/semantic-layer-contract.md), [semantic-layer-contract](../../techniques/semantic-layer-contract.md)
**Tools.** [reasoning-bank](../../tools/reasoning-bank.md)
**Links.** repo (https://github.com/google-research/reasoning-bank)
**Related items.** [x-2087208634493095978](../x-2087208634493095978/card.md), [x-2086920236079681607](../x-2086920236079681607/card.md)
**Media.** —
**Thread.** captured_partial · reported 39 · captured 2 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2087208634493095978](../x-2087208634493095978/card.md), [web-cerebras-knowledge-base](../web-cerebras-knowledge-base/card.md)
