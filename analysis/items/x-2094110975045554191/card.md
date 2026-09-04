# fini multi-agent blast-radius checklist: one login, six bots, 24k actions

`x-2094110975045554191` · x · thread · en · [source](https://x.com/0xfini/status/2094110975045554191) · [raw](../../../raw/items/x-2094110975045554191/)
**Author:** fini (@0xfini) · **Published:** — · **Captured:** 2026-09-04T06:50:05Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** technique, claim-source · **Platforms:** browser, mcp

**Summary.** fini warns six named sidebar bots can share one browser profile: 23,999 actions in twenty minutes across mail, drive, CRM, and billing with no spend cap, persistent session, and audit off by default.
**Question it answers.** What security checks should you run before adding another agent to a shared browser profile?

**Claims.**
- `x-2094110975045554191#c1` (result, stated) Six sidebar bots operated on one browser profile logging 23,999 actions in twenty minutes at 38 actions per second peak. — evidence: "23,999 actions. Peak rate 38 per second. Six bots on the board." [post]
- `x-2094110975045554191#c2` (counter-claim, stated) Deleting a bot did not kill its underlying session, so separate bots are not a security boundary. — evidence: "Separate bots are not a security boundary. That is not my opinion, it is in the docs nobody opens." [post]
**Numbers.** actions in 20 minutes: 23999 actions (post); peak action rate: 38 per second (post)
**Recipe.** —
**Techniques.** [session-hardening](../../techniques/session-hardening.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** —
**Links.** —
**Related items.** —
**Media.**
`raw/items/x-2094110975045554191/media/media_0.mp4` (video, carries_technique=true) — Screen recording of a multi-bot dashboard showing shared login, access ledger counts, and blast-radius metrics climbing.
**Thread.** captured_partial · reported 18 · captured 1 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
