#!/usr/bin/env python3
"""Assign analysis unit ids to batches (round-robin)."""

import argparse
import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
RAW_ITEMS = WORKSPACE / "raw" / "items"
RAW_NOTES = WORKSPACE / "raw" / "notes"
OUT_PATH = WORKSPACE / "analysis" / "_work" / "batches.json"


def collect_ids() -> list[str]:
    ids: list[str] = []
    if RAW_ITEMS.is_dir():
        for entry in sorted(RAW_ITEMS.iterdir()):
            if entry.is_dir():
                ids.append(entry.name)
    if RAW_NOTES.is_dir():
        for path in sorted(RAW_NOTES.glob("*.md")):
            ids.append(f"note-{path.stem}")
    return sorted(ids)


def assign_batches(ids: list[str], n: int) -> dict[str, int]:
    assignment: dict[str, int] = {}
    for i, item_id in enumerate(ids):
        assignment[item_id] = (i % n) + 1
    return assignment


def main() -> int:
    parser = argparse.ArgumentParser(description="Assign analysis ids to batches.")
    parser.add_argument("--batches", type=int, required=True, help="Number of batches (1-based)")
    args = parser.parse_args()
    if args.batches < 1:
        print("error: --batches must be >= 1", file=sys.stderr)
        return 1

    ids = collect_ids()
    assignment = assign_batches(ids, args.batches)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"batches": args.batches, "assignment": assignment}
    OUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    x_count = sum(1 for i in ids if i.startswith("x-"))
    batch_sizes: dict[int, int] = {}
    batch_x: dict[int, int] = {}
    for item_id, batch in assignment.items():
        batch_sizes[batch] = batch_sizes.get(batch, 0) + 1
        if item_id.startswith("x-"):
            batch_x[batch] = batch_x.get(batch, 0) + 1

    print(f"total_ids={len(ids)}")
    print(f"x_ids={x_count}")
    print(f"batches={args.batches}")
    for b in sorted(batch_sizes):
        print(f"batch_{b:02d}: total={batch_sizes[b]} x={batch_x.get(b, 0)}")
    print(f"wrote {OUT_PATH.relative_to(WORKSPACE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
