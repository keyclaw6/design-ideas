# Freetoken

**Slug:** `freetoken` · **Kind:** product · **URL:** https://x.com/akshay_pachaar/status/2091150763418620133 · **Canonical item:** [x-2091150763418620133](../items/x-2091150763418620133/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [local-inference-models](../subjects/local-inference-models/brief.md)
**Referenced by (1):**
- [FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints](../items/x-2091150763418620133/card.md) — tool, claim-source — local-inference-models

<!-- NOTES:START -->

Fetched 2026-09-04 README + arXiv:2608.16157

Repo: https://github.com/FlashML-org/FreeToken · **Apache-2.0**. Paper: Yang et al., “Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution.” Desktop app at flashml.ai (Windows/Linux). CLI: `uv pip install "freetoken[accel]"`. Claims in README/abstract: 20+ MoE models; 35B on 8GB laptop GPU; 284B on a gaming desktop; 753B GLM-5.2 on one workstation GPU; q* CPU–GPU policy; semantic anchor checkpoints for agent context edits; MXFP4/NVFP4/FP8/BF16. Tweet numbers (39.3 tok/s, 44s first token vs llama.cpp 232s) are **not** in the README — still tweet-only. No profile run on this host.

<!-- NOTES:END -->
