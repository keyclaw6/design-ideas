#!/usr/bin/env python3
"""Render markdown and JSONL artifacts from analysis JSON."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
ITEMS_DIR = WORKSPACE / "analysis" / "items"
SUBJECTS_DIR = WORKSPACE / "analysis" / "subjects"
TOOLS_DIR = WORKSPACE / "analysis" / "tools"
TECHNIQUES_DIR = WORKSPACE / "analysis" / "techniques"
SHELF_DIR = WORKSPACE / "analysis" / "shelf"
REGISTRY_DIR = WORKSPACE / "analysis" / "registry"
INDEX_PATH = WORKSPACE / "analysis" / "index.jsonl"

NOTES_START = "<!-- NOTES:START -->"
NOTES_END = "<!-- NOTES:END -->"


def load_cards() -> dict[str, dict]:
    cards: dict[str, dict] = {}
    if not ITEMS_DIR.is_dir():
        return cards
    for item_dir in sorted(ITEMS_DIR.iterdir()):
        card_path = item_dir / "card.json"
        if card_path.is_file():
            cards[item_dir.name] = json.loads(card_path.read_text(encoding="utf-8"))
    return cards


def load_threads() -> dict[str, dict]:
    threads: dict[str, dict] = {}
    for item_id in load_cards():
        if not item_id.startswith("x-"):
            continue
        thread_path = ITEMS_DIR / item_id / "thread.json"
        if thread_path.is_file():
            threads[item_id] = json.loads(thread_path.read_text(encoding="utf-8"))
    return threads


def load_registry_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def extract_notes(content: str) -> str:
    if NOTES_START in content and NOTES_END in content:
        start = content.index(NOTES_START) + len(NOTES_START)
        end = content.index(NOTES_END)
        return content[start:end].strip("\n")
    return ""


def join_list(items: list, sep: str = ", ") -> str:
    if not items:
        return "—"
    return sep.join(str(i) for i in items)


def render_card_md(item_id: str, card: dict, thread: dict | None) -> str:
    title = card.get("title", "")
    source_type = card.get("source_type", "")
    artifact_type = card.get("artifact_type", "")
    lang = card.get("lang", "")
    url = card.get("url", "")
    author = card.get("author") or {}
    name = author.get("name") or "—"
    handle = author.get("handle") or "—"
    published = card.get("published_at") or "—"
    captured = card.get("captured_at", "")
    disposition = card.get("disposition", "")
    shelf = card.get("shelf")
    shelf_code = card.get("shelf_reason_code")
    readiness = card.get("readiness", "")
    gaps = card.get("gaps") or []
    primary = card.get("primary_subject")
    secondary = card.get("secondary_subjects") or []
    roles = card.get("roles") or []
    platforms = card.get("platforms") or []
    summary = card.get("summary", "")
    question = card.get("question_it_answers") or "—"
    claims = card.get("claims") or []
    numbers = card.get("numbers") or []
    recipe = card.get("recipe_steps") or []
    techniques = card.get("techniques") or []
    tools = card.get("tools") or []
    links = card.get("links") or {}
    media = card.get("media") or []
    jh = card.get("judge_hints") or {}
    raw_folder = (card.get("raw") or {}).get("folder", f"raw/items/{item_id}")

    if disposition == "shelf":
        disp_line = f"shelf:{shelf} ({shelf_code})"
    else:
        disp_line = "analyze"

    subj_parts = []
    if primary:
        subj_parts.append(f"[{primary}](../../subjects/{primary}/brief.md)")
    also_parts = [f"[{s}](../../subjects/{s}/brief.md)" for s in secondary]
    also_str = join_list(also_parts) if also_parts else "—"

    lines = [
        f"# {title}",
        "",
        f"`{item_id}` · {source_type} · {artifact_type} · {lang} · [source]({url}) · [raw](../../../{raw_folder}/)",
        f"**Author:** {name} (@{handle}) · **Published:** {published} · **Captured:** {captured}",
        f"**Disposition:** {disp_line} · **Readiness:** {readiness} · **Gaps:** {join_list(gaps)}",
        f"**Subject:** {subj_parts[0] if subj_parts else '—'} · **Also:** {also_str} · **Roles:** {join_list(roles)} · **Platforms:** {join_list(platforms)}",
        "",
        f"**Summary.** {summary}",
        f"**Question it answers.** {question}",
        "",
        "**Claims.**",
    ]
    for c in claims:
        lines.append(
            f"- `{c.get('id')}` ({c.get('kind')}, {c.get('confidence')}) {c.get('text')} — evidence: \"{c.get('evidence')}\" [{c.get('evidence_source')}]"
        )
    if not claims:
        lines.append("—")

    if numbers:
        num_parts = []
        for n in numbers:
            unit = n.get("unit") or ""
            num_parts.append(f"{n.get('label')}: {n.get('value')} {unit} ({n.get('source')})".strip())
        lines.append(f"**Numbers.** {'; '.join(num_parts)}")
    else:
        lines.append("**Numbers.** —")

    if recipe:
        steps = " ".join(f"{i + 1}. {s}" for i, s in enumerate(recipe))
        lines.append(f"**Recipe.** {steps}")
    else:
        lines.append("**Recipe.** —")

    tech_links = [f"[{t}](../../techniques/{t}.md)" for t in techniques]
    tool_links = [f"[{t}](../../tools/{t}.md)" for t in tools]
    lines.append(f"**Techniques.** {join_list(tech_links)}")
    lines.append(f"**Tools.** {join_list(tool_links)}")

    link_bits = []
    if links.get("repo"):
        link_bits.append(f"repo ({links['repo']})")
    if links.get("paper"):
        link_bits.append(f"paper ({links['paper']})")
    if links.get("product"):
        link_bits.append(f"product ({links['product']})")
    for o in links.get("other") or []:
        link_bits.append(str(o))
    lines.append(f"**Links.** {join_list(link_bits)}")

    related = links.get("related_items") or []
    rel_links = [f"[{r}](../{r}/card.md)" for r in related]
    lines.append(f"**Related items.** {join_list(rel_links)}")

    if media:
        lines.append("**Media.**")
        for m in media:
            ct = "true" if m.get("carries_technique") else "false"
            desc = m.get("description") or m.get("skip_reason") or "—"
            lines.append(f"`{m.get('path')}` ({m.get('type')}, carries_technique={ct}) — {desc}")
    else:
        lines.append("**Media.** —")

    if item_id.startswith("x-") and thread:
        ts = thread.get("status", "—")
        rr = thread.get("reply_count_reported", "—")
        rc = thread.get("replies_captured", "—")
        rel = thread.get("replies_relevant", "—")
        ats = thread.get("author_thread_status", "—")
        lines.append(
            f"**Thread.** {ts} · reported {rr} · captured {rc} · relevant {rel} · author thread: {ats} → [thread.md](thread.md)"
        )
    elif item_id.startswith("x-"):
        lines.append("**Thread.** — → [thread.md](thread.md)")

    compare = jh.get("compare_with") or []
    cmp_links = [f"[{c}](../{c}/card.md)" for c in compare]
    lines.append(
        f"**Judge hints.** must_read: {jh.get('must_read', False)} · compare with: {join_list(cmp_links)}"
    )

    if disposition == "shelf":
        lines.append(f"**Shelf reason.** {card.get('shelf_reason', '')}")

    return "\n".join(lines) + "\n"


def render_thread_md(item_id: str, card: dict, thread: dict) -> str:
    title = card.get("title", "")
    status = thread.get("status", "")
    ats = thread.get("author_thread_status", "")
    rr = thread.get("reply_count_reported", "—")
    rc = thread.get("replies_captured", 0)
    rel = thread.get("replies_relevant", 0)
    unfetched = thread.get("replies_dropped_unfetched", "—")
    truncated = thread.get("truncated", False)

    fetch_bits = []
    for entry in thread.get("fetch_log") or []:
        fetch_bits.append(f"{entry.get('method')}→{entry.get('outcome')} ({entry.get('at')})")
    payloads = thread.get("raw_payloads") or []
    payload_str = ", ".join(f"`{p}`" for p in payloads) if payloads else "—"

    lines = [
        f"# Thread — {title} ({item_id})",
        "",
        f"**Status:** {status} · **Author thread:** {ats} · **Replies reported:** {rr} · **Captured:** {rc} · **Relevant:** {rel} · **Unfetched:** {unfetched} · **Truncated:** {truncated}",
        f"**Fetch log:** {'; '.join(fetch_bits)}",
        f"**Raw payloads:** {payload_str}",
        "",
    ]

    def quote_block(text: str) -> list[str]:
        """Keep tweet bodies inside a blockquote so # lines cannot become headings."""
        raw = (text or "").replace("\r\n", "\n").replace("\r", "\n")
        out = []
        for ln in raw.split("\n"):
            safe = ln.replace("\t", " ")
            if safe.startswith("#"):
                safe = "＃" + safe[1:]
            out.append(f"> {safe}")
        return out or ["> "]

    author_thread = thread.get("author_thread") or []
    lines.append(f"**Author continuation ({len(author_thread)} posts).**")
    for p in author_thread:
        lines.append(f"> **@{p.get('author_handle')}** · {p.get('id')} · {p.get('created_at')}")
        lines.extend(quote_block(p.get("text", "")))
        lines.append("")

    quoted = thread.get("quoted") or []
    lines.append("**Quoted.**")
    for p in quoted:
        lines.append(f"> **@{p.get('author_handle')}** · {p.get('id')}")
        lines.extend(quote_block(p.get("text", "")))
        lines.append("")

    replies = thread.get("replies") or []
    relevant = [r for r in replies if r.get("relevance") == "relevant"]
    lines.append(f"**Relevant replies ({len(relevant)} of {len(replies)} captured).**")
    for r in relevant:
        lines.append(
            f"> **@{r.get('author_handle')}** · {r.get('id')} · depth {r.get('depth')} · {r.get('relevance_kind')}"
        )
        lines.extend(quote_block(r.get("text", "")))
        lines.append("")

    noise_count = sum(1 for r in replies if r.get("relevance") == "noise")
    lines.append(f"**Dropped as noise:** {noise_count} replies (praise, emoji, bots, unrelated promo).")

    return "\n".join(lines) + "\n"


