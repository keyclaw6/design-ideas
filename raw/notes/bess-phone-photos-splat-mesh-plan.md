# Plan of attack: salvage phone photos → Gaussian splat → minimal mesh

**Date:** 2026-09-05  
**Status:** inventory + methods plan (no training run yet)  
**Adjacent:** [gaussian-splatting](../../catalog/topics/gaussian-splatting.md), [bess-3d-flythrough](../../catalog/topics/bess-3d-flythrough.md), [blender-minimax-h3-video-generation](blender-minimax-h3-video-generation.md)

The cabinet is **reassembled**. These photos are the last capture. Goal: reuse them, get a usable 3DGS if the geometry allows, convert splat → mesh, then **decimate to a minimal mesh**. If SfM cannot lock, skip splat and go photo→mesh or CAD blockout + photo projection.

---

## 1. What we actually have (Drive, not Google Photos)

Composio login with the provided user API key returned **HTTP 401**. Cached Composio tools on this machine have Gmail/Drive/Calendar — **no Google Photos toolkit**. Gmail MCP still needs a browser auth. Fallback: existing `rclone` remote `gdrive:` (My Drive + Shared with me + Shared drives).

**No Google Photos camera-roll dump was found on Drive.** If a larger 2026 internals set still lives only in Photos, that set is not in this inventory. Complete Composio/Photos auth to pull it.

### Dataset A — Woshixing factory internals (the splat candidate)

`gdrive:Suppilers Doc's/Woshixing/Photos/`

- 20 JPEG + 1 short MP4, **Samsung SM-S901B (Galaxy S22)**, 4000×3000, no special capture mode.
- Shot **2025-08-06 10:54–11:10** in one factory visit (warehouse roof visible in some frames).
- EXIF `Orientation` flips between 1 and 6 inside the same burst — rotate to a consistent frame **before** SfM.
- Sequential subjects with 4–6 minute gaps (not mixed). Vision + timestamps:

| Asset | Files | Time | What it is | Splat viability |
|---|---|---|---|---|
| **A1 — SVOLT module stack + HV string** | `105407.mp4`, `105412`–`105423` (4 stills) | 10:54 | Open door, two columns of labeled modules (e.g. 129-1…133-3), orange HV, then close-up of MSD + 3× junction panels (B+/P+, BMS J1–J4) + red/blue cooling valves | Weak: 4 stills + 1 clip, steep angle, specular black modules |
| **A2 — Thermal / HVAC bay** | `105905`–`105926` (8 stills) | 10:59 | White interior: Flying Sails `FSP-M1308I`, Envicool, insulated hoses; later frames look **down onto module tops** + foil heat shield + COM/Voir ports | Best still count; mixed viewpoints (wall vs module-top) — split before training |
| **A3 — Controls / 24V / PCS** | `110529`, `110532` (2 stills) | 11:05 | DIN rail: Mean Well SDR-240-24 + DRDN20-24, Robustel R3000, E-T-A, then silver chassis with Y/G/B/R/O power leads + PE bar | Too few views; use as photo→mesh / texture refs |
| **A4 — Empty / pre-fit enclosure** | `111047`–`111056` (6 stills) | 11:10 | Empty white rack rails, foil lining, MCB/SPD/`电表` cutouts, unit on a pallet | Few views of a mostly textureless box; hybrid CAD |

These are **ZG-261-class internals** (SVOLT cells, Envicool loop, Flying Sails thermal unit), not site civil works.

### Dataset B — FAT / factory exterior (not splat)

`gdrive:First Batch FAT pictures/` and shared `Pictures/Real images ZG-261/` — WhatsApp JPEGs ~1536×2048, **2026-02-10**. Exterior cabinet at an **IPX5 test** rig, Zynex branding. No EXIF. **Do not train 3DGS on these.**

### Dataset C — Brædstrup site (same phone, wrong subject)

Shared `Pictures/Braedstrup-Pilot-Installation-Photos/` — 24 JPEG + 2 MP4, same SM-S901B, **2026-05-28 → 2026-07-02**. Civil trench / foundation / site. Same capture device as A, **not** internals.

### Dataset D — marketing / CAD (downstream only)

Twinmotion renders, website screenshots, labels, `BESS placering.png`. Use after a mesh exists, not as capture.

---

## 2. Why prior Gaussian splats failed (this capture, not “the phone”)

Catalog trainers (Splat.js, LichtFeld, ArtiFixer) still need **SfM poses**. This set fights that:

1. **Too few views per asset** (2–8 stills). 3DGS wants tens–hundreds with ~60–80% overlap.
2. **Specular black modules + orange HV insulation** — matchers lock on reflections.
3. **Textureless white powder-coat** on A3/A4.
4. **Tight interior, small baseline** — handheld steps, not an orbit.
5. **EXIF orientation mix** and wide-angle distortion.
6. **Dim cabinet + auto exposure** (unlocked AE between shots).
7. **A2 mixes two geometries** (HVAC wall vs module tops) — training them as one scene collapses.

ArtiFixer (`github-nv-tlabs-ArtiFixer`) repairs a **thin splat**. It does not invent cameras if COLMAP registers almost nothing.

