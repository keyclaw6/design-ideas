#!/usr/bin/env python3
"""Apply reclassification requests from analysis/_work/reclass/*.jsonl."""

from __future__ import annotations

import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
RECLASS_DIR = WORKSPACE / "analysis" / "_work" / "reclass"
REPORTS_DIR = WORKSPACE / "analysis" / "_work" / "reports"
ITEMS_DIR = WORKSPACE / "analysis" / "items"
CONFLICTS_PATH = REPORTS_DIR / "reclass-conflicts.md"

ALLOWED_FIELDS = {
    "primary_subject",
    "secondary_subjects",
    "disposition",
    "shelf",
    "shelf_reason_code",
    "shelf_reason",
    "duplicate_of",
    "judge_hints.must_read",
}


def load_records() -> list[dict]:
    records: list[dict] = []
    if not RECLASS_DIR.is_dir():
        return records
    for path in sorted(RECLASS_DIR.glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def get_nested(card: dict, field: str):
    if field == "judge_hints.must_read":
        return card.get("judge_hints", {}).get("must_read")
    return card.get(field)


def set_nested(card: dict, field: str, value) -> None:
    if field == "judge_hints.must_read":
        if "judge_hints" not in card or not isinstance(card["judge_hints"], dict):
            card["judge_hints"] = {"compare_with": [], "must_read": False, "why_must_read": None}
        card["judge_hints"]["must_read"] = value
    else:
        card[field] = value


def main() -> int:
    records = load_records()
    if not records:
        print("no reclass records")
        return 0

    # detect conflicts: same id+field, different to
    by_key: dict[tuple[str, str], list[dict]] = {}
    for rec in records:
        key = (rec["id"], rec["field"])
        by_key.setdefault(key, []).append(rec)

    conflicts: list[tuple[str, str, list[dict]]] = []
    applicable: list[dict] = []
    for key, group in by_key.items():
        to_values = {json.dumps(g["to"], sort_keys=True) for g in group}
        if len(to_values) > 1:
            conflicts.append((key[0], key[1], group))
        else:
            applicable.append(group[-1])

    if conflicts:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        lines = ["# Reclass conflicts\n", "\n"]
        for item_id, field, group in conflicts:
            lines.append(f"## {item_id} · {field}\n\n")
            for g in group:
                lines.append(
                    f"- from `{g.get('from')}` to `{g.get('to')}` by `{g.get('by')}`: {g.get('why', '')}\n"
                )
            lines.append("\n")
        CONFLICTS_PATH.write_text("".join(lines), encoding="utf-8")
        print(f"conflicts={len(conflicts)} written to {CONFLICTS_PATH.relative_to(WORKSPACE)}")

    applied = 0
    skipped = 0
    for rec in applicable:
        item_id = rec["id"]
        field = rec["field"]
        if field not in ALLOWED_FIELDS:
            print(f"skip {item_id}.{field}: field not allowed")
            skipped += 1
            continue
        card_path = ITEMS_DIR / item_id / "card.json"
        if not card_path.is_file():
            print(f"skip {item_id}: card.json missing")
            skipped += 1
            continue
        card = json.loads(card_path.read_text(encoding="utf-8"))
        current = get_nested(card, field)
        if json.dumps(current, sort_keys=True) != json.dumps(rec.get("from"), sort_keys=True):
            print(f"skip {item_id}.{field}: from mismatch (have {current!r})")
            skipped += 1
            continue
        set_nested(card, field, rec["to"])
        card_path.write_text(json.dumps(card, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        applied += 1

    print(f"applied={applied} skipped={skipped} conflicted={len(conflicts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