def render_tool_page(reg: dict, cards: dict[str, dict]) -> str:
    slug = reg["slug"]
    name = reg.get("name", slug)
    kind = reg.get("kind", "")
    url = reg.get("canonical_url") or "—"
    canonical = reg.get("canonical_item")
    if canonical:
        canon_link = f"[{canonical}](../items/{canonical}/card.md)"
    else:
        canon_link = "—"
    subjects = reg.get("subjects") or []
    subj_links = [f"[{s}](../subjects/{s}/brief.md)" for s in subjects]
    refs = reg.get("item_ids") or []

    lines = [
        f"# {name}",
        "",
        f"**Slug:** `{slug}` · **Kind:** {kind} · **URL:** {url} · **Canonical item:** {canon_link}",
        f"**Subjects:** {', '.join(subj_links) if subj_links else '—'}",
        f"**Referenced by ({len(refs)}):**",
    ]
    for iid in refs:
        c = cards.get(iid, {})
        roles = join_list(c.get("roles") or [])
        ps = c.get("primary_subject") or "—"
        title = c.get("title", iid)
        lines.append(f"- [{title}](../items/{iid}/card.md) — {roles} — {ps}")

    notes_path = TOOLS_DIR / f"{slug}.md"
    notes = extract_notes(notes_path.read_text(encoding="utf-8")) if notes_path.is_file() else ""
    lines.extend(["", NOTES_START, notes, NOTES_END, ""])
    return "\n".join(lines)


