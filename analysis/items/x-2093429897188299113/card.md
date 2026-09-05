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
- `x-2093429897188299113#c3` (counter-claim, demonstrated) Neighbor REAP-288 HF README (sh0wie/Qwen3.8-Flash-Next-REAP-288-MLX-4bit) is 288 experts / 68 GB resident or 39 GB streamed / 91.5% HumanEval — not this leftover’s 60% experts-on-disk / 37 GB / 40 tok/s M4 Max. Unsloth Qwen3.8-27B Q4_0 file is 16.06 GB (tweet ~17 GB is a RAM envelope). Do not collapse 37 / 39 / 68. — evidence: "unsloth NOTES REAP-288 68 GB resident / 39 GB streamed; Q4_0 16056478688 B. leftover10 attach." [note]
**Numbers.** experts stored on disk: 60 % (post); resident memory with full experts: 37 GB (post); decode speed on M4 Max: 40 tok/s (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md)
**Tools.** —
**Links.** —
**Related items.** [x-2093160779960774982](../x-2093160779960774982/card.md)
**Media.**
`raw/items/x-2093429897188299113/media/media_0.jpg` (image, carries_technique=true) — Benchmark table comparing REAP-288 and full-model configs showing resident RAM, bare and MTP speeds, and quality percentages with a highlighted 37.3GB row.
**Thread.** captured_partial · reported 38 · captured 2 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2093160779960774982](../x-2093160779960774982/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
