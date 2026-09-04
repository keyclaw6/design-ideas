# Idea bank completion plan

**Goal:** Turn 387 harvested items into a **navigable idea bank** — taxonomy, topic briefs, index, and patterns so a new LLM gets an overview without re-reading 311 X posts.

**Priority:** file structure and navigation over per-item prose. Do **not** pad `research.md`; leave thin or omit when the post speaks for itself.

**Status:** executing (2026-09-04, structure-first correction)

---

## 1. Natural category taxonomy

Categories map to `topics[]` in `source.json` (non-exclusive). Grouped for human navigation in `catalog/topics/`.

| Category file | Topic slug(s) | What belongs here |
|---------------|---------------|-------------------|
| `seo-agents.md` | `seo-agents` | SEO, AEO, GEO, citation outreach, directory launches, topical maps, GSC/IndexNow, rank tracking, AI search visibility |
| `agent-skills.md` | `agent-skills` | Cursor/Codex skills, taste/motion/UI skill packs, prompt galleries, agent workflows, context engineering |
| `mcp.md` | `mcp` | MCP servers, tool routing, browser MCP, sales/data MCP stacks, OpenRouter-for-tools |
| `design.md` | `design` | DESIGN.md, design systems, vibe-design, landing builders, UI kits, taste, checklists, infographics-as-design |
| `ui-motion.md` | `ui-motion` | Scroll-driven heroes, parallax, Lottie/motion templates, CSS/JS motion, marketing page motion pipelines |
| `three-js.md` | `three-js` | Three.js, WebGL, R3F, graphics agent skills, web 3D scenes |
| `video-generation.md` | `video-generation` | Veo/Kling/Seedance/MiniMax, image-to-video, html-video, ad/video gen tools |
| `bess-3d-flythrough.md` | `bess-3d-flythrough` | BESS/site flythroughs, industrial 3D marketing, scroll-world style landings |
| `gaussian-splatting.md` | `gaussian-splatting` | 3DGS capture, splat repair, PLY/mesh export, ArtiFixer, splat2mesh |
| `camera-control.md` | `camera-control` | Camera paths, Blender MCP flythrough, depth passes, cinematic motion reference |
| `keyboard-pcb.md` | `keyboard-pcb` | Ergonomic keyboards, PCB, split keyboards, hardware (later focus) |
| `infographics.md` | `infographics` | Data viz, diagram design, AntV, chart-as-content |

**Cross-cutting:** Many items get 2–3 topics (e.g. scroll-craft → `design`, `ui-motion`, `agent-skills`).

---

## 2. Filter rules (noise vs keep)

| Keep | Filter (mark `extra.filtered: true`, `topics: []`) |
|------|-----------------------------------------------------|
| Actionable technique, tool, repo, or pipeline | Pure engagement bait, giveaways, "follow for more" |
| Reusable for BESS marketing, 3D flythrough, SEO, or agent stack | Personal drama, politics, unrelated crypto/hype |
| Design/motion/SEO/MCP reference worth re-finding | Duplicate of another item with no new angle (link primary, filter duplicate) |
| Saved for a specific implementation idea | Empty quote-tweet with no linked artifact |

**Filtered items stay on disk** with `research.md` explaining why filtered — catalog index still lists them with note.

---

## 3. Per-item files (light touch)

**`source.json` (required for every item):**
- `topics`: array of slugs from SCHEMA (non-filtered items)
- `extra.filtered`: `true` for noise (keep on disk, `topics: []`)
- `extra.category_note`: optional one-line when taxonomy alone is unclear

**`research.md` (optional, value only):**
- Write only when the capture is thin, ambiguous, or needs cross-links the post does not provide
- A few bullets or one paragraph is enough — **no minimum length**, no template padding
- Skip entirely when `post.md` / linked repo is self-explanatory

---

## 4. Catalog rewrite standard

### `catalog/topics/*.md`
Each file becomes:
- **Brief** (2–4 paragraphs): what this lane is, how items relate, query hints for agents
- **Pipelines** (bullets): common workflows in this lane
- **Curated entries**: grouped subsections (Tools, Techniques, Examples), not flat link dumps

### `catalog/patterns.md`
Cross-lane pipelines an agent can follow (already started — expand with item ids from research pass).

### `catalog/index.md`
Regenerated via `scripts/rebuild_catalog.py` after all `source.json` updates.

---

## 5. Execution (Grok 4.6 workers — structure only)

| Worker | Scope |
|--------|--------|
| Taxonomy A | Uncategorized items batch 1 → `source.json` topics/filtered only |
| Taxonomy B | Uncategorized items batch 2 → `source.json` topics/filtered only |
| Briefs 1 | `catalog/topics/` — agent-skills, mcp, seo-agents |
| Briefs 2 | `catalog/topics/` — design, ui-motion, three-js |
| Briefs 3 | `catalog/topics/` — video-generation, bess-3d-flythrough, gaussian-splatting, camera-control, keyboard-pcb, infographics |
| Navigation | `catalog/README.md`, expand `catalog/patterns.md` |

Parent: fix `rebuild_catalog.py`, rebuild index item lists, `graphify update .`, commit, push.

---

## 6. Done criteria

- [ ] `topics` set on every non-filtered item; filters marked in `source.json`
- [ ] `catalog/README.md` — taxonomy map + query order for agents
- [ ] `catalog/topics/*.md` — briefs + curated subsections + auto item list
- [ ] `catalog/patterns.md` — cross-lane pipelines with item ids
- [ ] `catalog/index.md` matches disk (includes filtered flag)
- [ ] `graphify update .` committed
- [ ] Pushed to `origin/main`, working tree clean
- [ ] **Not required:** fat `research.md` on every item