def render_technique_page(reg: dict, cards: dict[str, dict]) -> str:
    slug = reg["slug"]
    name = reg.get("name", slug)
    owner = reg.get("owner_subject", "")
    owner_link = f"[{owner}](../subjects/{owner}/brief.md)" if owner else "—"
    subjects = reg.get("subjects") or []
    subj_links = [f"[{s}](../subjects/{s}/brief.md)" for s in subjects]
    refs = reg.get("item_ids") or []

    lines = [
        f"# {name}",
        "",
        f"**Slug:** `{slug}` · **Owner subject:** {owner_link}",
        f"**Subjects:** {', '.join(subj_links) if subj_links else '—'}",
        f"**Referenced by ({len(refs)}):**",
    ]
    for iid in refs:
        c = cards.get(iid, {})
        roles = join_list(c.get("roles") or [])
        ps = c.get("primary_subject") or "—"
        title = c.get("title", iid)
        lines.append(f"- [{title}](../items/{iid}/card.md) — {roles} — {ps}")

    notes_path = TECHNIQUES_DIR / f"{slug}.md"
    notes = extract_notes(notes_path.read_text(encoding="utf-8")) if notes_path.is_file() else ""
    lines.extend(["", NOTES_START, notes, NOTES_END, ""])
    return "\n".join(lines)


def thread_status_for_claim(item_id: str, threads: dict[str, dict]) -> str | None:
    if not item_id.startswith("x-"):
        return None
    t = threads.get(item_id)
    return t.get("status") if t else None


