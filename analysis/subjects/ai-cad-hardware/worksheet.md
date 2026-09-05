# Judgment worksheet: AI CAD & hardware (ai-cad-hardware)

Later lane. Owner aliases: CAD, keyboard, PCB, KiCad. Keyboard *business* briefs stay out of this library; keyboard *boards* as PCB examples stay here. Web engine demos → [web-3d-scenes](../web-3d-scenes/worksheet.md).

## ai-cad-hardware — short stack to try

Two loops. Text-to-pretty-mesh is not the same as MCP-in-Fusion.

1. **MCP / programmatic CAD (assemblies).** Must-read Fusion MCP concentric-ring stress-test ([x-2093305736717545869](../../items/x-2093305736717545869/card.md)). Fusion-as-database argument ([x-2088296314484162719](../../items/x-2088296314484162719/card.md)). OpenSCAD + grill-me rack ([x-2088252062454751483](../../items/x-2088252062454751483/card.md)). “10GB meshes from <3MB Python” ([x-2095548418533798086](../../items/x-2095548418533798086/card.md)).
2. **PCB: autoroute + SI, not a 3D render.** Custom two-layer keyboard autorouter in ~1 minute ([x-2091891133286605067](../../items/x-2091891133286605067/card.md)). KiCad + OpenEMS harness ([x-2093020107509514674](../../items/x-2093020107509514674/card.md)). Atlas Fields Studio EM viewer ([x-2094840529997410525](../../items/x-2094840529997410525/card.md)).
3. **Text-to-CAD demos (look, don’t fab).** CadXStudio bookshelf / hexacopter / screwdriver / hub / Stanley cup. VibeCAD exploded views. Smith mini jet. Fable 5.1 gripper and W16 one-shots.

SipeedLab “one hour vs half day” schematic claim is a vendor clock.

## ai-cad-hardware — axis scores

| item | text-to-CAD vs MCP-in-DCC | mesh/solid validity | PCB / SI sim | local vs cloud CAD | keyboard-specific vs general |
|---|---|---|---|---|---|
| Fusion MCP rings (must-read) | MCP-in-Fusion | claimed aligned assembly | n/a | Fusion (cloud/local seat) | general |
| Fusion as CAD database | MCP-in-Fusion | param-edit claimed | n/a | Fusion | general |
| OpenSCAD + grill-me | text/skills → OpenSCAD | printable rack claimed | n/a | local | general (homelab) |
| text-to-cad Python repo | programmatic (11 skill dirs; MIT; **14,338★**) | tweet 10GB **not** in git; **covers.step** 11.2 MB / 56 solids validated | n/a | local | general |
| CadXStudio demos | text-to-CAD | unknown (pretty models) | n/a | hosted cadxstudio.in | general |
| VibeCAD | text-to-CAD + sim | unknown | n/a | unknown | mechanical |
| Smith + Opus jet | text-to-CAD | “manufacturable” claimed | n/a | Smith | general |
| Fable 5.1 Fusion gripper / W16 | agentic in Fusion | unknown | n/a | Fusion | robot mount / engine showpiece |
| custom autorouter | n/a | n/a | route only | local implied | keyboard board |
| KiCad + OpenEMS | n/a | n/a | high (SI before fab) | local OSS | general PCB |
| Atlas Fields Studio | n/a | n/a | EM view, not route | free web | PCB |
| SipeedLab schematic hour | AI schematic | unknown | schematic, not SI | unknown | general |

## ai-cad-hardware — claims that need a receipt

- Fusion rings “stay aligned” — must-read demo; need a STEP/F3D, not a video. Wrapper `export` can emit `step` / `f3d` ([autodesk-fusion](../../tools/autodesk-fusion.md)) but this host has no Fusion seat. Root amplify video is **15.866 s** / 2452×1080. Card is now `ready` (thread `empty`).
- Autorouter 1 minute / two layers vs four — one author’s board; no gerbers in this bank.
- OpenEMS harness “flags SI issues” — need one before/after plot.
- CadX / Smith / Fable W16 “one-shot manufacturable” — trailers. Do not send to a shop.
- 10GB from <3MB Python — **du’d**. Public tree blob sum **18,800,398** B; GitHub size **155,412** KB; `models/*/src/*.py` **3,046,558** B; W16 **12,678** lines. Tweet 10GB / 12,000 not in README. A real STEP from that tree now exists: `covers.step` **11.2 MB** / 56 solids ([text-to-cad](../../tools/text-to-cad.md)).
- Fable 5.1 “strongest agentic CAD” — ranking language in the source; do not echo it.

## ai-cad-hardware — do not treat as load-bearing

- Repeated CadXStudio product tweets — one product page is enough.
- Keyboard ergonomics / business content — out of scope for this library.
- SipeedLab hour-vs-half-day — no schematic attached.

## ai-cad-hardware — next capture work

1. Fusion official MCP vs `fusion-cad-mcp` 75/74 tools and `export` formats (`step`, `f3d`, …) are on [autodesk-fusion](../../tools/autodesk-fusion.md). Quoted X article **2089992746178150400** (title *GPT + Autodesk Fusion MCP…*; 14,743 chars via fxtwitter) documents Codex `127.0.0.1:27182/mcp` and argues MCP is not text-to-3D. Rings card is `ready` (thread `empty`; video **15.866 s**). Remaining: a STEP/F3D of the ring assembly (article has none; this host has no Fusion seat).
2. Keep PCB items (autoroute, OpenEMS, Fields Studio) in a separate shortlist from CadX demos.
3. text-to-cad repo + docs are on [text-to-cad](../../tools/text-to-cad.md). **Generated STEP now in-bank:** `cadgen 0.5.0` wrote `models/w16/STEP/covers.step` **11,769,007** B (56 solids / 129 occurrences / validate `failureCount` 0) — card `#c5`. Full `w16.py` engine not run (`BUILDING.md` memory warning). Tweet 10GB assembled meshes still not in git.
4. Do not expand keyboard coverage beyond boards already in the roster.
5. Fable 5.1 Fusion demo is an X amplify video **7.633 s** / 3396×2160 — no STEP/F3D ([fusion](../../tools/fusion.md)). Stale `media-undescribed` dropped; card stays `ready-with-gaps` (`thread-partial` 79/1). VibeCAD exploded-view clip is **58.616 s** / 1920×1080 ([vibecad](../../tools/vibecad.md)); thread 5/1. KiCad+OpenEMS harness has **no public repo**; artifact is a **17.866 s** / 1920×1024 clip ([openems](../../tools/openems.md)). Do not treat `antmicro/kicad-si-simulation-wrapper` as that harness.
