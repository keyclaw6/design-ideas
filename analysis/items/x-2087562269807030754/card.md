# Edge8-35B sparse MoE running on-device on an iPhone

`x-2087562269807030754` · x · announcement · en · [source](https://x.com/SamuelZengML/status/2087562269807030754) · [raw](../../../raw/items/x-2087562269807030754/)
**Author:** SamuelZengML (@SamuelZengML) · **Published:** — · **Captured:** 2026-09-04T07:07:44Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** claim-source, example · **Platforms:** other

**Summary.** Announcement of Edge8-35B, a 35B ultra-sparse MoE with dynamic expert planner and SSD-streaming runtime, demoed on one iPhone at 44 tok/s and ~1.06 GB peak memory; model and paper promised open source.
**Question it answers.** What on-device performance has Edge8-35B claimed for a 35B-class model?

**Claims.**
- `x-2087562269807030754#c1` (benchmark, stated) Demo reports 44 tokens per second at about 1.06 GB peak memory on one iPhone without cloud. — evidence: "In this demo: 44 tok/s, ~1.06 GB peak memory." [post]
- `x-2087562269807030754#c2` (capability, stated) The stack pairs a jointly trained dynamic expert planner with an SSD-streaming inference engine. — evidence: "We trained Edge8-35B, an ultra-sparse MoE with a jointly trained dynamic expert planner, and built an SSD-streaming inference engine around it." [post]
**Numbers.** throughput: 44 tok/s (post); peak memory: 1.06 GB (post); parameters: 35 B (post)
**Recipe.** —
**Techniques.** [moe-expert-offload](../../techniques/moe-expert-offload.md)
**Tools.** [edge8-35b](../../tools/edge8-35b.md)
**Links.** —
**Related items.** [x-2087962842985058365](../x-2087962842985058365/card.md), [x-2088281537427235320](../x-2088281537427235320/card.md), [x-2087240056037908509](../x-2087240056037908509/card.md)
**Media.**
`raw/items/x-2087562269807030754/media/media_0.jpg` (video, carries_technique=false) — iPhone chat UI for Edge8-35B showing on-device MoE streaming prompts like palindrome-check and attention explainers.
**Thread.** captured_partial · reported 32 · captured 3 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
