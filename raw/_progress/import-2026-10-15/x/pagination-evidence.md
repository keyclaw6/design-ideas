# X bookmarks pagination evidence — 2026-10-15

- Authenticated identity verified with read-only `twitter whoami`: `KristianBi25423`.
- Two independent bookmark scans returned the same 126 unique tweet IDs. The SHA-256 of the sorted ID list in the raw export matches the independently paginated scan: `8c07110e4ce9b8e9e5a5e945186d96cb23e037a49f16f87fc35dfac4f6ca03fe`.
- Pagination instrumentation observed pages with 40, 40, 40, 6, then 0 new posts. The final cursor repeated on the empty page, the client stop condition. The scan stayed below its 1,000 item cap; the empty repeated-cursor page establishes the timeline's current boundary.
- Raw export: `bookmarks-export.json`; structured page evidence: `pagination-evidence.json`.
- No bookmark was removed, no like changed, and no X write operation was performed.
