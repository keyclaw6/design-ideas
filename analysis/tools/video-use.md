# Video Use

**Slug:** `video-use` · **Kind:** repo · **URL:** https://github.com/browser-use/video-use · **Canonical item:** [x-2092980272819999227](../items/x-2092980272819999227/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [ai-video-generation](../subjects/ai-video-generation/brief.md)
**Referenced by (2):**
- [video-use plus Codex for agent-driven video editing](../items/x-2092980272819999227/card.md) — tool, example — ai-video-generation
- [Video Use: open-source Claude Code agent video editor (browser-use)](../items/x-2094061655990702150/card.md) — tool — ai-video-generation

<!-- NOTES:START -->
**2026-09-04 capture — README local-folder path.** `https://raw.githubusercontent.com/browser-use/video-use/main/README.md` (5,645 B). OSS flow: drop raw footage in a folder, chat with Claude Code / Codex / Hermes, get `final.mp4`. Outputs live in `<videos_dir>/edit/`. Manual install is clone + symlink into the agent skills dir + `uv sync` + ffmpeg; ElevenLabs key is for Scribe transcription, not a hosted editor account. Optional: Browser Use Cloud / Box. The LLM reads a packed transcript (`takes_packed.md` ~12KB) plus on-demand `timeline_view` PNGs — it does not watch frames. Self-eval loop max 3 re-renders. This is first-party README, not a local edit run on this host.

**2026-09-04 capture — local `helpers/render.py` on a lavfi EDL.** Clone `browser-use/video-use`. Source: ffmpeg `testsrc`+`sine` 640×360 / 24 fps / 2.000 s / 35,910 B. EDL two ranges on one take (`0.00–0.80`, `1.00–1.80`). `python helpers/render.py edl.json -o final.mp4 --draft --no-subtitles --no-loudnorm` exit 0. Output **132,217** B, **1.666** s, **1280×720** / 24 fps / libx264 + aac (draft upscale). Intermediate `base_draft.mp4` 132,209 B. This is the helper pipeline only — no Claude Code session, no ElevenLabs Scribe, no filler-cut or captions. Receipt: `analysis/_work/captures/video-use-edit/`.
<!-- NOTES:END -->
