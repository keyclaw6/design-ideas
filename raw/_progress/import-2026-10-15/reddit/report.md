# Reddit import report — 2026-10-15

## Outcome

Imported the authenticated account’s current Saved history into the Reddit archive. The live Reddit identity was `Strange_Tomatillo335`; the project’s earlier `kab264set` account note was stale, and that old saved-profile URL returned 404. The Saved list was read through Reddit’s authenticated read-only JSON endpoints. The initial capture phase preserved save state; the completed unsave phase is documented below. No votes or posts were made.

## Counts

- Saved entries: 38 (37 posts, 1 saved comment)
- Pagination: 1 page; 38 entries; terminal `after` is `null`; exhausted
- Unique entries mapped: 38
- New folders: 37
- Existing folder refreshed from the authenticated source: `reddit-1x3b9aa`
- Context comments captured: 1,666 comment records across the 38 thread captures, plus the separately preserved saved comment
- Reddit-hosted media: 56 local files, all referenced from `content.md` and `source.json`; unresolved media gaps: 0
- Reddit videos with source audio: 5 (`reddit-1x4vndw`, `reddit-1x4cvvw`, `reddit-1w4ljsx`, `reddit-1v4e576`, `reddit-1vvf7ou`), each merged and verified by ffprobe to contain video and audio streams; `reddit-1w0by3s` is correctly video-only because Reddit reports `has_audio=false`
- Local MP4 stream and duration evidence for all six videos: [evidence/audio-stream-audit.json](evidence/audio-stream-audit.json)
- Unexpanded Reddit `more` placeholders: 0 after expansion on all five affected threads

Fullnames, permalinks, folder mapping, and capture status are in [inventory.md](inventory.md). Saved-list terminal-page evidence is in [evidence/pagination.json](evidence/pagination.json). The sanitized comment-expansion counts are in [evidence/comments-expansion.json](evidence/comments-expansion.json). The independent final audit is recorded in [verification.json](../verification.json).

## Capture details and gaps

All 38 items include the full Reddit post body. The saved comment has its own `reddit-p3g4kte` folder, its exact comment text, author/date, and the parent post plus thread context. Each post capture includes every comment record returned by Reddit’s comments API; all explicit `more` placeholders were expanded and exhausted.

The Reddit `num_comments` counters exceed the comment records exposed by the API on some threads. The exact per-folder differences below are recorded as unavailable comment records; Reddit did not return those records after all explicit `more` placeholders were expanded, so no text was invented.

| Folder | Reddit comment counter | Context comment records captured | Saved comment captured separately | Difference not exposed |
|---|---:|---:|---:|---:|
| `reddit-1u13158` | 59 | 50 | 0 | 9 |
| `reddit-1uxaxg8` | 21 | 20 | 0 | 1 |
| `reddit-1v8ep5r` | 104 | 101 | 0 | 3 |
| `reddit-1v8mop3` | 18 | 17 | 0 | 1 |
| `reddit-1vht9fa` | 26 | 22 | 0 | 4 |
| `reddit-1vv5wel` | 83 | 67 | 0 | 16 |
| `reddit-1vvf7ou` | 90 | 88 | 0 | 2 |
| `reddit-1vxx51g` | 83 | 82 | 0 | 1 |
| `reddit-1vzg2e2` | 29 | 26 | 0 | 3 |
| `reddit-1w0by3s` | 56 | 54 | 0 | 2 |
| `reddit-1w0swod` | 87 | 79 | 0 | 8 |
| `reddit-1w32gzj` | 17 | 14 | 0 | 3 |
| `reddit-1w37d9y` | 18 | 16 | 0 | 2 |
| `reddit-1w4ljsx` | 20 | 19 | 0 | 1 |
| `reddit-1wgu40p` | 101 | 96 | 0 | 5 |
| `reddit-1wilp6x` | 239 | 190 | 0 | 49 |
| `reddit-1wp4i6k` | 43 | 42 | 0 | 1 |
| `reddit-1wwi9uz` | 177 | 165 | 0 | 12 |
| `reddit-1wydtmj` | 15 | 14 | 0 | 1 |
| `reddit-1x03yw4` | 19 | 16 | 0 | 3 |
| `reddit-1x3b9aa` | 22 | 21 | 0 | 1 |
| `reddit-1x48dxc` | 221 | 204 | 0 | 17 |
| `reddit-1x4ab4r` | 10 | 9 | 0 | 1 |
| `reddit-1x4cvvw` | 47 | 46 | 0 | 1 |
| `reddit-1x4vndw` | 63 | 58 | 0 | 5 |
| `reddit-p3g4kte` | 26 | 23 | 1 | 2 |

One image URL for `reddit-1ujr89i` returned 404 without a file suffix. The `.png` variant returned `image/png` and is now captured locally; it is not an unresolved gap.

Root reviewed the topic tags for all 38 items. General saved references use `general-reference`; no item was filtered out based on topic.

## Completed unsave phase

All 38 saved entries were removed after their captures were verified, including the saved comment as `t1_p3g4kte` rather than its parent post. Reddit rate-limited the action after 32 removals; after a five-minute cooldown the remaining six were unsaved successfully. Fresh complete pagination returned zero entries with `after: null`. The root agent independently confirmed the account and empty Saved list. All 38 source files now record canonical `unsaved: true` and `extra.unsaved_at`. See [unsave-ledger.json](unsave-ledger.json) and [unsave-root-verification.json](unsave-root-verification.json).
