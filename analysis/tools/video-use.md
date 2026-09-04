# Video Use

**Slug:** `video-use` · **Kind:** repo · **URL:** https://github.com/browser-use/video-use · **Canonical item:** [x-2092980272819999227](../items/x-2092980272819999227/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [ai-video-generation](../subjects/ai-video-generation/brief.md)
**Referenced by (2):**
- [video-use plus Codex for agent-driven video editing](../items/x-2092980272819999227/card.md) — tool, example — ai-video-generation
- [Video Use: open-source Claude Code agent video editor (browser-use)](../items/x-2094061655990702150/card.md) — tool — ai-video-generation

<!-- NOTES:START -->
**2026-09-04 capture — README local-folder path.** `https://raw.githubusercontent.com/browser-use/video-use/main/README.md` (5,645 B). OSS flow: drop raw footage in a folder, chat with Claude Code / Codex / Hermes, get `final.mp4`. Outputs live in `<videos_dir>/edit/`. Manual install is clone + symlink into the agent skills dir + `uv sync` + ffmpeg; ElevenLabs key is for Scribe transcription, not a hosted editor account. Optional: Browser Use Cloud / Box. The LLM reads a packed transcript (`takes_packed.md` ~12KB) plus on-demand `timeline_view` PNGs — it does not watch frames. Self-eval loop max 3 re-renders. This is first-party README, not a local edit run on this host.
<!-- NOTES:END -->
