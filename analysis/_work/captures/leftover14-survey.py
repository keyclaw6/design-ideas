#!/usr/bin/env python3
"""List analyze ready-with-gaps cards with no note claim."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/workspace/analysis/items")
rows = []
for card_path in sorted(ROOT.glob("*/card.json")):
    c = json.loads(card_path.read_text())
    if c.get("disposition") != "analyze":
        continue
    if c.get("readiness") != "ready-with-gaps":
        continue
    claims = c.get("claims") or []
    has_note = any(cl.get("evidence_source") == "note" for cl in claims)
    must = bool((c.get("judge_hints") or {}).get("must_read"))
    rows.append(
        {
            "id": c["id"],
            "subject": c.get("primary_subject"),
            "must_read": must,
            "has_note": has_note,
            "gaps": c.get("gaps") or [],
            "title": (c.get("title") or "")[:90],
            "n_claims": len(claims),
        }
    )

empty = [r for r in rows if not r["has_note"]]
must = [r for r in rows if r["must_read"]]
print(f"ready-with-gaps analyze: {len(rows)}")
print(f"no note claim: {len(empty)}")
print(f"must-read still gaps: {len(must)}")
print("\n=== empty-no-note ===")
for r in empty:
    print(f"{r['id']}\t{r['subject']}\tmust={r['must_read']}\tgaps={r['gaps']}\t{r['title']}")
print("\n=== must-read still gaps ===")
for r in must:
    print(f"{r['id']}\t{r['subject']}\thas_note={r['has_note']}\tgaps={r['gaps']}\t{r['title']}")
