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

**2026-09-04 capture — `mcp/` verify on clone `NomaDamas/CozyClay` v1.7.0.** Root `npm install` (three is a **devDependency**). `cd mcp && npm install && npm run verify` exit 0. `listTools` = **25** names (README “24 tools” is stale): `add_character`, `add_scene`, `apply_batch`, `capture_frame`, `describe_camera_move`, `describe_scene`, `describe_shot`, `focus_character`, `frame_shot`, `generate_motion`, `group_objects`, `live_status`, `load_motion`, `mark_camera_move`, `open_project`, `place_character`, `place_object`, `remove_character`, `remove_object`, `render_prompt`, `save_project`, `set_camera`, `set_prompt_blocks`, `switch_scene`, `update_object`. Extra vs the 24-count is **`load_motion`**.

`verify.mjs` (no editor): **420** `frame_shot` size×view×level×side combinations; detective/courier cast; `place_object` parent/child carry; `mark_camera_move` + `describe_camera_move`; **`render_prompt`** `mode=video` `model=seedance_2` must include “wide shot” / “24mm” / detective / courier; `save_project` / `open_project` `.cclayproject` round-trip; rejects paths outside project root, wrong extension, symlinks, external hard links. Also: protocol **2025-11-25**; HTTP origin guard forgedOrigin/Host **403**, loopback **200**. This is the in-memory fallback, not a headed `capture_frame`.

**2026-09-04 capture — `npm run verify:capture` timed out.** `mcp/verify-live-capture.mjs` with `CHROME_PATH=/usr/bin/google-chrome` (headless=new). Suite reached a connected live editor, then `capture_frame` returned `isError` text “Live editor error: Live editor timed out running capture_frame.” Assertion failed (`actual: true`). No 640×360 PNG / `nonBlackPixels` receipt. Remaining: a successful live-editor `capture_frame` (GPU/SwiftShader may be required).
<!-- NOTES:END -->
