# Html Video

**Slug:** `html-video` · **Kind:** repo · **URL:** https://github.com/nexu-io/html-video · **Canonical item:** [github-nexu-io-html-video](../items/github-nexu-io-html-video/card.md)
**Subjects:** [code-motion-graphics](../subjects/code-motion-graphics/brief.md), [design-agent-skills](../subjects/design-agent-skills/brief.md)
**Referenced by (1):**
- [nexu-io/html-video: agent-driven HTML/CSS to local MP4](../items/github-nexu-io-html-video/card.md) — tool, technique — code-motion-graphics

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/nexu-io/html-video

**Apache-2.0**. Default engine **Hyperframes**: headless Chromium records HTML/CSS/GSAP, ffmpeg libx264 → local MP4. README lists a long agent set (Open Design, Claude Code, Cursor, Codex, Gemini, Grok, …) — “14 agents” is the card count; README is a longer name list. README still says **21 templates**; tree now has **23** `template.html-video.yaml`: frame-bold-poster, frame-bold-signal, frame-build-minimal, frame-creative-voltage, frame-data-chart-nyt, frame-data-rollup, frame-decision-tree, frame-electric-studio, frame-glitch-title, frame-kinetic-type, frame-light-leak-cinema, frame-liquid-bg-hero, frame-logo-outro, frame-nyt-graph, frame-pentagram-stat, frame-play-mode, frame-product-promo, frame-product-promo-30s, frame-swiss-grid, frame-takram-organic, frame-vignelli, frame-warm-grain, vfx-text-cursor. Remotion adapter package exists; Motion Canvas / Manim adapters are **roadmap, not built**.

**2026-09-04 capture — local MP4.** `node packages/cli/dist/bin.js doctor`: overall ok; ffmpeg 6.1.1; Hyperframes 0.4.x + Remotion 4.x adapters; **23** templates discovered. `node packages/cli/dist/smoke.js` after `npx playwright install chromium`: preview HTML then Hyperframes export of `frame-data-chart-nyt`. First smoke `/tmp/html-video-smoke-ulllAR/.../output-2026-09-04_20-40-56.mp4` **226,463** bytes; ffprobe **4.77 s**, **1920×1080**, **60 fps**, h264 High / `libx264` / yuv420p. Smoke also wrote a 3-node content-graph (intro/middle/outro) without a second MP4.

**2026-09-04 re-run — file now in this bank.** Second smoke at 22:12 wrote `/tmp/html-video-smoke-yIG8mp/.html-video/projects/proj_ec828209-439/output-2026-09-04_22-12-31.mp4`. Copied to `analysis/_work/captures/html-video-smoke/output-2026-09-04_22-12-31.mp4`. ffprobe: **241,922** bytes, **4.75 s**, **1920×1080**, **60/1** fps, h264 / yuv420p. Same template (`frame-data-chart-nyt`); do not collapse the two byte counts.

**Neighbor — HeyGen compositions.** `heygen-com/hyperframes-launches` is the public source behind the JakeFromHeyGen launch clip (`x-2093129469926215800`), not this nexu-io monorepo. Counts and LFS note live on [hyperframes](hyperframes.md). Official renderer CLI is `heygen-com/hyperframes`.
<!-- NOTES:END -->
