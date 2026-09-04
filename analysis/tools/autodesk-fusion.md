# Autodesk Fusion

**Slug:** `autodesk-fusion` · **Kind:** product · **URL:** https://x.com/irinatoxi/status/2093305736717545869 · **Canonical item:** [x-2093305736717545869](../items/x-2093305736717545869/card.md)
**Subjects:** [ai-cad-hardware](../subjects/ai-cad-hardware/brief.md)
**Referenced by (1):**
- [Fusion MCP stress-test: weird concentric-ring CAD assembly stays aligned](../items/x-2093305736717545869/card.md) — example, technique — ai-cad-hardware

<!-- NOTES:START -->

**2026-09-04 capture — official MCP vs named-tool wrappers.** `Mfrostbutter/fusion-cad-mcp` README (beta 0.2.x): Fusion’s own MCP (`Preferences > General > API > Fusion MCP Server`, `127.0.0.1:27182/mcp`) exposes **four broad tools that take raw Python**. The wrapper registers **75** tools / **74** usable (`rib` always `rib_not_scriptable`); 467 tests; live pass against Fusion **2704.1.23**. Groups include sketch, features, assembly/joints (`create_joint`, `drive_joint`, `interference_check`), verify (`audit_feature_health`, `screenshot`), export. Escape hatch: `execute`. Other community servers exist (`Joe-Spencer/fusion-mcp-server` add-in, `faust-machines/fusion360-mcp-server`). The concentric-ring must-read ([x-2093305736717545869](../items/x-2093305736717545869/card.md)) is still video-only — no STEP/F3D, and the tweet does not name which MCP.

<!-- NOTES:END -->
