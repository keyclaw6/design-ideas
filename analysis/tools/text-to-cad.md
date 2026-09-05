# Text To Cad

**Slug:** `text-to-cad` · **Kind:** product · **URL:** https://x.com/earthtojake/status/2095548418533798086 · **Canonical item:** [x-2095548418533798086](../items/x-2095548418533798086/card.md)
**Subjects:** [ai-cad-hardware](../subjects/ai-cad-hardware/brief.md)
**Referenced by (1):**
- [Programmatic CAD efficiency — text-to-cad demos are 10GB meshes from <3MB Python](../items/x-2095548418533798086/card.md) — claim-source, example — ai-cad-hardware

<!-- NOTES:START -->
**2026-09-04 capture — earthtojake/text-to-cad + texttocad.dev.** GitHub **MIT**, **14,338** stars / **1,520** forks. `GET https://www.texttocad.dev` **200 / 79,751 B**; HTML extract shows **0.4.28** and **14,338**. Recursive tree **1,634** entries (not truncated). **11** skill dirs: bambu-labs, cad, cad-viewer, dfam-check, dxf, gcode, sdf, sendcutsend, srdf, step-parts, urdf.

Tweet **~10GB** demo models / **<3MB** scripts / **12,000**-line W16 is **not** what the public tree holds. Blob sum **18,800,398** B; GitHub `size` **155,412** KB. All `.py` **695** files / **6,772,509** B. `models/*/src/*.py` **338** files / **3,046,558** B. `models/w16/src` **38** files / **12,678** lines / **562,721** B. README does not repeat those tweet integers. Do not collapse 10GB / 152 MB / 18.8 MB, or 12,000 / 12,678, or 3 MB / 6.77 MB. Receipt `text-to-cad-2026-09-04.json`.

**2026-09-05 capture — generated STEP from `models/w16`.** `pip install cadgen[snapshot]==0.5.0` (skill pin). `python3 src/covers.py` from `/tmp/repos/text-to-cad/models/w16` exit **0** in **44.262** s and wrote `STEP/covers.step` **11,769,007** B (`ISO-10303-21`, `AUTOMOTIVE_DESIGN`, Open CASCADE 7.9 / cadgen). Entity counts: **56** `MANIFOLD_SOLID_BREP` / **56** `CLOSED_SHELL` / **1,626** `ADVANCED_FACE`. `cadgen step inspect validate`: `ok`, `occurrenceCount` **129**, `prototypeCount` **56**, `failureCount` **0**. Full `w16.py` not run (`BUILDING.md` memory warning). Tweet 10GB assembled meshes still not in git. Receipt `text-to-cad-w16/covers-step-2026-09-05.json`.

**2026-09-05 leftover14 — OpenSCAD + nurb neighbor (no openscad.md / nurb.md).** `openscad.org` **8,719 B**. GitHub `openscad/openscad` **10,133★** license **NOASSERTION**. grill-me reply t.co is the official **157 B** alias in `mattpocock/skills`. Neighbor `nurb.dev` **29,103 B** (Ordinary Systems LLC talk-to-print). Official repo `Shpigford/nurb` **501★** license **NOASSERTION**; page copy **FSL-1.1-MIT** — do not collapse those. GH search `nurb.dev OR nurb cad` total **177,756** is other CAD/NURBS products — do not treat as an inventory. Printable homelab rack stays tweet-only ([x-2088252062454751483](../items/x-2088252062454751483/card.md)). Receipt `leftover14-2026-09-05.json` + `leftover14b-2026-09-05.json`.
<!-- NOTES:END -->
