# Schema

## Item folders

Each captured bookmark or URL lives under:

```
raw/items/<id>/
├── source.json      # required metadata
├── page.md          # website/github content (or post.md for X posts)
├── comments.md      # optional — thread replies, discussion
├── research.md      # agent synthesis, follow-ups, open questions
└── media/           # screenshots, downloads, attachments
```

Use `post.md` instead of `page.md` when `source_type` is `x` or `reddit`.

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

`bess-3d-flythrough`, `gaussian-splatting`, `camera-control`, `three-js`, `seo-agents`, `keyboard-pcb`, `design`, `video-generation`, `agent-skills`, `ui-motion`, `mcp`, `infographics`

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
