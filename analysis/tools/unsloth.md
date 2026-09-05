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

**2026-09-05 capture — docs page.** `https://unsloth.ai/docs/basics/dynamic-3.0-ggufs` GET 200 / **1,390,164 B**. First-party: Qwen3.8-27B Dynamic v3.0 quants deliver **>10% top-1% better accuracy** at the same size vs every other provider (author claim). Separate sentence: Unsloth GGUFs perform better despite being **~8GB smaller**. Do not collapse >10% with ~8GB. No GPU profile. Receipt `analysis/_work/captures/leftover-2026-09-05.json`.

Neighbor: `https://developer.amd.com` GET 200 / **108,551 B**. Complimentary cloud credits; free to join. **Token Factory** / daily strings absent. Receipt `analysis/_work/captures/leftover2-2026-09-05.json`.

Neighbor (parked; no hamster.md): 2026-09-05 HF `sh0wie/Qwen3.8-Flash-Next-REAP-288-MLX-4bit` (not a HamsterResearch org). README table: Base Q4 **512** experts **98 GB** disk / **97 GB** resident / **93.9%** HumanEval; this build **288** experts **68 GB** disk / **68 GB** resident or **39 GB streamed** / **91.5%** HumanEval. String Hamster absent. Do not collapse 39 streamed with 68 resident. Receipt `analysis/_work/captures/mustread-2026-09-05/hf-reap-readme.md`.
<!-- NOTES:END -->
