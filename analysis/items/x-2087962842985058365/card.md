# Bonsai-1.7B hits 90 tok/s CPU decode on Android without NPU or GPU

`x-2087962842985058365` · x · announcement · en · [source](https://x.com/GlennSonna/status/2087962842985058365) · [raw](../../../raw/items/x-2087962842985058365/)
**Author:** Glenn Sonna (@GlennSonna) · **Published:** — · **Captured:** 2026-09-04T06:49:27Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** claim-source, technique · **Platforms:** other

**Summary.** Glenn Sonna reports PrismML Bonsai-1.7B decode rising from 64 to 90 tokens per second on the same Android device using CPU only—no NPU or GPU—and about 3× faster than the llama.cpp reference on that hardware.
**Question it answers.** What on-device decode speed was reported for Bonsai-1.7B on CPU-only Android?

**Claims.**
- `x-2087962842985058365#c1` (benchmark, stated) Bonsai-1.7B reached 90 tok/s decode on the same Android device, up from 64 tok/s, CPU only. — evidence: "64 → 90 tok/s decode on the same Android Device.
CPU only, no NPU, no GPU." [post]
- `x-2087962842985058365#c2` (benchmark, stated) The reported speed is almost 3× faster than the llama.cpp reference on that setup. — evidence: "Almost 3x faster than the llama.cpp reference." [post]
- `x-2087962842985058365#c3` (availability, demonstrated) First-party Bonsai-1.7B weights are on Hugging Face: prism-ml/Bonsai-1.7B-gguf Apache-2.0, 91 likes / 66,378 downloads; unpacked base prism-ml/Bonsai-1.7B-unpacked. README: GGUF Q1_0 0.24 GB (14.2× vs FP16 3.44 GB); 13.9× smaller than FP16; throughput table RTX 4090 674 vs FP16 224 tok/s (3.0×) and M4 Pro 250 vs 65 (3.8×). Android is named as a platform. Tweet 64→90 tok/s CPU-only and “almost 3× llama.cpp” are not on the README or prismml.com (96,797 B; homepage hero is Bonsai 27B 5.9 GB ternary / 3.9 GB 1-bit). Do not collapse those tweet integers with the 4090/M4 table. — evidence: "HF prism-ml/Bonsai-1.7B-gguf apache-2.0 91 likes 66378 dl; README 0.24 GB 674/224 4090 250/65 M4 Pro; prismml.com 96797 B. leftover10-bonsai-detail-2026-09-05.json." [note]
**Numbers.** decode throughput: 90 tok/s (post); prior decode throughput: 64 tok/s (post)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** repo (https://github.com/PrismML-Eng/Bonsai-demo), product (https://huggingface.co/prism-ml/Bonsai-1.7B-gguf)
**Related items.** [x-2087562269807030754](../x-2087562269807030754/card.md), [x-2088281537427235320](../x-2088281537427235320/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
**Media.** —
**Thread.** captured_partial · reported 15 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
