# Catalog

Navigable idea bank over harvested items. Taxonomy and briefs first; do not pad per-item `research.md`.

Presence in the catalog is not a recommendation. Topics are tags, not a hierarchy — one item often has 2–3 slugs.

## Taxonomy

| Category file | Topic slug | What belongs here |
|---------------|------------|-------------------|
| [seo-agents.md](topics/seo-agents.md) | `seo-agents` | SEO, AEO, GEO, citation outreach, directory launches, topical maps, GSC/IndexNow, rank tracking, AI search visibility |
| [agent-skills.md](topics/agent-skills.md) | `agent-skills` | Cursor/Codex skills, taste/motion/UI skill packs, prompt galleries, agent workflows, context engineering |
| [mcp.md](topics/mcp.md) | `mcp` | MCP servers, tool routing, browser MCP, sales/data MCP stacks, OpenRouter-for-tools |
| [design.md](topics/design.md) | `design` | DESIGN.md, design systems, vibe-design, landing builders, UI kits, taste, checklists, infographics-as-design |
| [ui-motion.md](topics/ui-motion.md) | `ui-motion` | Scroll-driven heroes, parallax, Lottie/motion templates, CSS/JS motion, marketing page motion pipelines |
| [three-js.md](topics/three-js.md) | `three-js` | Three.js, WebGL, R3F, graphics agent skills, web 3D scenes |
| [video-generation.md](topics/video-generation.md) | `video-generation` | Veo/Kling/Seedance/MiniMax, image-to-video, html-video, ad/video gen tools |
| [bess-3d-flythrough.md](topics/bess-3d-flythrough.md) | `bess-3d-flythrough` | BESS/site flythroughs, industrial 3D marketing, scroll-world style landings |
| [gaussian-splatting.md](topics/gaussian-splatting.md) | `gaussian-splatting` | 3DGS capture, splat repair, PLY/mesh export, ArtiFixer, splat2mesh |
| [camera-control.md](topics/camera-control.md) | `camera-control` | Camera paths, Blender MCP flythrough, depth passes, cinematic motion reference |
| [keyboard-pcb.md](topics/keyboard-pcb.md) | `keyboard-pcb` | Ergonomic keyboards, PCB, split keyboards, hardware (later focus) |
| [infographics.md](topics/infographics.md) | `infographics` | Data viz, diagram design, AntV, chart-as-content |

Full table of every entry: [index.md](index.md). Cross-lane recipes: [patterns.md](patterns.md). Topic briefs: [topics/](topics/). Schema: [`SCHEMA.md`](../SCHEMA.md). Completion plan: [PLAN.md](PLAN.md).

## Query order (agents)

1. **This file** — pick a slug from the table.
2. **[index.md](index.md)** — id / title / `source_type` / topics / path (and filtered flag when present).
3. **`catalog/topics/<slug>.md`** — lane brief, Pipelines, curated Tools / Techniques / Examples, then the auto item list (`<!-- AUTO:ITEMS -->`). See [topics/](topics/).
4. **[patterns.md](patterns.md)** — pipelines that cross slugs, with item ids.
5. **Item folder** `raw/items/<id>/` (or `raw/notes/` for unsplit notes), in this order:
   - `source.json` — metadata, URL, topics, `related_items`
   - `page.md` or `post.md` — primary capture
   - `comments.md` — optional thread
   - `research.md` — **optional**; write or read only when the post is thin, ambiguous, or needs cross-links. Skip when `post.md` / the repo speaks for itself. No minimum length.
   - `media/` — screenshots, attachments

Graphify (`graphify query` / `explain` / `path`) before broad file search. After catalog or `raw/` edits: `graphify update .`.