def write_subjects(cards: dict[str, dict], threads: dict[str, dict], index_records: list[dict]) -> None:
    by_subject: dict[str, list[dict]] = defaultdict(list)
    for rec in index_records:
        primary = rec.get("primary_subject")
        secondary = rec.get("secondary_subjects") or []
        if primary:
            r = dict(rec)
            r["membership"] = "primary"
            by_subject[primary].append(r)
        for s in secondary:
            r = dict(rec)
            r["membership"] = "secondary"
            by_subject[s].append(r)

    for subject, recs in by_subject.items():
        subj_dir = SUBJECTS_DIR / subject
        subj_dir.mkdir(parents=True, exist_ok=True)
        recs.sort(key=lambda r: (0 if r.get("membership") == "primary" else 1, r["id"]))
        items_path = subj_dir / "items.jsonl"
        items_path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in recs) + "\n",
            encoding="utf-8",
        )

        claims_lines = []
        for rec in recs:
            item_id = rec["id"]
            card = cards[item_id]
            for claim in card.get("claims") or []:
                if claim.get("subject") != subject:
                    continue
                row = dict(claim)
                row["item_id"] = item_id
                row["item_title"] = card.get("title")
                row["roles"] = card.get("roles")
                row["thread_status"] = thread_status_for_claim(item_id, threads)
                claims_lines.append(row)
        claims_path = subj_dir / "claims.jsonl"
        claims_path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in claims_lines) + ("\n" if claims_lines else ""),
            encoding="utf-8",
        )


def write_shelf(cards: dict[str, dict]) -> None:
    SHELF_DIR.mkdir(parents=True, exist_ok=True)
    shelved = []
    for item_id, card in sorted(cards.items()):
        if card.get("disposition") != "shelf":
            continue
        raw = card.get("raw") or {}
        shelved.append({
            "id": item_id,
            "title": card.get("title"),
            "shelf": card.get("shelf"),
            "shelf_reason_code": card.get("shelf_reason_code"),
            "shelf_reason": card.get("shelf_reason"),
            "duplicate_of": card.get("duplicate_of"),
            "legacy_filtered": raw.get("legacy_filtered", False),
            "worker": card.get("worker"),
            "written_at": card.get("written_at"),
            "raw_folder": raw.get("folder"),
        })

    shelf_jsonl = SHELF_DIR / "shelf.jsonl"
    shelf_jsonl.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in shelved) + ("\n" if shelved else ""),
        encoding="utf-8",
    )

    for shelf_name in ("noise", "duplicate", "out-of-scope", "uncategorized"):
        rows = [r for r in shelved if r.get("shelf") == shelf_name]
        md_path = SHELF_DIR / f"{shelf_name}.md"
        lines = [f"# {shelf_name}", "", "| id | title | code | reason |", "|---|---|---|---|"]
        for r in rows:
            reason = (r.get("shelf_reason") or "").replace("|", "\\|")
            lines.append(
                f"| [{r['id']}](../items/{r['id']}/card.md) | {r.get('title', '')} | {r.get('shelf_reason_code', '')} | {reason} |"
            )
        md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    cards = load_cards()
    threads = load_threads()
    if not cards:
        print("no cards found; skipping render")
        return 0

    rendered_cards = 0
    rendered_threads = 0
    for item_id, card in cards.items():
        card_md_path = ITEMS_DIR / item_id / "card.md"
        card_md_path.write_text(render_card_md(item_id, card, threads.get(item_id)), encoding="utf-8")
        rendered_cards += 1
        if item_id.startswith("x-") and item_id in threads:
            thread_md_path = ITEMS_DIR / item_id / "thread.md"
            thread_md_path.write_text(render_thread_md(item_id, card, threads[item_id]), encoding="utf-8")
            rendered_threads += 1

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    TECHNIQUES_DIR.mkdir(parents=True, exist_ok=True)
    for reg in load_registry_jsonl(REGISTRY_DIR / "tools.jsonl"):
        (TOOLS_DIR / f"{reg['slug']}.md").write_text(render_tool_page(reg, cards), encoding="utf-8")
    for reg in load_registry_jsonl(REGISTRY_DIR / "techniques.jsonl"):
        (TECHNIQUES_DIR / f"{reg['slug']}.md").write_text(render_technique_page(reg, cards), encoding="utf-8")

    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_index import build_index_record

    index_records = []
    for item_id in sorted(cards):
        thread = threads.get(item_id) if item_id.startswith("x-") else None
        index_records.append(build_index_record(item_id, cards[item_id], thread))

    write_subjects(cards, threads, index_records)
    write_shelf(cards)

    print(f"rendered cards={rendered_cards} threads={rendered_threads}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
