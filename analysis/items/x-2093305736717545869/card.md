# Fusion MCP stress-test: weird concentric-ring CAD assembly stays aligned

`x-2093305736717545869` · x · demo-video · en · [source](https://x.com/irinatoxi/status/2093305736717545869) · [raw](../../../raw/items/x-2093305736717545869/)
**Author:** irinatoxi (@irinatoxi) · **Published:** — · **Captured:** 2026-09-04T06:53:00Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [ai-cad-hardware](../../subjects/ai-cad-hardware/brief.md) · **Also:** — · **Roles:** example, technique · **Platforms:** fusion, mcp

**Summary.** Demo of an AI-built Autodesk Fusion assembly via MCP stacking concentric rings, shafts, and dense central mechanisms; author argues weird multi-part geometry is a better CAD agent benchmark than another gear because alignment holds under rotation.
**Question it answers.** How do you stress-test an AI CAD agent on weird assemblies instead of simple brackets?

**Claims.**
- `x-2093305736717545869#c1` (result, stated) A Fusion MCP-built assembly with concentric rings and intersecting shafts remains aligned and inspectable under rotation, making complex geometry a better agent benchmark than simple parts. — evidence: "The harder test is how weird the assembly can get before the agent loses the plot." [post]
- `x-2093305736717545869#c2` (capability, demonstrated) fusion-cad-mcp export() documents step and f3d among eight formats; a silent fail can return ok with bytes_written 0. No ring file was written here. — evidence: "tools.md export formats: stl, 3mf, step, iges, obj, f3d, sat, smt. Check bytes_written. This host has no Fusion seat." [note]
- `x-2093305736717545869#c3` (capability, demonstrated) Quoted tweet t.co/1UznDisZmz 301s to X article 2089992746178150400, titled GPT + Autodesk Fusion MCP: The AI That Can Build and Edit Real CAD Models. fxtwitter article payload is 76 blocks / 14,743 chars. Codex config shown: [mcp_servers.fusion] url = "http://127.0.0.1:27182/mcp". — evidence: "fxtwitter tweet 2089997971089703423 article.id 2089992746178150400. First sentence: Most AI-generated 3D demos become much less impressive once you ask what actually exists behind the final image. MCP URL in entityMap markdown." [note]
- `x-2093305736717545869#c4` (opinion, demonstrated) The article argues Fusion MCP is not text-to-3D: GPT can operate a live Fusion session (sketches, history, parameters, scripts) but still lacks engineering judgment and can make incorrect edits as fast as useful ones. It does not include a STEP/F3D of the concentric-ring assembly. — evidence: "Article H2s: This is not another text-to-3D generator; It still does not know whether the design is good; Direct control also makes mistakes faster. No ring/STEP filename in the 14,743-char body." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [cad-agent-assembly](../../techniques/cad-agent-assembly.md), [text-to-cad](../../techniques/text-to-cad.md)
**Tools.** [autodesk-fusion](../../tools/autodesk-fusion.md)
**Links.** https://x.com/i/article/2089992746178150400, https://x.com/irinatoxi/status/2089997971089703423
**Related items.** [x-2095193896687177873](../x-2095193896687177873/card.md), [x-2095352925597884465](../x-2095352925597884465/card.md)
**Media.**
`raw/items/x-2093305736717545869/media/media_0.jpg` (image, carries_technique=true) — Screen recording of a complex Fusion 360 assembly with concentric rings and radial spokes being rotated and inspected in the viewport.
**Thread.** empty · reported 0 · captured 0 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2095193896687177873](../x-2095193896687177873/card.md)
