# Card worker instructions

You write `analysis/items/<id>/card.json` for every id you own. Read `docs/ANALYSIS_STRUCTURE.md` §4.1, §4.5, §5.

## Procedure (fixed order, every item)

1. Read `analysis/subjects.json` (taxonomy).
2. Read `raw/items/<id>/source.json`, then `post.md` or `page.md`, then `comments.md`, then `thread.json` if present, then `research.md`.
3. Look at every image in `raw/items/<id>/media/` (Read the image). Describe what is visible.
4. Decide `disposition`: `analyze` or `shelf`. Re-judge legacy `extra.filtered` — do not copy it.
5. Write `card.json` with **every key** in §4.1. Absent optionals are `null`, never omitted.
6. Run `python3 scripts/analysis/validate_cards.py analysis/items/<id>` and fix until exit 0.
7. Do **not** write `card.md` or `thread.json`. Do not edit other batches. Do not `git add -A`.

## Hard rules

- `title` ≤ 90 chars, English, names the artifact/claim. For X posts the first 60 chars must **not** equal the first 60 chars of `post.md` body (no truncated tweet as title).
- `summary` 80–320 chars, what it IS and DOES, no hype adjectives from the post.
- If `analyze`: `primary_subject` from subjects.json, 1–3 `roles`, ≥1 claim, `question_it_answers` set, shelf fields null.
- If `shelf`: `shelf_reason` ≥ 60 chars naming something observable; banned: `see post.md`, `filtered noise`, `no matching topic`, `out of taxonomy`.
- Claims: id `<id>#c1`, `#c2`, …; `evidence` is a verbatim quote; `subject` is primary or a secondary.
- `media[]` one entry per file in `raw/items/<id>/media/` excluding `reply-*`. Images need `description` ≥ 20 chars or `skip_reason`.
- `raw.legacy_topics` = `source.json.topics`; `raw.legacy_filtered` = bool(extra.filtered).
- `worker` = your worker id (`cards-NN`). `schema_version` = `"1"`.
- `source_type`: `x-`→`x`, `github-`→`github`, `web-`→`website`, `note-`→`note`.
- Note item `note-blender-minimax-h3-video-generation` lives at `raw/notes/blender-minimax-h3-video-generation.md`.

## Seeds

If the id is in a subject's `seed_items`, that subject is the default primary unless the post is clearly noise/duplicate.

## Handoff

Write `analysis/_work/handoffs/<worker-id>.md`: ids owned, ids done, blocked/failed, alias proposals `{"from","to","why"}`, reclass proposals.

Commit only your `analysis/items/<id>/card.json` files plus your handoff:

```
git add analysis/items/<id>/card.json ... analysis/_work/handoffs/cards-NN.md
git commit -m "feat(cards-NN): analysis cards for batch NN"
```

Do not push unless asked. Do not spawn sub-agents.
