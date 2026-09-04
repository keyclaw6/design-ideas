# HamsterResearch Qwen3.8-Flash REAP-288 MLX 4-bit runs 180B-class on 39GB

`x-2093160779960774982` · x · announcement · en · [source](https://x.com/EyalToledano/status/2093160779960774982) · [raw](../../../raw/items/x-2093160779960774982/)
**Author:** — (@EyalToledano) · **Published:** — · **Captured:** 2026-09-04T07:50:34Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** tool, claim-source · **Platforms:** other

**Summary.** Eyal Toledano announces HamsterResearch Qwen3.8-Flash-Next-REAP-288-MLX-4bit: MLX-native 4-bit quant pruned from 512 to 288 experts via REAP, claiming 91.5% HumanEval at 39GB VRAM.
**Question it answers.** What REAP-pruned MLX 4-bit quant lets a ~180B Qwen class model run in 39GB?

**Claims.**
- `x-2093160779960774982#c1` (capability, stated) REAP pruning cuts MoE experts from 512 to 288 with MLX 4-bit build 60% smaller than stock q4. — evidence: "Pruned 512→288 experts via REAP" [post]
- `x-2093160779960774982#c2` (benchmark, contested) Author claims 91.5% HumanEval versus 93.9% stock while fitting in 39GB memory. — evidence: "91.5% HumanEval (vs 93.9% stock)" [post]
**Numbers.** VRAM requirement: 39 GB (post); HumanEval score: 91.5 percent (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md), [dynamic-quantization](../../techniques/dynamic-quantization.md)
**Tools.** —
**Links.** https://huggingface.co
**Related items.** —
**Media.**
`media/media_0.jpg` (video, carries_technique=true) — Screen recording demo of the REAP-pruned Qwen MLX 4-bit model running locally with benchmark overlay.
**Thread.** captured_partial · reported 29 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: [] · compare with: —
