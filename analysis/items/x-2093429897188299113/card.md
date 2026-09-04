# Qwen expert-on-disk streaming runs full model in 37GB at 40 tok/s

`x-2093429897188299113` · x · demo-image · en · [source](https://x.com/EyalToledano/status/2093429897188299113) · [raw](../../../raw/items/x-2093429897188299113/)
**Author:** Eyal Toledano (@EyalToledano) · **Published:** — · **Captured:** 2026-09-04T06:49:46Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** technique, claim-source · **Platforms:** other

**Summary.** Follow-up on Qwen3.8-Flash-Next storing sixty percent of MoE experts on disk with on-demand streaming; author reports full-expert eval on thirty-seven gigabytes RAM decoding at forty tokens per second on an M4 Max.
**Question it answers.** How can MoE experts stream from disk to run a full Qwen model under forty gigabytes locally?

**Claims.**
- `x-2093429897188299113#c1` (capability, stated) Sixty percent of experts are stored on disk and stream to memory on demand, similar to n-gram streaming. — evidence: "I stored 60% of experts on disk which stream to memory on-demand. Similar technique as n-gram streaming" [post]
- `x-2093429897188299113#c2` (benchmark, stated) Full experts without pruning run in thirty-seven gigabytes and decode at forty tokens per second on M4 Max. — evidence: "Just eval'd with FULL experts (no prune) running on just 37gb of memory and decoding at 40 tok/s on my M4 Max" [post]
**Numbers.** experts stored on disk: 60 % (post); resident memory with full experts: 37 GB (post); decode speed on M4 Max: 40 tok/s (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md)
**Tools.** —
**Links.** —
**Related items.** [x-2093160779960774982](../x-2093160779960774982/card.md)
**Media.**
`media/media_0.jpg` (image, carries_technique=true) — Benchmark table comparing REAP-288 and full-model configs showing resident RAM, bare and MTP speeds, and quality percentages with a highlighted 37.3GB row.
**Thread.** captured_partial · reported 38 · captured 2 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: [] · compare with: [x-2093160779960774982](../x-2093160779960774982/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
