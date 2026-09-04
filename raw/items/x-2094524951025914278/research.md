## What they are actually doing

Olav (founder/CEO of Blume, Toronto) published an X article on how they built [blume.codes](https://blume.codes) — a macOS sidecar for coding agents (Cursor / Claude Code / Codex). Site copy at capture: “Tired of steering your coding agents?”; Download DMG, Apple Silicon v1.0.71; local conversation history; rules/skills/hooks. Blume started in 2025 as a landing-page builder, then pivoted to an “control plane for agentic coding.” Olav: 12 years design-engineering; Modulize (2020); first designer/technical hire at Wordware (Product Hunt Product of the Year 2024).

Design philosophy in the article: **attention is zero-sum** — one red button stands out; all red none do. Goal is not merely to convince but to amaze. He asks readers to scroll the live site and spot four effects before reading on. Explicitly does not want 1:1 clones.

**1. Parallax hero.** First landscape felt flat. Built with **Codex** (code + image gen in one harness; Claude Code + fal.ai is the fallback). Vibe prompt: “epic landscape filled with flowers, with a Makoto Shinkai modern aesthetic,” plus flower-logo refs. Minimum 3 layers; they used **7**. Codex prompt (article markdown block): generate each layer with the reference in every request; real alpha (no magenta/checkerboard); closer layers parallax faster, opposite scroll; viewport-tall hero; bottom 20% gradient; then check gaps, speed, unseen layers, halos; upscale approved layers with the reference again.

**2. Interactive product demo.** Screenshots go stale. Landing page and Electron app share a **Turborepo** UI package; the site embed is a live mock-data instance of the app. Codex ran a week-long `/goal` refactor to get there (also unlocked browser-based testing).

**3. Sprouting vine.** Scroll-drawn vector path; flower crowns from a custom [Dicebear](https://www.dicebear.com/) style, seeded by the current date so they change daily. “Site should work like a song.”

**4. Flower theme.** Six flowers in the app; same on the page, including regenerated graphics per theme. Hidden/easter-egg; can also be set from the in-page app demo settings.

## Open questions

- Whether the 13 login-walled replies include a public repo or extra prompt paste.
- Exact layer count vs the eight cards in `article-layers.jpg`.
- How much of the “wow” is original illustration vs GPT-image layers on a Shinkai brief.
