# Refero DESIGN.md library — 2000+ product design languages for agents

`x-2093766772029559077` · x · product · en · [source](https://x.com/Voxyz_ai/status/2093766772029559077) · [raw](../../../raw/items/x-2093766772029559077/)
**Author:** — (@@Voxyz_ai) · **Published:** — · **Captured:** 2026-09-04T07:52:38Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** codex, cursor, cli

**Summary.** X post promoting styles.refero.design: over 2000 DESIGN.md files encoding colors, typography, spacing, and component rules from products like Linear and Notion. Agents read a file to align or rebuild UI to a chosen design language.
**Question it answers.** Where can agents get ready-made DESIGN.md files for well-known product design languages?

**Claims.**
- `x-2093766772029559077#c1` (capability, stated) Library has DESIGN.md files for 2000+ products with colors, type, spacing, and component rules. — evidence: "the design language of 2,000+ of the world's best products into DESIGN.md files" [post]
- `x-2093766772029559077#c2` (availability, stated) Free library hosted at styles.refero.design for Codex and Claude Code. — evidence: "The library is currently free to use:
https://styles.refero.design/" [post]
- `x-2093766772029559077#c3` (capability, demonstrated) Refero Linear record is a JSON designSystem (16 colors, 12 components, Agent Prompt Guide), not a downloadable DESIGN.md file. — evidence: "GET /api/styles/90ce5883-bb24-4466-93f7-801cd617b0d1 HTTP 200, 81180 bytes; fullResult.designSystem has dos/donts/colors/components/customSections; no .md attachment." [note]
- `x-2093766772029559077#c4` (counter-claim, demonstrated) Live paged GET /api/styles (styles[] key) still returns 1,289 unique style ids / 1,241 unique siteNames (20/page through page 64, 10 on page 65, empty page 66). Marketing 2,000+ stays above this public API. Records are gallery JSON, not a DESIGN.md tree. — evidence: "pages 1–65; empty page 66 {"styles":[],"nextCursor":null}. analysis/_work/captures/2026-09-05-refero-recount.json" [note]
**Numbers.** Linear designSystem HTTP body: 81180 bytes (note); public API unique style ids: 1289  (note)
**Recipe.** —
**Techniques.** —
**Tools.** [styles-refero-design](../../tools/styles-refero-design.md)
**Links.** product (https://styles.refero.design/)
**Related items.** [web-styles-refero-design](../web-styles-refero-design/card.md)
**Media.**
`raw/items/x-2093766772029559077/media/media_0.jpg` (image, carries_technique=false) — Screen recording demo of browsing Refero DESIGN.md files and applying design tokens (file stored as media_0.jpg but is MP4).
**Thread.** captured_partial · reported 28 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [web-styles-refero-design](../web-styles-refero-design/card.md), [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md)
