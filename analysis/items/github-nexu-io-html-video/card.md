# nexu-io/html-video: agent-driven HTML/CSS to local MP4

`github-nexu-io-html-video` · github · repo · en · [source](https://github.com/nexu-io/html-video) · [raw](../../../raw/items/github-nexu-io-html-video/)
**Author:** nexu-io (@—) · **Published:** — · **Captured:** 2026-09-02T17:15:19Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [code-motion-graphics](../../subjects/code-motion-graphics/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** tool, technique · **Platforms:** claude-code, cursor, remotion

**Summary.** Apache-2.0 monorepo that turns prompts, links, or repos into MP4 videos by generating per-frame HTML and rendering locally via Hyperframes (headless Chromium + ffmpeg). Ships a studio CLI, 21 templates, and optional MiniMax soundtrack; no per-render cloud fee.
**Question it answers.** How can coding agents render HTML/CSS storyboards into MP4 on a laptop without a video model?

**Claims.**
- `github-nexu-io-html-video#c1` (capability, demonstrated) Default render path is Hyperframes headless Chromium plus ffmpeg to MP4. — evidence: "default engine is Hyperframes (headless Chromium + ffmpeg)" [linked-page]
- `github-nexu-io-html-video#c2` (capability, stated) Repo documents 14 supported coding agents and 21 motion templates. — evidence: "**14 coding agents** supported (Open Design, Claude Code, Cursor, Codex, etc.)
- **21 templates** (data viz, kinetic type, cinematic frames)" [linked-page]
- `github-nexu-io-html-video#c3` (result, demonstrated) A 2026-09-04 local smoke of frame-data-chart-nyt wrote a 226,463-byte 1920×1080 60 fps libx264 MP4 lasting 4.77 seconds; doctor listed 23 templates. — evidence: "smoke.js export: output-2026-09-04_20-40-56.mp4 226463 bytes; ffprobe 4.77s 1920x1080 60fps h264 libx264; doctor templates=23 discovered" [note]
- `github-nexu-io-html-video#c4` (result, demonstrated) A second 2026-09-04 smoke of frame-data-chart-nyt is stored at analysis/_work/captures/html-video-smoke/output-2026-09-04_22-12-31.mp4: 241,922 bytes, 4.75 s, 1920×1080, 60 fps, h264 yuv420p. — evidence: "ffprobe on banked MP4: size 241922; duration 4.75; 1920x1080; r_frame_rate 60/1; codec h264; pix_fmt yuv420p" [note]
**Numbers.** smoke MP4 bytes: 226463 bytes (note); doctor template count: 23  (note); banked smoke MP4 bytes: 241922 bytes (note)
**Recipe.** —
**Techniques.** [remotion-code-video](../../techniques/remotion-code-video.md), [remotion-code-video](../../techniques/remotion-code-video.md), [remotion-code-video](../../techniques/remotion-code-video.md)
**Tools.** [html-video](../../tools/html-video.md), [hyperframes](../../tools/hyperframes.md), [ffmpeg](../../tools/ffmpeg.md)
**Links.** repo (https://github.com/nexu-io/html-video), product (https://open-design.ai/html-video), https://github.com/nexu-io/open-design
**Related items.** [github-nexu-io-open-design](../github-nexu-io-open-design/card.md), [github-nexu-io-motion-anything](../github-nexu-io-motion-anything/card.md), [web-open-design-ai](../web-open-design-ai/card.md), [web-fal-ai](../web-fal-ai/card.md), [web-animos-editor](../web-animos-editor/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: [github-nexu-io-motion-anything](../github-nexu-io-motion-anything/card.md), [web-fal-ai](../web-fal-ai/card.md)
