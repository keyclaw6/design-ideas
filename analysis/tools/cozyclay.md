# Cozyclay

**Slug:** `cozyclay` · **Kind:** repo · **URL:** https://x.com/Yun_HDY/status/2091577179914338583 · **Canonical item:** [x-2091577179914338583](../items/x-2091577179914338583/card.md)
**Subjects:** [ai-video-generation](../subjects/ai-video-generation/brief.md), [blockout-to-video-flythrough](../subjects/blockout-to-video-flythrough/brief.md)
**Referenced by (2):**
- [CozyClay open-source previs before pricey AI video generation](../items/x-2091577179914338583/card.md) — tool, technique — blockout-to-video-flythrough
- [CozyClay open-source previs tool with MCP for fast shot iteration](../items/x-2092009056164872620/card.md) — tool, technique — blockout-to-video-flythrough

<!-- NOTES:START -->
Fetched 2026-09-04 from https://github.com/NomaDamas/CozyClay README + `mcp/README.md` (default branch).

- License **AGPL-3.0**. Install: `npx cozyclay` (Node 22.13+, Chromium). Demo reel: https://cozyclay.org/
- Browser studio: Three.js + R3F. Block scene, pose cast, timeline Prompt Blocks, camera fly/orbit, undo store. Motion gen is optional via Kimodo on an SSH NVIDIA box (`CCLAY_KIMODO_HOST=…`).
- MCP is real: `npx cozyclay mcp` or `node mcp/server.mjs`. README says **24 tools** appear. Editor-open calls drive the viewport; headless mode can block scenes and write `.cclayproject`. Live-only: `capture_frame`, `set_prompt_blocks`, `generate_motion`, `apply_batch`.
- Named tools include `describe_scene`, `describe_shot`, `frame_shot`, `set_camera`, `render_prompt`, `generate_motion`, `add_character` / `place_character`, `place_object` / `update_object`, `mark_camera_move`, `open_project` / `save_project`.
- `$17/30s` miss remains the author’s X claim, not a README number.
<!-- NOTES:END -->
