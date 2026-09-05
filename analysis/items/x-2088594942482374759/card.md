# RunInfra hosts full BF16 DeepSeek V4 Flash at 278 tok/s

`x-2088594942482374759` · x · announcement · en · [source](https://x.com/runinfrai/status/2088594942482374759) · [raw](../../../raw/items/x-2088594942482374759/)
**Author:** runinfrai (@runinfrai) · **Published:** — · **Captured:** 2026-09-04T07:07:49Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [local-inference-models](../../subjects/local-inference-models/brief.md) · **Also:** — · **Roles:** tool · **Platforms:** other

**Summary.** RunInfra announces full-precision BF16 DeepSeek V4 Flash inference at about 278 tokens per second with $0.13 per million input and $0.27 per million output tokens via its API.
**Question it answers.** What cheap hosted endpoint serves full-precision DeepSeek V4 Flash for high-volume agent loops?

**Claims.**
- `x-2088594942482374759#c1` (pricing, stated) RunInfra claims the fastest full-precision V4 Flash inference at 278.3 tok/s with sub-dollar-per-million-token pricing. — evidence: "278.3 tok/s. $0.13/1M input. $0.27/1M output. full BF16" [post]
- `x-2088594942482374759#c2` (counter-claim, demonstrated) runinfra.ai/inference-api/qwen3-8-2-4t-a95b 200 / 401,869 B. Visible library lists DeepSeek V4 Flash at $0.13 / $0.01 cached / $0.27 per 1M tokens. Strings 278 / tok/s / BF16 are absent from this HTML. Tweet 278.3 tok/s stays tweet-only. — evidence: "GET 200 401869 B. 278 and BF16 absent. $0.13/$0.27 first-party." [note]
**Numbers.** throughput: 278.3 tok/s (post); input price: 0.13 USD per 1M tokens (post); output price: 0.27 USD per 1M tokens (post)
**Recipe.** —
**Techniques.** —
**Tools.** [runinfra](../../tools/runinfra.md)
**Links.** product (https://runinfra.ai/inference-api/qwen3-8-2-4t-a95b)
**Related items.** [x-2088695568474546387](../x-2088695568474546387/card.md), [x-2090103470015828184](../x-2090103470015828184/card.md), [x-2089165107364278341](../x-2089165107364278341/card.md), [github-superdesigndev-treg](../github-superdesigndev-treg/card.md)
**Media.** —
**Thread.** captured_partial · reported 72 · captured 2 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
