# Atlas

**Slug:** `atlas` · **Kind:** product · **URL:** https://x.com/XRarchitect/status/2094864872853119216 · **Canonical item:** [x-2094864872853119216](../items/x-2094864872853119216/card.md)
**Subjects:** [gaussian-splatting](../subjects/gaussian-splatting/brief.md), [image-to-3d-world](../subjects/image-to-3d-world/brief.md)
**Referenced by (1):**
- [World Labs Atlas plus spark.js Three.js scene from one photo](../items/x-2094864872853119216/card.md) — example, technique — image-to-3d-world

<!-- NOTES:START -->
Fetched 2026-09-04 World Labs **Marble** docs (product name on docs.worldlabs.ai; the tweet still says Atlas).

Export is **not** “navigable field only.” Docs distinguish:

- **Highest fidelity:** Gaussian splat. Formats: SPZ ~2M / low-res SPZ ~500k; PLY ~2M / low-res PLY ~500k.
- **Collider mesh GLB** (Standard plan): 100–200k tris, 3–4 MB typical, physics only — “do not use for visual rendering.”
- **High-quality mesh GLB** (Pro): offline, **up to 1 hour**, rate-limited **4/hour/user**, owner-only. Two files: ~600k tris + textures (typical 100–200 MB) and ~1M tris + vertex colors. Artifacts expected (holes, floaters, thin/transparent/sky). Docs say use splat when visual quality matters.
- **360 pano:** 2560×1280 equirect PNG.
- **Free plan generates worlds but does not export.** Standard: splat + pano + collider. Pro: HQ mesh + commercial rights.
- Coordinates: OpenCV (+x left, +y down, +z forward); DCC often needs Y/Z scale −1.

**2026-09-04 capture — billing caps + public example files.** `GET https://docs.worldlabs.ai/llms.txt` 200 (7,570 bytes). Markdown export pages (HTML `/export/...` 404s; use `/marble/export/.../*.md`). Account-billing.md names four tiers: Free **up to 4** world gens (text / single image / 360 pano, no export); Standard **up to 12** (multi-image/video/3D, edit, export, community download); Pro **up to 25** (expand, HQ textured mesh, commercial rights); Max **up to 75**. Credits: e.g. single-image gen **1,580** (1,500 world + 80 input); Marble credits ≠ World API credits. Public example CDN `https://wlt-ai-cdn.art/example_exports/…` (no login). Rustic kitchen (`69a9fc22-…`): collider GLB **2,976,256** bytes (glTF magic `glTF`); 500k SPZ **7,582,907** bytes (gzip); pano PNG **3,860,086** bytes, valid PNG. Docs “typical 3–4 MB” collider is in the same band. These are **official example files**, not a logged-in user-world export.

No logged-in *user* export was run here. spark.js is the Three.js viewer path, not the mesh path — see [spark-js](spark-js.md).

Agent skill (docs): `npx skills add worldlabsai/marble-developer-api-skill --skill marble-developer-api` (optional `--global`). Mirror: `worldlabsai/marble-developer-api-skill`. Skill name `marble-developer-api` — world gen, media upload, operation polling, OpenAPI snapshot. Do not paste API keys into prompts.
<!-- NOTES:END -->
