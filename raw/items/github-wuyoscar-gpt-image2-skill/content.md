# GPT Image 2 Prompt Gallery + Agentic Skill + CLI

> Source: https://github.com/wuyoscar/GPT-Image2-Skill — by wuyoscar — captured 2026-09-02T17:15:19Z — stats-at-capture: stars=5056; forks=437; license=MIT; language=Python

## Article

**Repo:** wuyoscar/GPT-Image2-Skill  
**Stars:** 5,056 · **License:** MIT · **Python ≥ 3.11**

Curated GPT Image 2 prompt gallery, agent skill, and CLI for OpenAI image generation/editing. Surfaces: Claude Code, Codex, OpenClaw, Hermes Agent.

## Features

- Curated prompt gallery (research figures, posters, UI mockups, anime, typography, maps, tattoos)
- CLI: `gpt-image -p "prompt"` with text-to-image and multi-reference edits
- Supports sizes 1k/2k/4k, quality tiers, mask inpaint
- Uses OpenAI `/v1/images/generations` and `/v1/images/edits` endpoints

## Install

```bash
npx skills add wuyoscar/gpt_image_2_skill --skill gpt-image --agent codex
uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image -p "a cat astronaut"
```

Reads `OPENAI_API_KEY` from env, `.env`, or `~/.env`.
