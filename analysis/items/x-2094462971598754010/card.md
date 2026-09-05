# Garry Tan gbrain-evals: SOTA memory retrieval without LLM-in-loop

`x-2094462971598754010` · x · repo · en · [source](https://x.com/garrytan/status/2094462971598754010) · [raw](../../../raw/items/x-2094462971598754010/)
**Author:** Garry Tan (@garrytan) · **Published:** 2026-08-31T16:31:00Z · **Captured:** 2026-09-02T18:49:18Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** tool, claim-source · **Platforms:** other

**Summary.** Garry Tan announces new gbrain-evals benchmarks showing gbrain retrieval at 97.6% R@5 on LongMemEval without an LLM in the retrieval loop, plus memory-save evals from agent transcripts. Attached table compares read, write, and volunteer-memory arenas.
**Question it answers.** What benchmark numbers does Garry Tan cite for gbrain memory retrieval and save paths?

**Claims.**
- `x-2094462971598754010#c1` (benchmark, stated) LongMemEval reading memory back scores 97.6% R@5 with no LLM in the retrieval loop. — evidence: "97.6% R@5 with no LLM in the retrieval loop" [media]
- `x-2094462971598754010#c2` (benchmark, stated) Cat 35 write-path eval reports 88.1% salient content survives into usable pages. — evidence: "88.1% of salient content survives into pages rated 91% usable" [media]
- `x-2094462971598754010#c3` (capability, stated) Author added evals for memory-save from agent transcript as the best enrichment path. — evidence: "I've also added evals for memory-save from agent transcript, which is the best way to enrich your brain" [post]
- `x-2094462971598754010#c4` (availability, demonstrated) github.com/garrytan/gbrain MIT, 29,591 stars this pass. Description: Garry's Opinionated OpenClaw/Hermes Agent Brain. Root includes evals/, .gbrain-evals/, skills/, plugin/. This is the product repo; gbrain-evals SOTA integers stay on the evals card, not this listing. — evidence: "GitHub API 2026-09-05: 29591 stars MIT." [note]
**Numbers.** LongMemEval R@5: 97.6 percent (media); Cat 35 salient content survival: 88.1 percent (media); gbrain-evals repo stars at capture: 406  (note)
**Recipe.** —
**Techniques.** [autoresearch-loop](../../techniques/autoresearch-loop.md), [filesystem-context-memory](../../techniques/filesystem-context-memory.md)
**Tools.** [gbrain](../../tools/gbrain.md), [gbrain-evals](../../tools/gbrain-evals.md)
**Links.** repo (https://github.com/garrytan/gbrain-evals), paper (https://arxiv.org/abs/2604.21284), product (https://github.com/garrytan/gbrain)
**Related items.** [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md), [x-2091169290661838965](../x-2091169290661838965/card.md), [x-2087143369181114868](../x-2087143369181114868/card.md)
**Media.**
`raw/items/x-2094462971598754010/media/photo.jpg` (image, carries_technique=false) — Comparison table with three arenas—reading memory back, writing memory down, volunteering memory—listing gbrain scores versus competitors and gap notes.
**Thread.** captured_partial · reported 101 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md)
