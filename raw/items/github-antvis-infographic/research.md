# Research

## What it is

Alibaba AntV framework (`@antv/infographic`) for generating and editing infographics: AI-tuned syntax, ~200 templates, themes, a built-in editor, and SVG output with a `skills/` pack for coding agents.

## How it works

- Agents emit compact template strings (`infographic list-row-simple-horizontal-arrow` style) that the renderer turns into editable SVG.
- Gallery at infographic.antv.vision/gallery; AI surface at /ai supports streaming model output into the renderer.
- Theme system covers hand-drawn and gradient looks so the same spec can match editorial vs product decks.
- npm package plus agent skills so Cursor/Claude can pick templates without hand-authoring SVG.
- Output stays vector, so infographics can land in marketing pages or DESIGN.md-driven sites without raster bake-in.

## Why saved

BESS and SEO content often needs diagrams that are not Mermaid-default. This is a programmable infographic stack with agent skills, complementary to Cathryn Lavery’s editorial HTML diagrams and Microsoft Flint’s chart IL.

## Topics

`infographics`, `design`, `agent-skills`

## Related

`github-cathrynlavery-diagram-design`, `web-flint-chart`, `github-youmind-openlab-nano-banana-pro-prompts`, `web-iandmacomber-post-ai-data-stack`, `github-wuyoscar-gpt-image2-skill`

## Use when

An agent must produce list/process/comparison infographics as SVG; you want template-driven viz instead of screenshot-from-Figma; pairing chart language (Flint) with narrative diagrams.
