# AI CAD, text-to-CAD, PCB and keyboard hardware (ai-cad-hardware)

## ai-cad-hardware — scope

Text-to-CAD tools and demos (CadXStudio, Smith, VibeCAD, OpenSCAD+skills, Fusion MCP, text-to-cad), FreeCAD internals, PCB autorouting, KiCAD+OpenEMS simulation, AI schematic design, EM field visualisation for boards, ergonomic keyboards.

Exclusion: Web 3D engine demos → web-3d-scenes.

Priority `later`. Owner aliases: CAD, keyboard, PCB, KiCad.
Expected primary range [14, 20]. This roster has **17** primary and **0** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## ai-cad-hardware — what the owner is trying to decide

Later lane. Decide whether text-to-CAD + Fusion MCP + PCB autoroute is a real hardware loop or a pile of demos. Keyboards stay later by owner request.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## ai-cad-hardware — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=4, technique=6, example=13, claim-source=7, reference=2.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (1):
- [Atlas Fields Studio — free 3D EM field viewer for PCB designs](../../items/x-2094840529997410525/card.md) — tool, reference — Arena Physica releases Atlas Fields Studio at fields-studio.arenaphysica.com, a free web app to explore electromagnetic fields around…

First role `technique` (3):
- [OpenSCAD homelab rack via Cursor plan mode and grill-me skill](../../items/x-2088252062454751483/card.md) — technique, example — Anaïs Betts describes designing a custom homelab server rack with OpenSCAD, Cursor plan mode, and Matt Pocock's grill-me skill, then…
- [Fusion MCP agents querying assemblies like a CAD database](../../items/x-2088296314484162719/card.md) — technique, claim-source — Rina argues MCP-style agents in Autodesk Fusion can search messy assemblies, isolate fasteners, param-edit screw sizes, and re-layout…
- [Custom PCB autorouter finishes keyboard board in one minute on two layers](../../items/x-2091891133286605067/card.md) — technique, claim-source — Paul Hetherington reports his custom PCB autorouter completes a keyboard board in about one minute on two layers versus four, beating…

First role `example` (11):
- [CadXStudio one-prompt parametric bookshelf speaker enclosure](../../items/x-2087272209429766596/card.md) — example, tool — CadX Studio demo tweet shows a parametric bookshelf speaker enclosure with walnut legs and perforated steel grille generated from one…
- [VibeCAD exploded-view and simulation progress demo](../../items/x-2088277946918142211/card.md) — example, technique — @10_X_eng shows VibeCAD progress on exploded mechanical views and motion simulations, arguing the workflow is becoming usable for…
- [CadX Studio text-to-CAD hexacopter demo](../../items/x-2088308976278790258/card.md) — example, tool — CadX Studio tweet demoing a prompt-generated hexacopter to show text-to-CAD removing the CAD skills wall for hardware ideas; links…
- [CadX Studio text-to-CAD demo: prompt-built screwdriver design](../../items/x-2089717063921332378/card.md) — example, tool — CadX Studio shows prompt-to-CAD on cadxstudio.in, generating a fully designed screwdriver from language as a TextToCAD…
- [Opus-in-Smith prompt-to-manufacturable mini jet engine demo](../../items/x-2089802212000362939/card.md) — example — Archedotco demo of a manufacturable mini jet engine designed with Opus inside Smith CAD, tagged #prompttoengine
- [CadX Studio prompt-to-CAD wheel hub with bolt circle and spline](../../items/x-2090535643353153833/card.md) — example, claim-source — CadX Studio demo testing AI design of a wheel hub with bolt circle, drive spline, and brake-disc mount, going from prompt to CAD model…
- [CadX Studio one-shot AI Stanley cup product design demo](../../items/x-2091621183422943726/card.md) — example, claim-source — CadX Studio demo tweet: AI designed a Stanley-style cup in one shot with zero CAD skills, built entirely in cadxstudio.in
- [KiCad + OpenEMS harness flags PCB signal-integrity issues before fab](../../items/x-2093020107509514674/card.md) — example, technique — Author built a fully open-source KiCad plus OpenEMS physical simulation harness to check PCB signal integrity before sending boards to…
- [Fusion MCP stress-test: weird concentric-ring CAD assembly stays aligned](../../items/x-2093305736717545869/card.md) — example, technique — Demo of an AI-built Autodesk Fusion assembly via MCP stacking concentric rings, shafts, and dense central mechanisms; author argues…
- [Claude Fable 5.1 agentic CAD in Fusion — SO-101 gripper plus Pi Camera mount](../../items/x-2095193896687177873/card.md) — example, reference — Adam reports Claude Fable 5.1 at Max effort is the strongest agentic CAD model they have tested, rebuilding an SO-101 gripper around the…
- [Fable 5.1 one-shot quad-turbo W16 CAD model and animation](../../items/x-2095352925597884465/card.md) — example, claim-source — @earthtojake demo claims Fable 5.1 one-shotted a full quad-turbo W16 engine as a CAD model plus animation in a single generation, shown…

