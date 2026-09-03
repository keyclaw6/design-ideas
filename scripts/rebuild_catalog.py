#!/usr/bin/env python3
"""Rebuild catalog/index.md and catalog/topics/*.md from raw/items and raw/notes."""
import json, glob, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "raw" / "items"
NOTES = ROOT / "raw" / "notes"
CATALOG = ROOT / "catalog"
TOPICS_DIR = CATALOG / "topics"

SCHEMA_TOPICS = [
    "bess-3d-flythrough", "gaussian-splatting", "camera-control", "three-js",
    "seo-agents", "keyboard-pcb", "design", "video-generation", "agent-skills",
    "ui-motion", "mcp", "infographics",
]

def load_entries():
    entries = []
    for p in sorted(glob.glob(str(ITEMS / "*/source.json"))):
        d = json.load(open(p))
        eid = d["id"]
        unsaved = d.get("unsaved", False) if d.get("source_type") in ("x", "reddit") else False
        entries.append({
            "id": eid,
            "title": d.get("title", eid),
            "source_type": d["source_type"],
            "topics": d.get("topics", []),
            "unsaved": unsaved,
            "path": f"raw/items/{eid}/",
        })
    for p in sorted(glob.glob(str(NOTES / "*.md"))):
        name = Path(p).stem
        entries.append({
            "id": f"note-{name}",
            "title": name.replace("-", " ").title(),
            "source_type": "note",
            "topics": [],
            "unsaved": False,
            "path": f"raw/notes/{Path(p).name}",
        })
    return sorted(entries, key=lambda x: x["id"])

def write_index(entries):
    lines = [
        "# Catalog index",
        "",
        "Master table of all entries. Start here when querying the library.",
        "",
        "| id | title | source_type | topics | unsaved | path |",
        "|----|-------|-------------|--------|---------|------|",
    ]
    for e in entries:
        topics = ", ".join(e["topics"]) if e["topics"] else ""
        uns = "true" if e["unsaved"] else "false"
        title = e["title"].replace("|", "\\|")
        lines.append(f"| {e['id']} | {title} | {e['source_type']} | {topics} | {uns} | {e['path']} |")
    (CATALOG / "index.md").write_text("\n".join(lines) + "\n")

def write_topics(entries):
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    by_topic = {t: [] for t in SCHEMA_TOPICS}
    for e in entries:
        for t in e["topics"]:
            if t in by_topic:
                by_topic[t].append(e)
    for t in SCHEMA_TOPICS:
        items = by_topic[t]
        if not items:
            p = TOPICS_DIR / f"{t}.md"
            if p.exists():
                p.unlink()
            continue
        title = t.replace("-", " ").title()
        lines = [f"# {title}", "", f"Curated slice — topic `{t}`.", ""]
        for e in items:
            rel = f"../../{e['path']}"
            lines.append(f"- [{e['title']}]({rel}) — `{e['id']}`")
        (TOPICS_DIR / f"{t}.md").write_text("\n".join(lines) + "\n")

if __name__ == "__main__":
    entries = load_entries()
    write_index(entries)
    write_topics(entries)
    from collections import Counter
    c = Counter(e["source_type"] for e in entries)
    print(f"Rebuilt {len(entries)} entries:", dict(c))
