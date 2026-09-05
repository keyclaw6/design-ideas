# FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints

`x-2091150763418620133` · x · announcement · en · [source](https://x.com/akshay_pachaar/status/2091150763418620133) · [raw](../../../raw/items/x-2091150763418620133/)
**Author:** akshay_pachaar (@akshay_pachaar) · **Published:** — · **Captured:** 2026-09-04T06:52:39Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Roles:** tool, claim-source · **Platforms:** cli

**Summary.** Long-form thread on Berkeley FlashML FreeToken: profiles PCIe vs CPU bandwidth per machine to split MoE expert cache misses, serves OpenAI/Anthropic APIs locally, and checkpoints at agent-framework edit boundaries so prefill after history rewrites stays under 44 seconds.
**Question it answers.** How does FreeToken run large MoE models on consumer GPUs and speed agent prefill?

**Claims.**
- `x-2091150763418620133#c1` (benchmark, stated) FreeToken serves Qwen3.6-35B at 39.3 tokens per second on an 8GB GPU by exploiting MoE sparsity. — evidence: "Qwen3.6-35B on an 8GB GPU at 39.3 tokens/s" [post]
- `x-2091150763418620133#c2` (capability, stated) The engine profiles PCIe and CPU bandwidth once per machine and splits each step's expert misses proportionally between GPU copy and CPU compute. — evidence: "FreeToken measures both bandwidths on your machine and splits each step's misses between the two paths in proportion." [post]
- `x-2091150763418620133#c3` (benchmark, stated) Agent-oriented checkpoints at framework edit boundaries keep slowest first token under 44 seconds versus 232 for llama.cpp. — evidence: "its slowest first token stays under 44 seconds, while llama.cpp peaks at 232 and KTransformers at 946." [post]
- `x-2091150763418620133#c4` (capability, demonstrated) Local FreeToken clone is Apache-2.0 with 499 Python files; README now claims 290B+ on a gaming PC (older NOTES said 284B). — evidence: "Clone FlashML-org/FreeToken: 499 .py files; pyproject.toml license Apache-2.0, torch>=2.11,<2.12; README lead: Run 290B+ frontier MoE models locally on your gaming PC." [note]
- `x-2091150763418620133#c5` (benchmark, demonstrated) arXiv 2608.16157 PDF (888,695 B; pdftotext 74,232 chars) first-party: 8GB RTX 4060 laptop serves a 35B at 39.3 tok/s (vs Codex median 33 tok/s); worst-case TTFT stays below 44 s while each baseline exceeds 150 s in at least one setting. RTX 5090: 77–83 tok/s on Qwen3.6-35B-A3B and 22–25 tok/s on DeepSeek-V4-Flash (1.5–2.3× named edge engines). Abstract (42,706 B) names 20+ models / 35B laptop / 284B desktop / 753B GLM-5.2 and does not include 39.3 or 44 s. — evidence: "On an 8,GB RTX 4060 laptop, it serves a 35B model at 39.3 tok/s, exceeding the 33 tok/s median decode speed of Codex. FreeToken’s worst turn stays below 44 s in every cell. analysis/_work/captures/freetoken-arxiv-2608.16157-extract.txt" [note]
- `x-2091150763418620133#c6` (availability, demonstrated) leftover21: flashml.ai 200 / 39,649 B (www.flashml.ai) titles FreeToken — Bring Frontier to Edge. FlashML-org/FreeToken Apache-2.0 11,665★. README 4,821 B still says Run 290B+ frontier MoE locally; desktop Windows/Linux; uv pip install freetoken[accel]. CLI docs mention profile in NOTES; this host still has no GPU profile run. — evidence: "leftover21 flashml 39649 B; gh-freetoken 11665 Apache-2.0; README 4821 B." [note]
- `x-2091150763418620133#c7` (availability, demonstrated) leftover24 unused GitHub FlashML-org/FreeToken is Apache-2.0 11,666★ this pass (leftover21 was 11,665★). Do not collapse. GPU profile still not run here. — evidence: "leftover24 gh-freetoken 11666 Apache-2.0." [note]
**Numbers.** Qwen3.6-35B throughput on 8GB GPU: 39.3 tokens/s (post); FreeToken slowest first token: 44 seconds (post); FreeToken clone Python files: 499 files (note); paper 4060 laptop 35B decode: 39.3 tok/s (note); paper worst-case TTFT: 44 seconds (note)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md), [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** [freetoken](../../tools/freetoken.md)
**Links.** repo (https://github.com/FlashML-org/FreeToken), paper (https://arxiv.org/abs/2608.16157), https://arxiv.org/pdf/2608.16157, https://www.flashml.ai/, https://github.com/FlashML-org/FreeToken
**Related items.** [x-2087240056037908509](../x-2087240056037908509/card.md), [x-2087562269807030754](../x-2087562269807030754/card.md), [x-2090930324817498246](../x-2090930324817498246/card.md)
**Media.**
`raw/items/x-2091150763418620133/media/media_0.jpg` (video, carries_technique=false) — Screen recording or animated explainer accompanying the FreeToken throughput and MoE expert-routing narrative in the thread.
**Thread.** captured_partial · reported 72 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2087240056037908509](../x-2087240056037908509/card.md), [x-2087562269807030754](../x-2087562269807030754/card.md)