First role `claim-source` (2):
- [SipeedLab claim — AI schematic design in one hour vs half day](../../items/x-2092106682302140648/card.md) — claim-source — SipeedLab X post claiming AI automated schematic design finishes in one hour what takes a skilled engineer half a day
- [Programmatic CAD efficiency — text-to-cad demos are 10GB meshes from <3MB Python](../../items/x-2095548418533798086/card.md) — claim-source, example — Jake argues programmatic CAD expresses complex geometry more efficiently: the text-to-cad repo ships about 10GB of demo models generated…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Fusion MCP stress-test: weird concentric-ring CAD assembly stays aligned](../../items/x-2093305736717545869/card.md)

## ai-cad-hardware — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [text-to-cad](../../techniques/text-to-cad.md) — Natural language or OpenSCAD skills that emit CAD solids or assemblies.
- [pcb-autorouting](../../techniques/pcb-autorouting.md) — Autoroute plus signal-integrity sim on a board, not just a pretty 3D PCB render.
- [cad-agent-assembly](../../techniques/cad-agent-assembly.md) — Fusion (or similar) MCP that constrains parts into an assembly.

## ai-cad-hardware — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [cadxstudio](../../tools/cadxstudio.md)
- [vibecad](../../tools/vibecad.md)
- [cadx-studio](../../tools/cadx-studio.md)
- [freerouting](../../tools/freerouting.md)
- [deeppcb](../../tools/deeppcb.md)
- [kicad](../../tools/kicad.md)
- [openems](../../tools/openems.md)
- [autodesk-fusion](../../tools/autodesk-fusion.md)
- [claude-fable](../../tools/claude-fable.md)
- [fusion](../../tools/fusion.md)
- [fable-cad](../../tools/fable-cad.md)
- [text-to-cad](../../tools/text-to-cad.md)

## ai-cad-hardware — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `x-2087272209429766596#c1` | Single prompt produced a parametric bookshelf speaker enclosure claimed manufacturing-ready. | stated | [CadXStudio one-prompt parametric book…](../../items/x-2087272209429766596/card.md) |
| `x-2088252062454751483#c1` | grill-me plus OpenSCAD in Cursor plan mode produced a printable homelab rack from enclosure dimensions and a parts list. | demonstrated | [OpenSCAD homelab rack via Cursor plan…](../../items/x-2088252062454751483/card.md) |
| `x-2088277946918142211#c1` | VibeCAD now supports exploded views and simulations of mechanical assemblies. | stated | [VibeCAD exploded-view and simulation …](../../items/x-2088277946918142211/card.md) |
| `x-2088277946918142211#c2` | The author says the workflow is becoming decent and very usable. | stated | [VibeCAD exploded-view and simulation …](../../items/x-2088277946918142211/card.md) |
| `x-2088296314484162719#c1` | The described Fusion workflow finds fasteners in a large assembly, hides everything else, and changes dimensions acro… | stated | [Fusion MCP agents querying assemblies…](../../items/x-2088296314484162719/card.md) |
| `x-2088296314484162719#c2` | MCP-style agents that understand existing engineering data can automate find-filter-param-pattern work on live assemb… | stated | [Fusion MCP agents querying assemblies…](../../items/x-2088296314484162719/card.md) |
| `x-2088308976278790258#c1` | CadX generated a hexacopter from a text prompt as a greenfield hardware sketch. | stated | [CadX Studio text-to-CAD hexacopter demo](../../items/x-2088308976278790258/card.md) |
| `x-2089717063921332378#c1` | CadX Studio generates a fully designed screwdriver from a prompt on cadxstudio.in. | stated | [CadX Studio text-to-CAD demo: prompt-…](../../items/x-2089717063921332378/card.md) |
| `x-2089802212000362939#c1` | The shown mini jet engine was designed with Opus in Smith and is described as manufacturable. | stated | [Opus-in-Smith prompt-to-manufacturabl…](../../items/x-2089802212000362939/card.md) |
| `x-2090535643353153833#c1` | CadX Studio produced a wheel hub with bolt circle, drive spline, and brake disc mount from a prompt through to an eng… | stated | [CadX Studio prompt-to-CAD wheel hub w…](../../items/x-2090535643353153833/card.md) |
| `x-2091621183422943726#c1` | CadX Studio generated a Stanley cup design in one shot without CAD skills. | stated | [CadX Studio one-shot AI Stanley cup p…](../../items/x-2091621183422943726/card.md) |
| `x-2091891133286605067#c1` | The autorouter completes the board in around one minute on two layers instead of four. | stated | [Custom PCB autorouter finishes keyboa…](../../items/x-2091891133286605067/card.md) |
| `x-2091891133286605067#c2` | Freerouting could not complete the same board after twenty-five minutes of routing. | stated | [Custom PCB autorouter finishes keyboa…](../../items/x-2091891133286605067/card.md) |
| `x-2092106682302140648#c1` | AI automated schematic design finishes in one hour what takes a skilled engineer half a day. | stated | [SipeedLab claim — AI schematic design…](../../items/x-2092106682302140648/card.md) |
| `x-2093020107509514674#c1` | A custom KiCad plus OpenEMS harness can check signal integrity of a PCB design before fabrication. | demonstrated | [KiCad + OpenEMS harness flags PCB sig…](../../items/x-2093020107509514674/card.md) |
| `x-2093305736717545869#c3` | Quoted Fusion X article documents Codex MCP at 127.0.0.1:27182/mcp (14,743-char fxtwitter body). | demonstrated | [Fusion MCP stress-test: weird concent…](../../items/x-2093305736717545869/card.md) |
| `x-2093305736717545869#c5` | Rings stress-test is an X amplify video 15.866 s at 2452×1080; no STEP/F3D in this bank. | demonstrated | [Fusion MCP stress-test: weird concent…](../../items/x-2093305736717545869/card.md) |

