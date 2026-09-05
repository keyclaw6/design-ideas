# Unsloth Qwen3.8-27B Dynamic GGUF runs locally on about 17GB RAM

`x-2088281537427235320` · x · announcement · en · [source](https://x.com/UnslothAI/status/2088281537427235320) · [raw](../../../raw/items/x-2088281537427235320/)
**Author:** Unsloth AI (@UnslothAI) · **Published:** — · **Captured:** 2026-09-04T06:49:29Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** cli, other

**Summary.** Unsloth announces Qwen3.8-27B local inference via Dynamic GGUF quantizations targeting about 17GB RAM, plus NVFP4 quants on NVIDIA hardware. Hugging Face hosts weights; docs cover hybrid thinking and non-thinking sampling presets.
**Question it answers.** What RAM budget does Unsloth cite for running Qwen3.8-27B locally?

**Claims.**
- `x-2088281537427235320#c1` (availability, stated) Dynamic GGUF path targets about 17GB RAM for Qwen3.8-27B local runs. — evidence: "Run on 17GB RAM via Unsloth Dynamic GGUFs." [post]
- `x-2088281537427235320#c2` (availability, stated) Unsloth also uploaded NVFP4 quantizations for NVIDIA boxes. — evidence: "We also uploaded NVFP4 quants." [post]
- `x-2088281537427235320#c3` (counter-claim, demonstrated) HF unsloth/Qwen3.8-27B-GGUF tree (2026-09-04): apache-2.0; 30 .gguf siblings. Q4_0 is 16,056,478,688 B (~14.95 GiB) — tweet ~17GB RAM is a runtime envelope, not this file. UD-IQ1_S is 6,192,222,208 B (~5.77 GiB), not an 8GB file. No local load. — evidence: "analysis/tools/unsloth.md NOTES HF tree sizes 2026-09-04." [note]
**Numbers.** RAM target for Dynamic GGUF: 17 GB (post); model parameters: 27 B (post)
**Recipe.** —
**Techniques.** [dynamic-quantization](../../techniques/dynamic-quantization.md)
**Tools.** [unsloth](../../tools/unsloth.md), [qwen3-8-27b](../../tools/qwen3-8-27b.md)
**Links.** repo (https://huggingface.co/unsloth/Qwen3.8-27B-GGUF), https://unsloth.ai/docs/models/qwen3.8
**Related items.** [x-2087562269807030754](../x-2087562269807030754/card.md), [x-2087962842985058365](../x-2087962842985058365/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
**Media.**
`raw/items/x-2088281537427235320/media/media_0.jpg` (image, carries_technique=true) — Infographic lists Qwen3.8-27B specs, RAM tiers by quant bit-width, recommended thinking vs non-thinking sampling presets, and benchmark tables versus other 27B-class models.
**Thread.** captured_partial · reported 204 · captured 2 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
