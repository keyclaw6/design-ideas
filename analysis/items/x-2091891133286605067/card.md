# Custom PCB autorouter finishes keyboard board in one minute on two layers

`x-2091891133286605067` · x · demo-image · en · [source](https://x.com/paulcjh/status/2091891133286605067) · [raw](../../../raw/items/x-2091891133286605067/)
**Author:** Paul Hetherington (@paulcjh) · **Published:** — · **Captured:** 2026-09-04T06:49:34Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [ai-cad-hardware](../../subjects/ai-cad-hardware/brief.md) · **Also:** — · **Roles:** technique, claim-source · **Platforms:** kicad

**Summary.** Paul Hetherington reports his custom PCB autorouter completes a keyboard board in about one minute on two layers versus four, beating Freerouting after twenty-five minutes and matching DeepPCB airwire benchmarks with half the vias.
**Question it answers.** How fast can a custom autorouter finish a two-layer keyboard PCB compared to Freerouting?

**Claims.**
- `x-2091891133286605067#c1` (benchmark, stated) The autorouter completes the board in around one minute on two layers instead of four. — evidence: "This board completes in around 1 min, and manages to implement the required routing on just 2 layers instead of 4." [post]
- `x-2091891133286605067#c2` (benchmark, stated) Freerouting could not complete the same board after twenty-five minutes of routing. — evidence: "Freerouting was unable to complete the board after 25mins" [post]
- `x-2091891133286605067#c3` (availability, demonstrated) freerouting/freerouting GPL-3.0 **1,940★**; homepage https://www.freerouting.app. Docs freerouting.org **29,006 B**: PCB router via Specctra/Electra DSN; KiCad / Eagle / LayoutEditor; Alfons Wirtz 2004–2008, GPL 2014. deeppcb.ai **137,606 B** (InstaDeep): learned RL router; public benches STM32 100% / **18m 8s** vs ~8 hrs hand; RF mixed-signal **2m 6s** vs 2–3 hrs; critical nets stay human. Tweet 1 min / 2-layer keyboard vs Freerouting 25 min stays tweet-only — not a named board on DeepPCB’s public table. — evidence: "GET api.github.com/repos/freerouting/freerouting 1940 stars GPL-3.0. deeppcb.ai 137606 B. leftover7-2026-09-05.json" [note]
**Numbers.** autorouter completion time: 1 minute (post); Freerouting attempt duration: 25 minutes (post); routing layers used: 2 layers (post); Freerouting stars: 1940  (note)
**Recipe.** —
**Techniques.** [pcb-autorouting](../../techniques/pcb-autorouting.md)
**Tools.** [freerouting](../../tools/freerouting.md), [deeppcb](../../tools/deeppcb.md)
**Links.** repo (https://github.com/freerouting/freerouting), https://www.freerouting.org/, https://www.deeppcb.ai/
**Related items.** —
**Media.** —
**Thread.** captured_partial · reported 27 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2095193896687177873](../x-2095193896687177873/card.md)
