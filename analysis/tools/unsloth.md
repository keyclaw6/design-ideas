# Unsloth

**Slug:** `unsloth` · **Kind:** product · **URL:** https://x.com/UnslothAI/status/2088281537427235320 · **Canonical item:** [x-2088281537427235320](../items/x-2088281537427235320/card.md)
**Subjects:** [local-inference-models](../subjects/local-inference-models/brief.md)
**Referenced by (2):**
- [Unsloth Qwen3.8-27B Dynamic GGUF runs locally on about 17GB RAM](../items/x-2088281537427235320/card.md) — tool, reference — local-inference-models
- [Unsloth Dynamic V3 Qwen3.8-27B GGUFs — 10% accuracy gain, 8GB 1-bit path](../items/x-2090103470015828184/card.md) — tool, reference — local-inference-models

<!-- NOTES:START -->

**2026-09-04 capture — HF `unsloth/Qwen3.8-27B-GGUF`.**
Card YAML: **apache-2.0**, `base_model: Qwen/Qwen3.8-27B`. Tree (HF API `…/tree/main`): 30 `.gguf` siblings including BF16 split + MTP. File sizes this pass (bytes):

- `Qwen3.8-27B-Q4_0.gguf` **16,056,478,688** (~14.95 GiB) — tweet “~17GB RAM” is a runtime envelope, not this file size
- `Qwen3.8-27B-UD-IQ1_S.gguf` **6,192,222,208** (~5.77 GiB) — tweet “8GB 1-bit path” is also RAM, not this file
- `Qwen3.8-27B-UD-IQ1_M.gguf` 6,729,166,848
- `Qwen3.8-27B-Q8_0.gguf` 29,047,086,048
- BF16 split: 49,986,159,616 + 4,671,576,000

README uses ranking language (“>10% … better accuracy”). Quote that as a provider claim; do not restated it as a finding. No local load here.

<!-- NOTES:END -->
