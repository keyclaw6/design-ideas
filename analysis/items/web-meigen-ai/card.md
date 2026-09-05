# MeiGen: cross-model prompt gallery with MCP for GPT Image, Seedance, Nano Banana

`web-meigen-ai` · website · product · en · [source](https://www.meigen.ai/) · [raw](../../../raw/items/web-meigen-ai/)
**Author:** — (@—) · **Published:** — · **Captured:** 2026-09-02T17:15:19Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [image-prompt-galleries](../../subjects/image-prompt-galleries/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** tool, reference · **Platforms:** mcp, comfyui

**Summary.** MeiGen (meigen.ai) is a free community prompt gallery spanning GPT Image 2, Seedance, Nano Banana, and Midjourney with publish-to-earn credits, in-app generation tiers, and a 9-tool MCP repo for ComfyUI or OpenAI-compatible backends.
**Question it answers.** Which prompt gallery covers both image and video models with an agent-facing MCP server?

**Claims.**
- `web-meigen-ai#c1` (capability, stated) MeiGen MCP repo advertises 1,446+ curated prompts and nine MCP tools. — evidence: "1,446+ curated prompts, 9 MCP tools" [linked-page]
- `web-meigen-ai#c2` (capability, stated) Gallery spans GPT Image, Seedance, Nanobanana, and Midjourney with category browse and publish-to-earn credits. — evidence: "All GPT Image Seedance Nanobanana Midjourney" [linked-page]
- `web-meigen-ai#c3` (benchmark, demonstrated) A 2026-09-04 clone of jau123/MeiGen-AI-Design-MCP has exactly 1,446 objects in data/trending-prompts.json and nine src/tools registrations; www.meigen.ai returned Cloudflare 403 so the live gallery was not counted. — evidence: "trending-prompts.json list length 1446; nine tools: enhance-prompt, search-gallery, get-inspiration, generate-video, comfyui-workflow, manage-preferences, list-models, check-generation, generate-image" [note]
- `web-meigen-ai#c4` (availability, demonstrated) Live GET https://www.meigen.ai/ 200 / 129,701 B (Cloudflare 403 cleared). Title MeiGen - Free GPT Image 2, Nano Banana & Seedance 2.5 Prompts. SSR is a marketing/SPA shell (Loading…; 4 img tags; no 1,446 in HTML). /app is a mobile download page (104,802 B). /gallery and /api/prompts 404. Headed card count still missing; MCP file count 1,446 remains the counted integer. — evidence: "GET 200 https://www.meigen.ai/ 129701 B 2026-09-05. /gallery 404. analysis/_work/captures/meigen-live-2026-09-05.json" [note]
**Numbers.** MCP GitHub stars: 1737 stars (linked-page)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** repo (https://github.com/jau123/MeiGen-AI-Design-MCP), product (https://www.meigen.ai/app)
**Related items.** [github-wuyoscar-gpt-image2-skill](../github-wuyoscar-gpt-image2-skill/card.md), [github-youmind-openlab-nano-banana-pro-prompts](../github-youmind-openlab-nano-banana-pro-prompts/card.md), [web-fal-ai](../web-fal-ai/card.md), [web-sceneai-art](../web-sceneai-art/card.md), [github-oso95-scroll-world](../github-oso95-scroll-world/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
