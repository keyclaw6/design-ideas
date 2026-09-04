# FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints

`x-2091150763418620133` · x · announcement · en · [source](https://x.com/akshay_pachaar/status/2091150763418620133) · [raw](../../../raw/items/x-2091150763418620133/)
**Author:** akshay_pachaar (@akshay_pachaar) · **Published:** — · **Captured:** 2026-09-04T06:52:39Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Roles:** tool, claim-source · **Platforms:** cli

**Summary.** Long-form thread on Berkeley FlashML FreeToken: profiles PCIe vs CPU bandwidth per machine to split MoE expert cache misses, serves OpenAI/Anthropic APIs locally, and checkpoints at agent-framework edit boundaries so prefill after history rewrites stays under 44 seconds.
**Question it answers.** How does FreeToken run large MoE models on consumer GPUs and speed agent prefill?

**Claims.**
- `x-2091150763418620133#c1` (benchmark, stated) FreeToken serves Qwen3.6-35B at 39.3 tokens per second on an 8GB GPU by exploiting MoE sparsity. — evidence: "Qwen3.6-35B on an 8GB GPU at 39.3 tokens/s" [post]
- `x-2091150763418620133#c2` (capability, stated) The engine profiles PCIe and CPU bandwidth once per machine and splits each step's expert misses proportionally between GPU copy and CPU compute. — evidence: "FreeToken measures both bandwidths on your machine and splits each step's misses between the two paths in proportion." [post]
- `x-2091150763418620133#c3` (benchmark, stated) Agent-oriented checkpoints at framework edit boundaries keep slowest first token under 44 seconds versus 232 for llama.cpp. — evidence: "its slowest first token stays under 44 seconds, while llama.cpp peaks at 232 and KTransformers at 946." [post]
**Numbers.** Qwen3.6-35B throughput on 8GB GPU: 39.3 tokens/s (post); FreeToken slowest first token: 44 seconds (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md), [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** [freetoken](../../tools/freetoken.md)
**Links.** repo (https://github.com/FlashML-org/FreeToken), paper (https://arxiv.org/pdf/2608.16157)
**Related items.** [x-2087240056037908509](../x-2087240056037908509/card.md), [x-2087562269807030754](../x-2087562269807030754/card.md)
**Media.**
`media/media_0.jpg` (video, carries_technique=false) — Screen recording or animated explainer accompanying the FreeToken throughput and MoE expert-routing narrative in the thread.
**Thread.** captured_partial · reported 72 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2087240056037908509](../x-2087240056037908509/card.md), [x-2087562269807030754](../x-2087562269807030754/card.md)