---

## 3. Methods (from the design-ideas harvest)

### Gate (do this first, cheap)

**COLMAP / GLOMAP overlap audit per asset** on undistorted, orientation-normalized stills.  
If **&lt;30% of images register** → abandon splat for that asset (expected for A3; likely A1/A4).

Preprocess before the audit:

- `exiftran` / Pillow: apply Orientation, then strip.
- Undistort with a Galaxy S22 profile (or COLMAP simple radial).
- Optional: mask orange HV + glass/LED glare for feature extraction only.
- Extract 2–3 fps from `105407.mp4` into A1.

### Path 1 — Salvage 3DGS (only if the gate passes)

```
per-asset stills → SfM → Splat.js (MIT, in-browser) or LichtFeld (GPU)
  → [holes] ArtiFixer 1.3B on Linux CUDA
  → splat PLY
```

Harvest: `x-2090839282831270173` (Splat.js), `x-2091899114153754949` (LichtFeld), `github-nv-tlabs-ArtiFixer`.

**Linux worker:** Splat.js + ArtiFixer. LichtFeld is desktop/GPU-heavy.  
**Try first:** A2 (8 frames) with HVAC-only vs module-top split.

### Path 2 — Skip splat, photo → mesh (default for A1/A3/A4)

```
3–8 best stills / asset → Tripo P2.0 (low-poly arena) or Meshy 7
  → Customuse or Blender cleanup/UV
  → GLB
```

Harvest: `x-2087905319255257296`, `x-2093018082293813509`.  
Use when the gate fails. Occluded backs will be invented — mark as **look-dev**, not as-built.

### Path 3 — Hybrid CAD truth + photo projection (accuracy)

```
blockout known bays (module pitch, DIN rail, PCS envelope)
  + project Dataset A photos (four-view idea: x-2057113327508345047)
  → Blender remesh/decimate → GLB
```

This matches the BESS note: **structure in 3D; AI only polishes**. Only path that can stay to scale.

### Path 4 — Fast orbit POC (not a product mesh)

One still → Atlas / spark.js (`x-2094864872853119216`) or WorldGen (`x-2095437841958314100`). Marketing orbit only.

### Splat → mesh (if Path 1 yields a PLY)

| Tool | Notes |
|---|---|
| **IZUTSUYA 3DGS Mesh Converter** (`x-2095336950890983773`) | Browser β, Linux-viable, PLY → GLB/STL/OBJ |
| **Splat2Mesh** (`web-arcana-splat2mesh`) | Best documented; **Windows 11**; personal/non-commercial — **paid license for commercial meshes** |
| Watertight | **Not guaranteed** (`x-2095136786095951924`) |

### Finish → minimal mesh (always)

```
dense OBJ/GLB → Blender Decimate / Remesh
  → [optional] Instant Meshes / pymeshlab (not in harvest; standard OSS)
  → UV + bake (Customuse or Blender)
  → production GLB
```

NeedleTools 3.2M→3k (`x-2091927587471712274`) was “coming soon” at harvest — check if shipped. Target **3k–20k tris per bay**, not a fused whole-cabinet soup.

---

## 4. Recommended attack order

1. **Pull Google Photos camera roll** (2026 internals, if any) once Composio/Photos auth works. Until then, treat Dataset A as the internals corpus.
2. **Normalize Dataset A** (orientation, undistort, split A2).
3. **COLMAP audit per asset.** Write register rates into this note.
4. **A2 HVAC subset → Splat.js** as the only honest splat experiment.
5. **If that splat is holey but posed:** ArtiFixer 1.3B, then IZUTSUYA (Linux) vs Splat2Mesh (Windows) on the same PLY.
6. **In parallel, don’t wait:** Path 2 on A1 (hero module stack) and A3 (controls) — 3 stills each into Tripo P2.0.
7. **Path 3 blockout** of one module column + one DIN bay using labels already readable in the photos (module IDs, Mean Well P/Ns, Flying Sails FSP-M1308I).
8. **Decimate** whatever mesh wins; do not ship dense splat-mesh.

Do **not** spend another cycle training a whole-cabinet splat from all 20 frames mixed.

---

## 5. Platform / license (this Linux worker)

- Train/repair: Linux + CUDA (ArtiFixer Docker). Splat.js in a browser.
- Splat2Mesh: needs a **Windows 11** box (or skip; use IZUTSUYA).
- Commercial Zynex assets: **do not** ship Splat2Mesh output under the free personal license.
- FAT WhatsApp images: too small; ignore for geometry.

---

## 6. Open

- Is there a **larger 2026 Google Photos** internals set beyond Woshixing 2025-08-06?
- Any **failed PLY** from the earlier splat attempt to feed ArtiFixer?
- Measured cabinet / module dimensions for Path 3?
- Confirm Splat2Mesh commercial license vs stay on Blender/IZUTSUYA.

Scout evidence (not in git): `/tmp/bess-splat-plan/scout-catalog-methods.md`, `scout-capture-repair.md`, `scout-mesh-cleanup.md`.
