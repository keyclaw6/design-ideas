# Research

## What it is

wuyoscar/GPT-Image2-Skill (~5k stars, MIT): curated GPT Image 2 prompt gallery plus agent skill and CLI wrapping OpenAI image generation and multi-reference edits.

## How it works

- CLI `gpt-image -p "prompt"`; sizes 1k/2k/4k, quality tiers, mask inpaint; uses `/v1/images/generations` and `/v1/images/edits`.
- Gallery covers research figures, posters, UI mockups, anime, typography, maps, tattoos.
- Install via `npx skills add` for Codex/Claude/OpenClaw/Hermes or `uvx --from git+... gpt-image`.
- Reads `OPENAI_API_KEY` from env / `.env` / `~/.env`.
- Complements Nano Banana (Gemini) and MeiGen (multi-model gallery) rather than replacing them.

## Why saved

Still-image generation for scroll-world scene stills, DESIGN.md mood boards, and infographic figures with a skill-shaped interface — not a raw playground.

## Topics

`agent-skills`, `design`

## Related

`github-youmind-openlab-nano-banana-pro-prompts`, `web-meigen-ai`, `web-fal-ai`, `github-oso95-scroll-world`, `web-sceneai-art`

## Use when

An agent must call GPT Image 2 with proven prompts; editing with references/masks; generating UI mockups or poster frames before motion/video.
