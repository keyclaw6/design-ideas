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
- `x-2093160779960774982#c3` (benchmark, demonstrated) HF sh0wie/Qwen3.8-Flash-Next-REAP-288-MLX-4bit (not a HamsterResearch org). README table first-party: Base Q4 512 experts 98 GB disk / 97 GB resident / 93.9% HumanEval; this build 288 experts 68 GB disk / 68 GB resident or 39 GB streamed / 91.5% HumanEval. String Hamster absent. Do not collapse 39 streamed with 68 resident. — evidence: "README 10141 B 2026-09-05. 91.5% / 39 GB streamed / 68 GB resident. analysis/_work/captures/mustread-2026-09-05/hf-reap-readme.md" [note]
- `x-2093160779960774982#c4` (availability, demonstrated) leftover26 unused huggingface.co generic host is the same HF model already on #c3 (sh0wie REAP-288). No new integers. — evidence: "leftover26-2026-09-05.json skip huggingface.co generic host." [note]
**Numbers.** VRAM requirement: 39 GB (post); HumanEval score: 91.5 percent (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md), [dynamic-quantization](../../techniques/dynamic-quantization.md)
**Tools.** —
**Links.** https://huggingface.co
**Related items.** —
**Media.**
`raw/items/x-2093160779960774982/media/media_0.jpg` (video, carries_technique=true) — Screen recording demo of the REAP-pruned Qwen MLX 4-bit model running locally with benchmark overlay.
**Thread.** captured_partial · reported 29 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
