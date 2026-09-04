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
**Numbers.** decode throughput: 90 tok/s (post); prior decode throughput: 64 tok/s (post)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** —
**Related items.** [x-2087562269807030754](../x-2087562269807030754/card.md), [x-2088281537427235320](../x-2088281537427235320/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
**Media.** —
**Thread.** captured_partial · reported 15 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
