# Graph Report - design-ideas  (2026-09-05)

## Corpus Check
- 983 files · ~229,046 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 987 nodes · 4762 edges · 21 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b2ec8198`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after analysis markdown changes (heuristic rebuild: `python3 scripts/analysis/build_graph.py`).

## Community Hubs (Navigation)
- SERP & AI-answer visibility (SEO / AEO / GEO) (serp-ai-visibility)
- Outbound / GTM agent stacks (outbound-gtm-agents)
- Gaussian splatting (3DGS) capture, edit, export (gaussian-splatting)
- Image/video → 3D world, mesh, scene (image-to-3d-world)
- Blender/Unreal blockout + agent camera → video model (blockout-to-video-flythrough)
- AI video models, tools, and launch-video craft (ai-video-generation)
- Code-rendered motion graphics and HTML-as-video (code-motion-graphics)
- Three.js / WebGL / WebGPU / Spline scenes on the web (web-3d-scenes)
- Landing pages, UI component libraries, scroll motion, visual reference (landing-ui-motion)
- Design skills, DESIGN.md contracts, vibe-design workspaces, anti-slop (design-agent-skills)
- Image-gen prompt galleries and prompt-as-skill (image-prompt-galleries)
- Agent harnesses, autoresearch loops, orchestration, agent ops (agent-harness-loops)
- Agent memory, second brains, company knowledge bases (agent-memory-knowledge)
- MCP servers, tool routers, agent browsers, computer-use (mcp-and-agent-browsers)
- Infographics, diagrams-as-content, charts (infographics-diagrams)
- AI CAD, text-to-CAD, PCB and keyboard hardware (ai-cad-hardware)
- Local / edge inference, open-weight model releases (local-inference-models)
- Shared tool pages
- Shared technique pages
- Shelf indexes
- Analysis layer entry

## God Nodes (most connected - your core abstractions)
1. `Design skills, DESIGN.md contracts, vibe-design workspaces, anti-slop (design-agent-skills)` - 291 edges
2. `Landing pages, UI component libraries, scroll motion, visual reference (landing-ui-motion)` - 206 edges
3. `Agent harnesses, autoresearch loops, orchestration, agent ops (agent-harness-loops)` - 196 edges
4. `AI video models, tools, and launch-video craft (ai-video-generation)` - 147 edges
5. `blockout-then-video-model` - 141 edges
6. `SERP & AI-answer visibility (SEO / AEO / GEO) (serp-ai-visibility)` - 138 edges
7. `Three.js / WebGL / WebGPU / Spline scenes on the web (web-3d-scenes)` - 130 edges
8. `MCP servers, tool routers, agent browsers, computer-use (mcp-and-agent-browsers)` - 125 edges
9. `Image/video → 3D world, mesh, scene (image-to-3d-world)` - 95 edges
10. `Outbound / GTM agent stacks (outbound-gtm-agents)` - 91 edges
11. `AI CAD, text-to-CAD, PCB and keyboard hardware (ai-cad-hardware)` - 84 edges
12. `Agent memory, second brains, company knowledge bases (agent-memory-knowledge)` - 81 edges

## Surprising Connections (you probably didn't know these)
- Concept aliases connect Splat2Mesh to LichtFeld Studio through the gaussian-splatting brief.

## Communities (21 total, 0 thin omitted)

Communities are subject briefs plus tool-pages / technique-pages / shelf-pages.
Hubs are brief H1s and shared method/tool pages — not harvest folder headings.

