#!/usr/bin/env python3
"""Rebuild catalog/index.md and item lists in catalog/topics/*.md from raw/items."""
import json, glob, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "raw" / "items"
NOTES = ROOT / "raw" / "notes"
CATALOG = ROOT / "catalog"
TOPICS_DIR = CATALOG / "topics"

AUTO_START = "<!-- AUTO:ITEMS -->"
AUTO_END = "<!-- /AUTO:ITEMS -->"

SCHEMA_TOPICS = [
    "bess-3d-flythrough", "gaussian-splatting", "camera-control", "three-js",
    "seo-agents", "keyboard-pcb", "design", "video-generation", "agent-skills",
    "ui-motion", "mcp", "infographics",
]


def load_item(path: Path) -> dict:
    d = json.loads(path.read_text())
    eid = d["id"]
    unsaved = d.get("unsaved", False) if d.get("source_type") in ("x", "reddit") else False
    filtered = bool(d.get("extra", {}).get("filtered"))
    return {
        "id": eid,
        "title": d.get("title", eid),
        "source_type": d["source_type"],
        "topics": d.get("topics", []),
        "unsaved": unsaved,
        "filtered": filtered,
        "path": f"raw/items/{eid}/",
    }


def load_entries():
    entries = []
    for p in sorted(glob.glob(str(ITEMS / "*/source.json"))):
        entries.append(load_item(Path(p)))
    for p in sorted(glob.glob(str(NOTES / "*.md"))):
        name = Path(p).stem
        entries.append({
            "id": f"note-{name}",
            "title": name.replace("-", " ").title(),
            "source_type": "note",
            "topics": [],
            "unsaved": False,
            "filtered": False,
            "path": f"raw/notes/{Path(p).name}",
        })
    return sorted(entries, key=lambda x: x["id"])


def write_index(entries):
    lines = [
        "# Catalog index",
        "",
        "Master table of all entries. Start at [README.md](README.md) for taxonomy and query order.",
        "",
        "| id | title | source_type | topics | filtered | unsaved | path |",
        "|----|-------|-------------|--------|----------|---------|------|",
    ]
    for e in entries:
        topics = ", ".join(e["topics"]) if e["topics"] else ""
        uns = "true" if e["unsaved"] else "false"
        flt = "true" if e["filtered"] else "false"
        title = e["title"].replace("|", "\\|")
        lines.append(
            f"| {e['id']} | {title} | {e['source_type']} | {topics} | {flt} | {uns} | {e['path']} |"
        )
    (CATALOG / "index.md").write_text("\n".join(lines) + "\n")


def render_item_list(items: list[dict]) -> str:
    lines = []
    for e in sorted(items, key=lambda x: x["id"]):
        rel = f"../../{e['path']}"
        flt = " *(filtered)*" if e["filtered"] else ""
        lines.append(f"- [{e['title']}]({rel}) — `{e['id']}`{flt}")
    return "\n".join(lines) + "\n"


def patch_topic_file(topic: str, item_block: str):
    path = TOPICS_DIR / f"{topic}.md"
    title = topic.replace("-", " ").title()
    if path.exists():
        text = path.read_text()
        if AUTO_START in text and AUTO_END in text:
            new_text = re.sub(
                rf"{re.escape(AUTO_START)}.*?{re.escape(AUTO_END)}",
                f"{AUTO_START}\n{item_block}{AUTO_END}",
                text,
                flags=re.DOTALL,
            )
            path.write_text(new_text)
            return
        # Preserve existing brief; append auto section
        path.write_text(
            text.rstrip()
            + f"\n\n## All items\n\n{AUTO_START}\n{item_block}{AUTO_END}\n"
        )
        return
    # New topic file — minimal stub until brief worker fills it
    path.write_text(
        f"# {title}\n\n"
        f"Topic slug: `{topic}`. Brief pending — see [README.md](../README.md).\n\n"
        f"## All items\n\n{AUTO_START}\n{item_block}{AUTO_END}\n"
    )


def write_topic_lists(entries):
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
            if p.exists() and AUTO_START not in p.read_text():
                continue  # keep hand-written empty-topic stub
            if p.exists():
                p.unlink()
            continue
        patch_topic_file(t, render_item_list(items))


if __name__ == "__main__":
    entries = load_entries()
    write_index(entries)
    write_topic_lists(entries)
    from collections import Counter

    c = Counter(e["source_type"] for e in entries)
    filtered = sum(1 for e in entries if e["filtered"])
    print(f"Rebuilt {len(entries)} entries ({filtered} filtered):", dict(c))
