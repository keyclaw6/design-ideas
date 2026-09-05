# Plan of attack: salvage phone photos → Gaussian splat → minimal mesh

**Date:** 2026-09-05  
**Status:** inventory + 90s clustering + vision labels (no COLMAP / training yet)  
**Adjacent:** [gaussian-splatting](../../catalog/topics/gaussian-splatting.md), [bess-3d-flythrough](../../catalog/topics/bess-3d-flythrough.md), [blender-minimax-h3-video-generation](blender-minimax-h3-video-generation.md)

The cabinet is **reassembled**. These photos are the last capture. Goal: reuse them, get a usable 3DGS if the geometry allows, convert splat → mesh, then **decimate to a minimal mesh**. If SfM cannot lock, skip splat and go photo→mesh or CAD blockout + photo projection.

---

## 1. What we actually have

Composio **project API key** works against REST v3.1 (`x-api-key`). CLI `login --user-api-key` still 401 — that path wants a user-session key, not a project key. Connected account: **kab264z@gmail.com**. Google Drive is ACTIVE (`ca_eX96RS8QtGDe`). Google Photos is ACTIVE but limited to app-created data (empty library).

**Canonical capture:** Google Drive folder [`SPLAT images`](https://drive.google.com/drive/folders/1KUN9rAjrH8rRDVzJHIj-JOnZUCVFKrOi) (created 2026-09-05), seven zip chunks (~2.25 GB):

| Zip | Size | Files (zip listing) | Timestamp prefix |
|---|---|---|---|
| `Photos-1-001.zip` | 45 MB | 17 | `20260626_0552*` |
| `Photos-1-001(1).zip` | 218 MB | 63 | `20260610_143*` |
| `Photos-1-001(2).zip` | 374 MB | 109 | `20260610_140*` |
| `Photos-1-001(3).zip` | 275 MB | 78 | `20260610_135*` |
| `Photos-1-001(4).zip` | 357 MB | 108 | `20260610_083*` |
| `Photos-1-001(5).zip` | 656 MB | 187 | `20260610_083*` (overlap with 4) |
| `Photos-1-001(6).zip` | 321 MB | 92 | `20260609_104*` / `111*` |

Samsung `YYYYMMDD_HHMMSS.jpg` stills (~3 MB, 4000×3000 class). Dates **2026-06-09, 2026-06-10, 2026-06-26**. Zips (4) and (5) share names; `unzip -n` left **544 unique Samsung names** plus two unzip copies (`…(0).jpg`). Drive access confirmed as **Kristian Bilstrup / kab264z@gmail.com** (`GOOGLEDRIVE_GET_ABOUT`). Cursor’s Google Drive MCP on this worker still `needsAuth` (handshake timeout); Composio REST is the working path.

Local copies (not in git): `/home/kab/.cache/bess-splat-plan/` (zips, extract, 90s JSON, cluster previews).

### Vision-labeled assets (90s gaps + first/mid/last stills)

Do **not** train all 544 as one scene. Cluster 3 is a 3-frame detail burst of cluster 2 — attach it. Clusters 5 and 6 are the **same Envicool LCU** minutes apart (lid on, then lid off) — train separately first. Cluster 4 is one continuous cabinet walk (no ≥15s gap) with mixed orbit vs connector close-ups.

| ID | n | Window | What vision sees | First train path |
|---|---|---|---|---|
| **C1** | 58 | Jun 9 10:42–10:44 | Open PCS/inverter on a stool: GRID-A/B/C busbars, orange HV front, potting | COLMAP / 3DGS (specular metal) |
| **C2** | 31 | Jun 9 11:09–11:11 | Different black chassis: **BCU-B30**, KM1/FU, orange busbars, lime-green insulator | COLMAP; skip-splat if thin |
| **C3** | 3 | Jun 9 11:18 | C2 close-ups: RSGE 175-400 DC 1000V, RXLG 200W 50R, TSA1038 | Attach to C2 |
| **C4** | 185 | Jun 10 08:28–08:34 | **Assembled open cabinet**: stacked ZG-Mod-52, door electronics, in-bay Envicool **ENR605HFC1A**, Fire COM close-ups | Volume candidate; optional scale split |
| **C5** | 78 | Jun 10 13:52–13:55 | Standalone Envicool **LCU** on pallet: DEBUG/COM/POWER 220V, honeycomb, CHARGE/OUTLET | **First splat attempt** |
| **C6** | 109 | Jun 10 14:01–14:06 | Same LCU **open**: V-coil, fans, compressor **LP624D3FSBD1** R134a, red tanks, PUMP | **Second splat attempt** |
| **C7** | 63 | Jun 10 14:36–14:37 | Installed ZG-Mod-52 face: PACK+/PACK−, COM-IN/OUT, nameplate | Skip-splat or CAD + photo |
| **C8** | 17 | Jun 26 05:52–05:54 | Grey alcove: Tesoer TXA1725 fans, EATON; some motion blur | Filter blur; skip-splat |

### Dataset A — Woshixing 2025-08-06 (wrong set; do not train)

Earlier pass used `gdrive:Suppilers Doc's/Woshixing/Photos/` (20 stills + 1 clip). Same phone, factory internals, but **not** the requested dataset. Keep as extra reference only.

### Dataset B — FAT / factory exterior (not splat)

`gdrive:First Batch FAT pictures/` and shared `Pictures/Real images ZG-261/` — WhatsApp JPEGs ~1536×2048, **2026-02-10**. Exterior cabinet at an **IPX5 test** rig, Zynex branding. No EXIF. **Do not train 3DGS on these.**

### Dataset C — Brædstrup site (same phone, wrong subject)

Shared `Pictures/Braedstrup-Pilot-Installation-Photos/` — 24 JPEG + 2 MP4, same SM-S901B, **2026-05-28 → 2026-07-02**. Civil trench / foundation / site. Same capture device as A, **not** internals.

### Dataset D — marketing / CAD (downstream only)

Twinmotion renders, website screenshots, labels, `BESS placering.png`. Use after a mesh exists, not as capture.

---

## 2. Why prior Gaussian splats failed (and what this set changes)

Catalog trainers still need **SfM poses**. Casual phone interiors fight that (specular modules, textureless paint, unlocked AE, mixed orientation).

The **Woshixing 20-still set** was too sparse. The **SPLAT images** dump is different: Jun 10 afternoon alone is ~250 stills in a continuous window. Gate is still **COLMAP per time-cluster**, not one splat of all 650 frames mixed. Split by 90s+ gaps first; do not train Jun 9 + Jun 10 + Jun 26 as one scene.

ArtiFixer repairs a **thin splat**. It does not invent cameras if COLMAP fails.

---

## 3. Methods (from the design-ideas harvest)

### Gate (do this first, cheap)

**COLMAP / GLOMAP overlap audit per asset** on undistorted, orientation-normalized stills.  
If **&lt;30% of images register** → abandon splat for that asset (expected for C3/C7/C8; possible for C2).

Preprocess before the audit:

- `exiftran` / Pillow: apply Orientation, then strip.
- Undistort with a Galaxy S22 profile (or COLMAP simple radial).
- Optional: mask orange HV + glass/LED glare for feature extraction only.
- Drop motion-blur frames in C8 before any audit.

### Path 1 — Salvage 3DGS (only if the gate passes)

```
per-asset stills → SfM → Splat.js (MIT, in-browser) or LichtFeld (GPU)
  → [holes] ArtiFixer 1.3B on Linux CUDA
  → splat PLY
```

Harvest: `x-2090839282831270173` (Splat.js), `x-2091899114153754949` (LichtFeld), `github-nv-tlabs-ArtiFixer`.

**Linux worker:** Splat.js + ArtiFixer. LichtFeld is desktop/GPU-heavy.  
**Try first:** C5 (closed LCU, 78 stills), then C6 (open LCU, 109), then C1 (PCS guts, 58).

### Path 2 — Skip splat, photo → mesh (default for C7/C8 and any cluster that fails the gate)

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
  + project cluster stills (four-view idea: x-2057113327508345047)
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

1. ~~Normalize + cluster + vision~~ **done** (8 clusters; C3→C2; C5≠C6 on first train).
2. **COLMAP audit** in order **C5 → C6 → C1 → C4**. Write register rates here. Drop a cluster if &lt;~30% register.
3. **C5 → Splat.js** (or LichtFeld) if overlap passes; then C6, then C1.
4. **If holey but posed:** ArtiFixer 1.3B, then IZUTSUYA vs Splat2Mesh.
5. **Skip-splat (Tripo/Meshy)** on C7, C8 (after blur filter), and C2 if the gate fails.
6. **Path 3 blockout** from readable labels (ZG-Mod-52 SN, Envicool ENR605HFC1A / LP624D3FSBD1, BCU-B30, GRID-A/B/C).
7. **Decimate** whatever mesh wins.

Do **not** train all zips as one scene. Do **not** mix 2025 Woshixing with this dump.

---

## 5. Platform / license (this Linux worker)

- Train/repair: Linux + CUDA (ArtiFixer Docker). Splat.js in a browser.
- Splat2Mesh: needs a **Windows 11** box (or skip; use IZUTSUYA).
- Commercial Zynex assets: **do not** ship Splat2Mesh output under the free personal license.
- FAT WhatsApp images: too small; ignore for geometry.

---

## 6. Open

- Any **failed PLY** from the earlier splat attempt to feed ArtiFixer?
- Measured cabinet / module dimensions for Path 3?
- Confirm Splat2Mesh commercial license vs stay on Blender/IZUTSUYA.
- Optional C4 sub-split (rack orbit vs Envicool bay vs Fire COM) if COLMAP chokes on mixed scale.

Scout evidence (not in git): `/tmp/bess-splat-plan/scout-*.md`. Cluster JSON + previews: `/home/kab/.cache/bess-splat-plan/`.
