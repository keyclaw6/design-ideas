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

No logged-in export was run here. spark.js is the Three.js viewer path, not the mesh path — see [spark-js](spark-js.md).
<!-- NOTES:END -->
