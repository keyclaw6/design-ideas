# Howaboua Pi realtime voice changelog and extension announcement API

`x-2087714580491370655` · x · thread · en · [source](https://x.com/Howaboua/status/2087714580491370655) · [raw](../../../raw/items/x-2087714580491370655/)
**Author:** Howaboua (@Howaboua) · **Published:** — · **Captured:** 2026-09-04T07:32:03Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** tool, technique · **Platforms:** pi

**Summary.** Sixteen-hour voice-driven Pi release adds reportRealtimeVoicePrompt for extensions, togglable spoken acknowledgements and reasoning summaries, guided audio setup, and npm packages pi-codex-conversion or standalone pi-gippity-control.
**Question it answers.** How do Pi extensions announce events to the realtime voice assistant without canned lines?

**Claims.**
- `x-2087714580491370655#c1` (capability, stated) Pi extensions can send natural-language instructions to the active realtime voice assistant via reportRealtimeVoicePrompt with stable ids and active flags. — evidence: "Pi extensions can now send prompts to the active realtime voice assistant. These are instructions, not canned lines" [post]
- `x-2087714580491370655#c2` (recipe, stated) Install pi-codex-conversion or standalone pi-gippity-control but not both. — evidence: "Codex Conversion already contains GipPity. Pick the full Codex package or standalone GipPity. Do not install both." [post]
**Numbers.** —
**Recipe.** —
**Techniques.** [session-hardening](../../techniques/session-hardening.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** [pi-codex-conversion](../../tools/pi-codex-conversion.md), [pi-gippity-control](../../tools/pi-gippity-control.md)
**Links.** repo (https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-codex-conversion), https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-gippity-control, https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-shepherdr
**Related items.** [x-2087232392209531166](../x-2087232392209531166/card.md), [web-blume-codes](../web-blume-codes/card.md)
**Media.**
`media/media_0.jpg` (image, carries_technique=true) — Screenshot of Pi Realtime Voice chat UI showing casual morning greeting exchange between user and voice assistant.
**Thread.** captured_partial · reported 10 · captured 3 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: [] · compare with: —