Full set: claims.jsonl (33 rows)

## ai-cad-hardware — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- text-to-CAD vs MCP-in-Fusion/KiCad
- mesh/solid validity
- PCB / SI simulation present
- local vs cloud CAD
- keyboard-specific vs general mechanical

## ai-cad-hardware — thread coverage

X items in primary roster: 17. captured_full=0, captured_partial=14, empty=3, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2087272209429766596](../../items/x-2087272209429766596/thread.md) | captured_partial | 32 | 1 | 1 |
| [x-2088252062454751483](../../items/x-2088252062454751483/thread.md) | captured_partial | 17 | 3 | 3 |
| [x-2088277946918142211](../../items/x-2088277946918142211/thread.md) | captured_partial | 5 | 1 | 0 |
| [x-2088296314484162719](../../items/x-2088296314484162719/thread.md) | captured_partial | 18 | 3 | 2 |
| [x-2088308976278790258](../../items/x-2088308976278790258/thread.md) | captured_partial | 4 | 1 | 0 |
| [x-2089717063921332378](../../items/x-2089717063921332378/thread.md) | empty | 0 | 0 | 0 |
| [x-2089802212000362939](../../items/x-2089802212000362939/thread.md) | captured_partial | 6 | 3 | 1 |
| [x-2090535643353153833](../../items/x-2090535643353153833/thread.md) | empty | 0 | 0 | 0 |
| [x-2091621183422943726](../../items/x-2091621183422943726/thread.md) | captured_partial | 4 | 1 | 0 |
| [x-2091891133286605067](../../items/x-2091891133286605067/thread.md) | captured_partial | 27 | 1 | 1 |
| [x-2092106682302140648](../../items/x-2092106682302140648/thread.md) | captured_partial | 25 | 3 | 2 |
| [x-2093020107509514674](../../items/x-2093020107509514674/thread.md) | captured_partial | 34 | 1 | 1 |
| [x-2093305736717545869](../../items/x-2093305736717545869/thread.md) | empty | 0 | 0 | 0 |
| [x-2094840529997410525](../../items/x-2094840529997410525/thread.md) | captured_partial | 71 | 1 | 1 |
| [x-2095193896687177873](../../items/x-2095193896687177873/thread.md) | captured_partial | 79 | 1 | 1 |
| [x-2095352925597884465](../../items/x-2095352925597884465/thread.md) | captured_partial | 64 | 1 | 0 |
| [x-2095548418533798086](../../items/x-2095548418533798086/thread.md) | captured_partial | 19 | 1 | 1 |

## ai-cad-hardware — gaps and open questions

Primary readiness: ready=3, ready-with-gaps=14. Gap tags: linked-page-unfetched=3, media-undescribed=2, thread-partial=1, thread-failed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Does any text-to-CAD item produce manifold solids a mill can cut?
- Is Fusion MCP further along than OpenSCAD skills for assemblies?

If this subject drops below 6 primary items after a future reclass, merge it into `image-to-3d-world` and delete the folder.

## ai-cad-hardware — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [image-to-3d-world](../image-to-3d-world/brief.md)
- [gaussian-splatting](../gaussian-splatting/brief.md)

