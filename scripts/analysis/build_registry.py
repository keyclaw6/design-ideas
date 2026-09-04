#!/usr/bin/env python3
"""Build registry JSONL from cards; apply aliases."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
ITEMS_DIR = WORKSPACE / "analysis" / "items"
REGISTRY_DIR = WORKSPACE / "analysis" / "registry"
ALIASES_PATH = REGISTRY_DIR / "aliases.json"
TOOLS_PATH = REGISTRY_DIR / "tools.jsonl"
TECHNIQUES_PATH = REGISTRY_DIR / "techniques.jsonl"


def load_aliases() -> dict[str, str]:
    if not ALIASES_PATH.is_file():
        return {}
    data = json.loads(ALIASES_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    return {str(k): str(v) for k, v in data.items()}


def apply_alias(slug: str, aliases: dict[str, str]) -> str:
    seen: set[str] = set()
    current = slug
    while current in aliases:
        if current in seen:
            break
        seen.add(current)
        current = aliases[current]
    return current


def slug_to_name(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def infer_tool_kind(card: dict) -> str:
    artifact = card.get("artifact_type", "")
    source = card.get("source_type", "")
    if artifact == "repo" or source == "github":
        return "repo"
    if artifact == "product":
        return "product"
    if artifact in ("paper", "article"):
        return "library"
    if artifact == "dataset":
        return "library"
    if source == "website" and artifact in ("demo-video", "demo-image", "announcement"):
        return "service"
    if "api" in slug_to_name(card.get("id", "")).lower():
        return "api"
    return "product"


def collect_cards() -> list[tuple[str, dict]]:
    cards: list[tuple[str, dict]] = []
    if not ITEMS_DIR.is_dir():
        return cards
    for item_dir in sorted(ITEMS_DIR.iterdir()):
        card_path = item_dir / "card.json"
        if card_path.is_file():
            cards.append((item_dir.name, json.loads(card_path.read_text(encoding="utf-8"))))
    return cards


def rewrite_card_slugs(card_path: Path, aliases: dict[str, str]) -> bool:
    card = json.loads(card_path.read_text(encoding="utf-8"))
    changed = False
    for field in ("tools", "techniques"):
        slugs = card.get(field) or []
        new_slugs = []
        for s in slugs:
            ns = apply_alias(s, aliases)
            new_slugs.append(ns)
            if ns != s:
                changed = True
        if new_slugs != slugs:
            card[field] = new_slugs
            changed = True
    if changed:
        card_path.write_text(json.dumps(card, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def pick_canonical_item(slug: str, item_refs: list[tuple[str, dict]]) -> str | None:
    github = [iid for iid, c in item_refs if c.get("disposition") == "analyze" and iid.startswith("github-")]
    if github:
        return sorted(github)[0]
    analyze = [iid for iid, c in item_refs if c.get("disposition") == "analyze"]
    if analyze:
        return sorted(analyze)[0]
    return sorted(item_refs, key=lambda x: x[0])[0][0] if item_refs else None


def main() -> int:
    aliases = load_aliases()
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    rewritten = 0
    for item_dir in sorted(ITEMS_DIR.iterdir()) if ITEMS_DIR.is_dir() else []:
        card_path = item_dir / "card.json"
        if card_path.is_file() and rewrite_card_slugs(card_path, aliases):
            rewritten += 1

    cards = collect_cards()

    tool_items: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    technique_items: dict[str, list[tuple[str, dict]]] = defaultdict(list)

    for item_id, card in cards:
        if card.get("disposition") != "analyze":
            continue
        subjects = []
        if card.get("primary_subject"):
            subjects.append(card["primary_subject"])
        subjects.extend(card.get("secondary_subjects") or [])
        subjects = sorted(set(subjects))
        worker = card.get("worker", "")
        for raw_slug in card.get("tools") or []:
            slug = apply_alias(raw_slug, aliases)
            tool_items[slug].append((item_id, card))
        for raw_slug in card.get("techniques") or []:
            slug = apply_alias(raw_slug, aliases)
            technique_items[slug].append((item_id, card))

    tools_records = []
    for slug in sorted(tool_items):
        refs = tool_items[slug]
        item_ids = sorted({iid for iid, _ in refs})
        subjects: set[str] = set()
        first_worker = ""
        canonical_item = pick_canonical_item(slug, refs)
        canonical_card = next(c for iid, c in refs if iid == canonical_item) if canonical_item else refs[0][1]
        for iid, c in refs:
            if c.get("primary_subject"):
                subjects.add(c["primary_subject"])
            subjects.update(c.get("secondary_subjects") or [])
            if not first_worker:
                first_worker = c.get("worker", "")
        kind = infer_tool_kind(canonical_card)
        links = canonical_card.get("links") or {}
        canonical_url = links.get("canonical") or links.get("repo") or links.get("product") or canonical_card.get("url")
        tools_records.append({
            "slug": slug,
            "name": slug_to_name(slug),
            "kind": kind,
            "canonical_url": canonical_url,
            "canonical_item": canonical_item,
            "item_ids": item_ids,
            "subjects": sorted(subjects),
            "first_seen_worker": first_worker,
        })

    technique_records = []
    for slug in sorted(technique_items):
        refs = technique_items[slug]
        item_ids = sorted({iid for iid, _ in refs})
        subject_counts: dict[str, int] = defaultdict(int)
        for iid, c in refs:
            ps = c.get("primary_subject")
            if ps:
                subject_counts[ps] += 1
            for s in c.get("secondary_subjects") or []:
                subject_counts[s] += 1
        if subject_counts:
            max_count = max(subject_counts.values())
            candidates = sorted(s for s, n in subject_counts.items() if n == max_count)
            owner_subject = candidates[0]
        else:
            owner_subject = ""
        technique_records.append({
            "slug": slug,
            "name": slug_to_name(slug),
            "item_ids": item_ids,
            "subjects": sorted(subject_counts.keys()),
            "owner_subject": owner_subject,
            "singleton": len(item_ids) == 1,
        })

    TOOLS_PATH.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in tools_records) + ("\n" if tools_records else ""),
        encoding="utf-8",
    )
    TECHNIQUES_PATH.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in technique_records) + ("\n" if technique_records else ""),
        encoding="utf-8",
    )

    print(f"cards={len(cards)} rewritten={rewritten} tools={len(tools_records)} techniques={len(technique_records)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
