# Orchestration

## Wave 1 — done

| Lane | Agent | Status | Notes |
|------|-------|--------|-------|
| Skeleton + note ingest | executor | done | KB skeleton, SCHEMA, AGENTS, blender note copied |
| URL ingest | executor | done | 35 items + blender note |
| Item harvest | — | pending | X bookmarks → `raw/items/` |
| Topic slices | — | pending | `catalog/topics/*.md` |
| Patterns | — | pending | `catalog/patterns.md` after harvest |

## Wave 2 — in progress

| Lane | Agent | Status | Notes |
|------|-------|--------|-------|
| X bookmarks capture | parent | done | 33 x items on disk; all unsaved on X |
| Follow-on URLs | ingest | done | capture-1–9 follow-ons ingested |
| Catalog | rebuild | done | 110 entries; patterns.md filled |

## Blockers

- Bookmarks infinite scroll often sticks (~5 visible cards). Unsave captured batch then reload to reveal next IDs.
- `cursor-ide-browser` MCP drops; reconnect via `browser_tabs` list.

## Wave 1 catalog rebuild — done

Executor rebuilt `catalog/index.md` (36 entries: 19 github, 16 website, 1 note) and 10 topic slices under `catalog/topics/`. No x-* items included (none complete). Topics with zero items omitted: gaussian-splatting, keyboard-pcb.

## Catalog rebuild — done (2026-09-02)

Executor rebuilt from disk: 69 entries (23 github, 27 website, 18 x, 1 note); 12 topic slices.

## Catalog rebuild — done (2026-09-02, capture-7 + follow-ons)

Rebuilt from disk: **84 entries** (25 github, 35 website, 23 x, 1 note); 12 topic slices. +15 since prior rebuild (5 capture-7 x posts + 10 follow-on URLs). X unsaved: 20 true / 3 false.

## Catalog rebuild — done (2026-09-02, capture-8 + follow-ons)

Rebuilt from disk: **98 entries** (26 github, 43 website, 28 x, 1 note); 12 topic slices. **+14** since prior rebuild (5 capture-8 x posts + 9 follow-on URLs). X unsaved: 28 true / 0 false.

## After catalog (parent)

- Capture-6 five posts unsaved on X; `source.json` `unsaved: true`.
- Next Bookmarks batch (5): pmitu, hridoyreh Brave, codyschneider, jakezward, pierreeliottlal — capture-7 in flight; do not unsave until disk verify.
- Graphify CLI installed (`uv tool install graphifyy` 0.9.53) + `.cursor/rules/graphify.mdc`. Corpus graph **not** built yet.

## Catalog rebuild — done (2026-09-03, capture-9 + follow-ons)

Rebuilt from disk: **110 entries** (26 github, 50 website, 33 x, 1 note); 12 topic slices. **+12** since prior rebuild (5 capture-9 x posts + 7 follow-on URLs). X unsaved: 33 true / 0 false. `catalog/patterns.md` filled from harvest research.
