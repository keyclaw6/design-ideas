#!/usr/bin/env python3
"""Sanity-check catalog taxonomy and index consistency."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "raw" / "items"
NOTES = ROOT / "raw" / "notes"
CATALOG = ROOT / "catalog"

SCHEMA_TOPICS = {
    "bess-3d-flythrough", "gaussian-splatting", "camera-control", "three-js",
    "seo-agents", "keyboard-pcb", "design", "video-generation", "agent-skills",
    "ui-motion", "mcp", "infographics",
}


def main() -> int:
    errors = []
    uncategorized = []
    bad_topics = []
    filtered = 0
    kept = 0

    for p in sorted(ITEMS.glob("*/source.json")):
        d = json.loads(p.read_text())
        eid = d["id"]
        is_filtered = bool(d.get("extra", {}).get("filtered"))
        topics = d.get("topics", [])
        if is_filtered:
            filtered += 1
            if topics:
                errors.append(f"{eid}: filtered but has topics {topics}")
            continue
        kept += 1
        if not topics:
            uncategorized.append(eid)
        for t in topics:
            if t not in SCHEMA_TOPICS:
                bad_topics.append((eid, t))

    for p in sorted(NOTES.glob("*.md")):
        meta = p.with_suffix(".meta.json")
        if not meta.exists():
            errors.append(f"note {p.name}: missing {meta.name}")

    for name in ("README.md", "index.md", "patterns.md", "filtered.md", "PLAN.md"):
        if not (CATALOG / name).exists():
            errors.append(f"missing catalog/{name}")

    for t in SCHEMA_TOPICS:
        topic_file = CATALOG / "topics" / f"{t}.md"
        if not topic_file.exists():
            errors.append(f"missing catalog/topics/{t}.md")
        elif "<!-- AUTO:ITEMS -->" not in topic_file.read_text():
            errors.append(f"{topic_file}: missing AUTO:ITEMS marker")

    if uncategorized:
        errors.append(f"{len(uncategorized)} items without topics (e.g. {uncategorized[0]})")
    if bad_topics:
        errors.append(f"invalid topic slugs: {bad_topics[:3]}")

    # Rebuild should be a no-op on index row count
    before = (CATALOG / "index.md").read_text().count("\n| ")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "rebuild_catalog.py")], check=True)
    after = (CATALOG / "index.md").read_text().count("\n| ")
    if before != after:
        errors.append(f"index row count changed after rebuild: {before} -> {after}")

    print(f"kept={kept} filtered={filtered} notes={len(list(NOTES.glob('*.md')))}")
    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: catalog structure valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
