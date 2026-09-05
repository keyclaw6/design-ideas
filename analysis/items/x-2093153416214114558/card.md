# OmniParser: screenshot UI parsing so general LLMs can click screens

`x-2093153416214114558` · x · repo · en · [source](https://x.com/simplifyinAI/status/2093153416214114558) · [raw](../../../raw/items/x-2093153416214114558/)
**Author:** simplifyinAI (@simplifyinAI) · **Published:** — · **Captured:** 2026-09-04T06:52:58Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** — · **Roles:** tool, technique · **Platforms:** browser, mcp

**Summary.** OmniParser parses screenshots into labeled UI elements so general-purpose models (GPT-4o, DeepSeek R1, Qwen2.5VL) can click accurately instead of guessing coordinates. Paired with OmniTool it controls a Windows 11 VM; Hugging Face Spaces hosts a live demo.
**Question it answers.** How can a general LLM click UI elements without a native computer-use model?

**Claims.**
- `x-2093153416214114558#c1` (capability, stated) OmniParser converts screenshots into structured, labeled UI elements for click targeting. — evidence: "It parses a screenshot into structured, labeled UI elements, buttons, icons, text fields" [post]
- `x-2093153416214114558#c2` (capability, stated) OmniTool with OmniParser can control an actual Windows 11 VM using OpenAI, DeepSeek, Qwen, or Claude Computer Use. — evidence: "Paired with OmniTool, it can control an actual Windows 11 VM, works with OpenAI, DeepSeek, Qwen, or Anthropic's Claude Computer Use." [post]
- `x-2093153416214114558#c3` (capability, demonstrated) t.co/EVyRdK4iJv → github.com/microsoft/OmniParser. API: CC-BY-4.0 **25,370★** / 2,231 forks (README badge says MIT — do not collapse with the API SPDX). README: screen-parse for GPT-4V grounding; OmniTool Windows 11 VM + OpenAI 4o/o1/o3-mini, DeepSeek R1, Qwen 2.5VL, Anthropic Computer Use; paper arXiv 2408.00203; V2 Screen Spot Pro **39.5%** claimed; Hugging Face microsoft/OmniParser **171,529 B**. icon_detect_v3 MIT YOLOv9; earlier Ultralytics detectors AGPL; captions MIT. — evidence: "GET api.github.com/repos/microsoft/OmniParser 25370 stars CC-BY-4.0. README 5750 B. leftover6-2026-09-05/omniparser-readme.md" [note]
**Numbers.** GitHub stars: 25370  (note); Screen Spot Pro claimed: 39.5 percent (note)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** repo (https://github.com/microsoft/OmniParser), paper (https://arxiv.org/abs/2408.00203), https://huggingface.co/microsoft/OmniParser
**Related items.** —
**Media.**
`raw/items/x-2093153416214114558/media/media_0.jpg` (video, carries_technique=false) — Screen recording demo of OmniParser labeling UI elements on a Windows desktop for agent clicking.
**Thread.** captured_partial · reported 7 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
