# Ouroboros agent evolves tools and prompts via reviewed commits

`x-2087151807965401320` · x · announcement · en · [source](https://x.com/HuggingPapers/status/2087151807965401320) · [raw](../../../raw/items/x-2087151807965401320/)
**Author:** HuggingPapers (@HuggingPapers) · **Published:** — · **Captured:** 2026-09-04T07:01:46Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-failed
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** claim-source, reference · **Platforms:** —

**Summary.** HuggingPapers announces Ouroboros, a self-improving coding agent that evolves its own tools, prompts, and architecture through reviewed commits, citing SOTA terminal and OS benchmarks.
**Question it answers.** What benchmark numbers does the Ouroboros self-improving coding agent claim?

**Claims.**
- `x-2087151807965401320#c1` (capability, stated) Ouroboros evolves tools, prompts, and architecture through reviewed commits rather than silent self-rewrite. — evidence: "It can evolve its own tools, prompts, and architecture through reviewed commits." [post]
- `x-2087151807965401320#c2` (benchmark, stated) Ouroboros reports 86.74% on Terminal-Bench 2.1 and 90.69% on OSWorld-Verified. — evidence: "Achieves SOTA on Terminal-Bench 2.1 (86.74%), OSWorld-Verified (90.69%), and CL-Bench (0.2301)." [post]
- `x-2087151807965401320#c3` (benchmark, demonstrated) arXiv 2608.08311 abs GET 200 / 42,948 B. Title Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution (v3 2026-08-31). Abstract integers: Terminal-Bench 2.1 Opus 5 86.74%; OSWorld-Verified 90.69%; five-rollout CL-Bench 0.2301; Hope 161-day live evolution. Ranking language is the paper’s — quote the integers only. — evidence: "On Terminal-Bench 2.1, an Opus 5 run scores 86.74%... OSWorld-Verified... 90.69%... CL-Bench... 0.2301... Hope is... a 161-day living agent experiment." [note]
- `x-2087151807965401320#c4` (benchmark, demonstrated) https://ouroboros-agent.ai/benchmarks GET 200 / 6,553 B. Self-reported table: TB 2.1 Opus-5 86.74% after zeroing one reward-hack trial (raw 86.97%) vs Claude Code + Fable 5 83.8%; OSWorld-Verified Opus-5 90.69% vs previous public 90.19%; CL-Bench Sonnet-4.6 0.2301 vs previous 0.1960. SWE-bench Pro 58.2% vs Codex 59.4% (no significant difference). GAIA row marked pending traces. — evidence: "Terminal-Bench 2.1 Claude Opus-5 high 86.74% after zeroing one disclosed reward-hack trial (raw: 86.97%). analysis/_work/captures/2026-09-05-stale-next.json" [note]
- `x-2087151807965401320#c5` (availability, demonstrated) GitHub razzant/ouroboros is MIT, 1,265 stars / 614 forks this pass (born Feb 16, 2026 in the description). Do not collapse with Q00/ouroboros (5,769 stars, MIT, “Agent OS” / 14 runtimes) — different repo, different product. — evidence: "GET api.github.com/repos/razzant/ouroboros 200 license MIT stargazers_count 1265. Q00/ouroboros 5769 stars." [note]
**Numbers.** Terminal-Bench 2.1: 86.74 % (post); OSWorld-Verified: 90.69 % (post)
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** —
**Links.** repo (https://github.com/razzant/ouroboros), paper (https://arxiv.org/abs/2608.08311), product (https://ouroboros-agent.ai/)
**Related items.** [x-2032671842230501729](../x-2032671842230501729/card.md), [x-2080856252687745093](../x-2080856252687745093/card.md), [x-2074912810803560497](../x-2074912810803560497/card.md)
**Media.** —
**Thread.** failed · reported 2 · captured 0 · relevant 0 · author thread: unknown → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
