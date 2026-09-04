# Research

## What it is
Anaïs Betts’ recipe: OpenSCAD + Cursor + Matt Pocock’s grill-me skill to design a custom homelab server rack, then dump STLs into Bambu Studio.

## How it works
- 1) Empty folder + grill-me skill 2) Plan mode with enclosure dimensions + bill of items 3) Go 4) Export STL → Bambu.
- grill-me (see related reply in this batch) is the interrogation skill that forces the agent to specify sizes, clearances, and constraints before modeling.
- OpenSCAD keeps geometry parametric and git-friendly (keyboard/PCB/enclosure lane).
- Photos show a slotted chassis, hole grids, ghost volumes for reserved parts.
- Same grilling → CAD path as VibeCAD / CadX / Fusion-MCP items, but fully local/OSS.

## Why saved
Keyboard/hardware and plant-adjacent fixtures (racks, sensor mounts) need an agent CAD loop. This is the shortest Cursor-native version.

## Topics
`agent-skills`, `keyboard-pcb`

## Related
- `x-2088260067204137135` — link to grilling SKILL.md
- `x-2088290952704151671` — Pocock 25-skills overview
- `x-2087263510090874911` — AGENTS.md loading grilling among four skills
- `x-2088277946918142211` — VibeCAD exploded views
- `x-2088308976278790258` — CadX text-to-CAD hexacopter

## Use when
3D-printing an enclosure/rack/mount from a parts list, or combining grill-me with OpenSCAD instead of a hosted text-to-CAD product.
