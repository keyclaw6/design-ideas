# Nano Banana Pro Prompts Recommend

**Slug:** `nano-banana-pro-prompts-recommend` · **Kind:** repo · **URL:** https://github.com/youmind-openlab/nano-banana-pro-prompts-recommend-skill · **Canonical item:** [github-youmind-openlab-nano-banana-pro-prompts](../items/github-youmind-openlab-nano-banana-pro-prompts/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [image-prompt-galleries](../subjects/image-prompt-galleries/brief.md)
**Referenced by (1):**
- [YouMind Nano Banana Pro prompt recommender skill (10k+ prompts)](../items/github-youmind-openlab-nano-banana-pro-prompts/card.md) — tool — image-prompt-galleries

<!-- NOTES:START -->
**2026-09-04 capture — prompt-file counts.** Clone `youmind-openlab/nano-banana-pro-prompts-recommend-skill` (shallow, same day as `references/manifest.json` `updatedAt` 2026-09-04T16:03:22.445Z). `package.json` license **MIT**; no `LICENSE` file in the tree. README badge still says **10,000+**.

Do not collapse these three integers:

- `manifest.json` `totalPrompts`: **15,508** across **11** category files.
- Sum of the 11 `count` fields / file array lengths: **22,466**.
- Unique `id` values across those files: **14,965**. **7,299** ids appear in two or more category files (largest overlap: `product-marketing.json` ∩ `social-media-post.json` = 3,238).

Category files and array lengths: profile-avatar 2,056; social-media-post 9,657; infographic-edu-visual 601; youtube-thumbnail 220; comic-storyboard 680; product-marketing 5,642; ecommerce-main-image 570; game-asset 713; poster-flyer 992; app-web-design 238; others 1,097. Each item has `id`, `content`, `title`, `description`, `sourceMedia`, `needReferenceImages`.

**Neighbor — MeiGen MCP repo** `jau123/MeiGen-AI-Design-MCP` v1.4.0 MIT. `data/trending-prompts.json` is a list of **exactly 1,446** objects (README “1,446 curated prompts”). Nine `src/tools/*.ts` registrations: `enhance-prompt`, `search-gallery`, `get-inspiration`, `generate-video`, `comfyui-workflow`, `manage-preferences`, `list-models`, `check-generation`, `generate-image`. `www.meigen.ai` and `/app` returned Cloudflare challenge **403** this pass (no live gallery count). Free tools in `server.ts` copy: search_gallery, enhance_prompt, get_inspiration, list_models, manage_preferences work without a key; generate_* need `MEIGEN_API_TOKEN`.
<!-- NOTES:END -->
