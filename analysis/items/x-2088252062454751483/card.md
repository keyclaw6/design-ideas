# OpenSCAD homelab rack via Cursor plan mode and grill-me skill

`x-2088252062454751483` · x · thread · en · [source](https://x.com/anaisbetts/status/2088252062454751483) · [raw](../../../raw/items/x-2088252062454751483/)
**Author:** Anaïs Betts (@anaisbetts) · **Published:** — · **Captured:** 2026-09-04T06:49:28Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [ai-cad-hardware](../../subjects/ai-cad-hardware/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** technique, example · **Platforms:** cursor, openscad

**Summary.** Anaïs Betts describes designing a custom homelab server rack with OpenSCAD, Cursor plan mode, and Matt Pocock's grill-me skill, then exporting STLs to Bambu Studio for printing.
**Question it answers.** What is the shortest Cursor-native workflow for a parametric 3D-printed rack from a parts list?

**Claims.**
- `x-2088252062454751483#c1` (recipe, demonstrated) grill-me plus OpenSCAD in Cursor plan mode produced a printable homelab rack from enclosure dimensions and a parts list. — evidence: "OpenSCAD + Cursor + grill-me is incredible! I just made a custom homelab server device rack" [post]
- `x-2088252062454751483#c2` (availability, demonstrated) OpenSCAD first-party: openscad.org 200 / 8,719 B (The Programmers Solid 3D CAD Modeller). GitHub openscad/openscad 10,133★ license NOASSERTION. Reply t.co/yIPMiN9j4k is the official grill-me SKILL.md (157 B alias → grilling). Neighbor reply t.co/NOGx8QjLUO is nurb.dev 29,103 B (Ordinary Systems LLC; “describe the part, print the part”; install.sh). Official repo Shpigford/nurb 501★ license NOASSERTION / page copy FSL-1.1-MIT — do not collapse those, and do not collapse nurb with the OpenSCAD rack. Printable-rack claim stays tweet-only. Do not invent openscad.md or nurb.md. — evidence: "openscad.org 8719 B; openscad/openscad 10133★ NOASSERTION; nurb.dev 29103 B; Shpigford/nurb 501★. leftover14 + leftover14b-2026-09-05.json." [note]
**Numbers.** —
**Recipe.** 1. Create an empty folder with grill-me skill loaded. 2. Use plan mode: specify enclosure size and bill of rack items. 3. Run generation to produce OpenSCAD geometry. 4. Export STLs and print in Bambu Studio.
**Techniques.** [text-to-cad](../../techniques/text-to-cad.md)
**Tools.** —
**Links.** product (https://openscad.org/), https://github.com/openscad/openscad, https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md, https://nurb.dev/
**Related items.** [x-2088260067204137135](../x-2088260067204137135/card.md), [x-2088277946918142211](../x-2088277946918142211/card.md), [x-2088308976278790258](../x-2088308976278790258/card.md)
**Media.**
`raw/items/x-2088252062454751483/media/media_0.jpg` (image, carries_technique=true) — OpenSCAD viewport of a slotted homelab rack with perforated plates, translucent ghost volumes for reserved parts, and coordinate axes on a grid.
`raw/items/x-2088252062454751483/media/media_1.jpg` (image, carries_technique=true) — Bambu Studio layout showing five print plates with rack frame, perforated square panels, and diagonal rail parts on numbered build surfaces.
**Thread.** captured_partial · reported 17 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
