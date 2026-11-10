# Schema (v2 — single verbatim file, 2026-09-21)

## Item folders

Each captured bookmark or URL lives under:

```
raw/items/<id>/
├── content.md     # SINGLE readable file — verbatim snapshot, no summary
├── source.json    # required metadata (machine index for catalog rebuild)
└── media/         # local images/video/audio, referenced relatively
```

One folder per saved URL. One markdown file per folder. `content.md` holds the
original link plus the full original post/article as-is, local media embeds,
author thread/pinned items, and relevant comments from others — verbatim, no
paraphrase, no synthesis. An agent opens `content.md` and sees what was saved
without hitting X or the web.

## content.md

Sections in order; omit empty ones, never invent content:

1. `# <title>` (from `source.json` title, verbatim)
2. `> Source: <url>` + author + posted date + stats-at-capture if known
   (facts, not synthesis)
3. `## Post` or `## Article` — full original text, untruncated
4. `## Media` — local embeds `![](media/...)` (video: `[media/f](media/f)`)
   + original media URL for provenance
5. `## Thread` — author self-replies / pinned, verbatim with author + link
6. `## Comments` — relevant replies verbatim with author + link, no paraphrase
7. `## Links` — `related_urls` verbatim list

Rules: verbatim only — no summaries, no "what they are doing", no open
questions. Images/video live in `media/` and are embedded relatively; never
hotlink-only. Legacy `post.md` / `page.md` / `comments.md` / `research.md`
were merged into `content.md` and deleted (v2 migration 2026-09-21).

Reddit items use folder id `reddit-<post_id>` (base36 or full id from URL).

## source.json

```json
{
  "id": "string",
  "url": "string",
  "source_type": "github | website | x | reddit | note",
  "captured_at": "ISO-8601 datetime",
  "title": "string",
  "authors": ["string"],
  "topics": ["topic-slug"],
  "related_urls": ["string"],
  "media": ["relative/path/under/media/"],
  "unsaved": false,
  "extra": {}
}
```

| Field | Notes |
|-------|-------|
| `id` | Stable slug; matches folder name under `raw/items/` |
| `source_type` | Origin platform |
| `captured_at` | When the capture was taken |
| `topics` | Non-exclusive tags — see topic list below |
| `unsaved` | **X / Reddit only** — `true` after bookmark/save removed on platform |
| `unliked` | **X only** — `true` after like removed on X (set when harvesting Likes tab) |
| `extra` | Platform-specific fields (tweet id, repo stars, etc.) |

## Topics (non-exclusive)

`bess-3d-flythrough`, `gaussian-splatting`, `camera-control`, `three-js`, `seo-agents`, `keyboard-pcb`, `design`, `video-generation`, `agent-skills`, `ui-motion`, `mcp`, `infographics`, `general-reference`

Use `general-reference` for saved material outside the specialist lanes, such as
desktop utilities, general computing, and personal reference. Keep these captures
in the catalog; a saved item does not need to fit a design topic to be archived.

## Notes (pre-item research)

Long-form reports that have not been split into item folders live under `raw/notes/`. Optional sidecar `raw/notes/<name>.meta.json` sets `title` and `topics[]` for catalog indexing:

```json
{
  "id": "note-example",
  "title": "Human title",
  "topics": ["bess-3d-flythrough", "video-generation"]
}
```

Listed in `catalog/index.md` with paths under `raw/notes/` instead of `raw/items/<id>/`.

## Catalog

- `catalog/index.md` — master table: id, title, topics, path
- `catalog/filtered.md` — filtered items with reasons (auto-generated)
- `catalog/topics/<topic>.md` — curated slices per topic
- `catalog/patterns.md` — cross-cutting patterns (filled after harvest)
