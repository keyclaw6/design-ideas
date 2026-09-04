# Freetoken

**Slug:** `freetoken` · **Kind:** product · **URL:** https://x.com/akshay_pachaar/status/2091150763418620133 · **Canonical item:** [x-2091150763418620133](../items/x-2091150763418620133/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [local-inference-models](../subjects/local-inference-models/brief.md)
**Referenced by (1):**
- [FreeToken MoE inference engine: PCIe/CPU split and agent prefill checkpoints](../items/x-2091150763418620133/card.md) — tool, claim-source — local-inference-models

<!-- NOTES:START -->
Fetched 2026-09-04 README + arXiv:2608.16157

Repo: https://github.com/FlashML-org/FreeToken · **Apache-2.0**. Paper: Yang et al., “Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution.” Desktop app at flashml.ai (Windows/Linux). CLI: `uv pip install "freetoken[accel]"`. Claims in README/abstract: 20+ MoE models; 35B on 8GB laptop GPU; 284B on a gaming desktop; 753B GLM-5.2 on one workstation GPU; q* CPU–GPU policy; semantic anchor checkpoints for agent context edits; MXFP4/NVFP4/FP8/BF16.

Paper body (Yang et al., arXiv:2608.16157) **does** carry the tweet-scale numbers: RTX 4060 8 GB laptop serves a 35B at **39.3 tok/s** (paper: above Codex production median 33 tok/s). Worst-case TTFT **<44 s** across workloads vs baselines **>150 s** in at least one setting. RTX 5090: 77–83 tok/s on Qwen3.6-35B-A3B, 22–25 tok/s on DeepSeek-V4-Flash, 1.5–2.3× vs named edge engines; decode stays within 12% of single-turn under agentic load. Five consumer systems: 1.3–2.1× decode. GLM-5.2 753B on one RTX PRO 6000 at 2× llama.cpp. Authors: Berkeley / UT / others (Stoica, Zaharia, Han). No profile run on this host.

**2026-09-04 capture — local clone** `/tmp/captures2/freetoken` (`FlashML-org/FreeToken`). Apache-2.0. **499** `.py` files. `pyproject.toml` requires `torch>=2.11,<2.12`, `requires-python >=3.10`, Linux+CUDA (PyPI torch index `pytorch-cu130`). FastAPI OpenAI/Anthropic APIs. README now says **290B+** on a gaming PC (older NOTES said 284B). Still no `profile` run on this host.
<!-- NOTES:END -->
