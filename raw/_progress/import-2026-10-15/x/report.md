# X bookmark harvest and unsave report — 2026-10-15

Captured the complete currently saved bookmark list for `KristianBi25423` with read-only access. Two independent authenticated scans returned the same 126 unique tweet IDs. Pagination reached 40, 40, 40, 6, then an empty page with a repeated terminal cursor; the scan remained below the 1,000-item cap. Evidence and raw records are in this directory (`bookmarks-export.json`, `pagination-evidence.json`, `pagination-evidence.md`, and `inventory.json`). The initial capture phase did not modify the lists; the completed unsave phase is documented below. Likes were not changed.

All 126 saved IDs now map to `raw/items/` paths in `inventory.json`: 125 new captures and one existing alias at `raw/items/x-humanize-prompt-2107787922204152156/`. Every item has `content.md` and `source.json`; each initially recorded `unsaved: false`; completed unsaves now record `unsaved: true` and `extra.unsaved_at`. Saved post text and quoted-post text use FxTwitter's expanded text fields, with the original raw post text also retained in source metadata. Main-post media, article cover/content media and captured thread/reply media are downloaded locally. Local media references and declared media paths currently resolve across all 126 items.

The new captures contain 19 complete X Article bodies (10 direct and 9 quoted), covering 3,085 content blocks. The existing alias retains its prior article body and media. Its source metadata includes the X Article's `https://distribb.io/?utm_source=xarticle-oct7` link.

Thread data was available for 124 saved posts, with 3,281 reply records captured. Fifty-seven saved posts had reply counters higher than the returned context-record count; these are identified as partial in `report.json` and per-item metadata. For saved post `2102047124321939906`, the authenticated thread request returned HTTP 429. Its parent post (`2102025492840739175`), the full linked Nectiv article, and both associated images were recovered and saved locally. Other replies/comments for that item remain unavailable.

Media download failures and unresolved media gaps are zero. The 126 saved items reference 685 local media files (683 new files plus 2 reused existing files), totaling 2,362,837,920 bytes. Two videos exceed 100 MB (163,704,471 and 195,633,894 bytes); both are complete locally, linked from their captures, declared in metadata, and excluded from Git. Their exact downloaded sizes were verified.

A diagnostic command accidentally displayed two credential config lines in tool output during the session; no credential values were written into repository outputs. A byte-for-byte scan of all owned Markdown, JSON, and progress files against the configured `twitter_auth_token` and `twitter_ct0` values found zero matches.

Root reviewed all 126 topic mappings; see `topics-reviewed.json`. A separate review moved 387 records into “Other returned timeline records” because the normalized CLI response did not expose reply relationships and those records lacked a reply mention. This preserves recommendations/promoted material as source context without presenting it as a verified reply. All text and local media were retained; see `timeline-record-review.json`.

## Completed unsave phase

A fresh scan found four additional bookmarks after the initial 126-item capture. All four were fully archived first, including one 85-block Article and the complete 10-tool author thread; see [additional-captures.json](additional-captures.json). The final verified scope was 130 bookmarks, 129 new captures plus one existing capture, with 703 local media files and 21 Articles including the existing Article.

All 130 bookmarks were removed through authenticated `DeleteBookmark` operations. A fresh terminal listing returned zero entries. The root agent independently reverified the account and empty saved list. Every matching `source.json` now records canonical `unsaved: true` and `extra.unsaved_at`. Per-ID outcomes and final pagination are in [unsave-ledger.json](unsave-ledger.json); the independent check is in [unsave-root-verification.json](unsave-root-verification.json).
