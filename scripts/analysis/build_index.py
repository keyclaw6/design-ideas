#!/usr/bin/env python3
"""Build analysis/index.jsonl from cards and threads."""

from __future__ import annotations

import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
ITEMS_DIR = WORKSPACE / "analysis" / "items"
INDEX_PATH = WORKSPACE / "analysis" / "index.jsonl"


def load_card(item_dir: Path) -> dict | None:
    card_path = item_dir / "card.json"
    if not card_path.is_file():
        return None
    return json.loads(card_path.read_text(encoding="utf-8"))


def load_thread(item_dir: Path) -> dict | None:
    thread_path = item_dir / "thread.json"
    if not thread_path.is_file():
        return None
    return json.loads(thread_path.read_text(encoding="utf-8"))


def thread_projection(item_id: str, thread: dict | None) -> dict | None:
    if not item_id.startswith("x-"):
        return None
    if thread is None:
        return {
            "status": None,
            "author_thread_status": None,
            "reply_count_reported": None,
            "replies_captured": None,
            "replies_relevant": None,
        }
    return {
        "status": thread.get("status"),
        "author_thread_status": thread.get("author_thread_status"),
        "reply_count_reported": thread.get("reply_count_reported"),
        "replies_captured": thread.get("replies_captured"),
        "replies_relevant": thread.get("replies_relevant"),
    }


def media_counts(card: dict) -> tuple[int, int]:
    media = card.get("media") or []
    count = len(media)
    described = 0
    for m in media:
        desc = m.get("description")
        if desc and len(desc) >= 20:
            described += 1
    return count, described


def build_index_record(item_id: str, card: dict, thread: dict | None) -> dict:
    claims = card.get("claims") or []
    media_count, media_described = media_counts(card)
    author = card.get("author") or {}
    jh = card.get("judge_hints") or {}
    raw = card.get("raw") or {}
    return {
        "id": item_id,
        "source_type": card.get("source_type"),
        "url": card.get("url"),
        "title": card.get("title"),
        "author.handle": author.get("handle"),
        "published_at": card.get("published_at"),
        "lang": card.get("lang"),
        "disposition": card.get("disposition"),
        "shelf": card.get("shelf"),
        "shelf_reason_code": card.get("shelf_reason_code"),
        "duplicate_of": card.get("duplicate_of"),
        "primary_subject": card.get("primary_subject"),
        "secondary_subjects": card.get("secondary_subjects"),
        "roles": card.get("roles"),
        "artifact_type": card.get("artifact_type"),
        "platforms": card.get("platforms"),
        "summary": card.get("summary"),
        "question_it_answers": card.get("question_it_answers"),
        "claim_count": len(claims),
        "claim_ids": [c.get("id") for c in claims],
        "techniques": card.get("techniques"),
        "tools": card.get("tools"),
        "thread": thread_projection(item_id, thread),
        "media_count": media_count,
        "media_described_count": media_described,
        "readiness": card.get("readiness"),
        "gaps": card.get("gaps"),
        "judge_hints.must_read": jh.get("must_read"),
        "judge_hints.compare_with": jh.get("compare_with"),
        "paths": {
            "card": f"analysis/items/{item_id}/card.md",
            "card_json": f"analysis/items/{item_id}/card.json",
            "thread_json": f"analysis/items/{item_id}/thread.json" if item_id.startswith("x-") else None,
            "raw_folder": raw.get("folder", f"raw/items/{item_id}"),
        },
        "legacy": {
            "topics": raw.get("legacy_topics", []),
            "filtered": raw.get("legacy_filtered", False),
        },
    }


def collect_item_dirs() -> list[Path]:
    if not ITEMS_DIR.is_dir():
        return []
    return sorted(p for p in ITEMS_DIR.iterdir() if p.is_dir())


def main() -> int:
    records = []
    for item_dir in collect_item_dirs():
        item_id = item_dir.name
        card = load_card(item_dir)
        if card is None:
            continue
        thread = load_thread(item_dir) if item_id.startswith("x-") else None
        records.append(build_index_record(item_id, card, thread))

    records.sort(key=lambda r: r["id"])
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records) + ("\n" if records else ""),
        encoding="utf-8",
    )
    print(f"wrote {len(records)} lines to {INDEX_PATH.relative_to(WORKSPACE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
