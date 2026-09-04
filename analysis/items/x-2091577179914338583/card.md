# CozyClay open-source previs before pricey AI video generation

`x-2091577179914338583` · x · repo · en · [source](https://x.com/Yun_HDY/status/2091577179914338583) · [raw](../../../raw/items/x-2091577179914338583/)
**Author:** Yun (@Yun_HDY) · **Published:** — · **Captured:** 2026-09-04T06:49:33Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [blockout-to-video-flythrough](../../subjects/blockout-to-video-flythrough/brief.md) · **Also:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Roles:** tool, technique · **Platforms:** browser

**Summary.** Yun_HDY describes paying $17 per 30s AI video miss and open-sourcing CozyClay (NomaDamas/CozyClay) to block out scenes before sending them to video models when prompts cannot hold full character heads.
**Question it answers.** How does CozyClay previs reduce wasted spend on AI video generation?

**Claims.**
- `x-2091577179914338583#c1` (pricing, stated) Author pays about $17 per 30-second AI video generation and must redo on a miss. — evidence: "ok we are paying $17 for 30s... and then one miss and you pay it again" [post]
- `x-2091577179914338583#c2` (capability, stated) CozyClay is an open-source previs tool to build the scene before turning it into video. — evidence: "so i make the scene first then turn it into video

i made a previs tool
come look, opensource
https://github.com/NomaDamas/CozyClay" [post]
- `x-2091577179914338583#c3` (result, demonstrated) CozyClay mcp verify (v1.7.0, no editor) lists 25 tools, checks 420 frame_shot combinations, and render_prompt (seedance_2 video) carries wide-shot / 24mm / both subjects. README 24-tool count is stale. — evidence: "npm run verify exit 0; listTools 25 including load_motion; render_prompt mode=video model=seedance_2; .cclayproject save/open round-trip." [note]
**Numbers.** AI video generation cost: 17 USD per 30s (post)
**Recipe.** —
**Techniques.** —
**Tools.** [cozyclay](../../tools/cozyclay.md)
**Links.** repo (https://github.com/NomaDamas/CozyClay), product (https://github.com/NomaDamas/CozyClay), https://github.com/NomaDamas/CozyClay
**Related items.** —
**Media.** —
**Thread.** captured_partial · reported 17 · captured 1 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
