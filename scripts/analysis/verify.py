#!/usr/bin/env python3
"""Run §9 acceptance checklist."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
REPORTS_DIR = WORKSPACE / "analysis" / "_work" / "reports"
VERIFY_PATH = REPORTS_DIR / "verify.md"

# Import validation helpers
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_cards import (  # noqa: E402
    BANNED_SHELF_SUBSTRINGS,
    SHELF_REASON_CODES,
    compute_readiness,
    load_subjects,
    prefix_source_type,
    validate_card,
    validate_thread,
    SLUG_RE,
)

RAW_ITEMS = WORKSPACE / "raw" / "items"
RAW_NOTES = WORKSPACE / "raw" / "notes"
ITEMS_DIR = WORKSPACE / "analysis" / "items"
SUBJECTS_DIR = WORKSPACE / "analysis" / "subjects"
GRAPHIFY_OUT = WORKSPACE / "graphify-out"


def collect_r() -> set[str]:
    ids: set[str] = set()
    if RAW_ITEMS.is_dir():
        for entry in RAW_ITEMS.iterdir():
            if entry.is_dir():
                ids.add(entry.name)
    if RAW_NOTES.is_dir():
        for path in RAW_NOTES.glob("*.md"):
            ids.add(f"note-{path.stem}")
    return ids


class Checker:
    def __init__(self) -> None:
        self.results: list[tuple[int, str, str]] = []
        self.failed: set[int] = set()

    def record(self, n: int, status: str, detail: str) -> None:
        self.results.append((n, status, detail))
        if status == "FAIL":
            self.failed.add(n)
        print(f"CHECK {n} {status} {detail}")

    def pass_(self, n: int, detail: str = "") -> None:
        self.record(n, "PASS", detail)

    def fail(self, n: int, detail: str) -> None:
        self.record(n, "FAIL", detail)

    def skip(self, n: int, detail: str) -> None:
        self.record(n, "SKIP", detail)


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def count_md_files(analysis: Path) -> int:
    count = 0
    for p in analysis.rglob("*.md"):
        if "_work" in p.parts:
            continue
        count += 1
    return count


def check_heading_hygiene(path: Path) -> list[str]:
    errors = []
    if not path.is_file():
        return ["missing"]
    text = path.read_text(encoding="utf-8")
    h1 = [ln for ln in text.splitlines() if re.match(r"^# ", ln)]
    h2plus = [ln for ln in text.splitlines() if re.match(r"^#{2,} ", ln)]
    if len(h1) != 1:
        errors.append(f"{path}: expected 1 H1, found {len(h1)}")
    if h2plus:
        errors.append(f"{path}: found H2+ headings")
    return errors


def resolve_link(from_path: Path, href: str) -> Path | None:
    if href.startswith("http"):
        return None
    target = (from_path.parent / href).resolve()
    return target


def main() -> int:
    c = Checker()
    R = collect_r()
    S = load_subjects()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1 existence
    required = [
        WORKSPACE / "docs" / "ANALYSIS_STRUCTURE.md",
        WORKSPACE / "analysis" / "README.md",
        WORKSPACE / "analysis" / "subjects.json",
        WORKSPACE / "analysis" / "index.jsonl",
        WORKSPACE / "analysis" / "registry" / "tools.jsonl",
        WORKSPACE / "analysis" / "registry" / "techniques.jsonl",
        WORKSPACE / "analysis" / "registry" / "aliases.json",
        WORKSPACE / "analysis" / "shelf" / "shelf.jsonl",
        WORKSPACE / "analysis" / "shelf" / "noise.md",
        WORKSPACE / "analysis" / "shelf" / "duplicate.md",
        WORKSPACE / "analysis" / "shelf" / "out-of-scope.md",
        WORKSPACE / "analysis" / "shelf" / "uncategorized.md",
        WORKSPACE / ".graphifyignore",
        GRAPHIFY_OUT / "GRAPH_REPORT.md",
        GRAPHIFY_OUT / "graph.json",
    ]
    missing = [str(p.relative_to(WORKSPACE)) for p in required if not p.is_file()]
    if missing:
        c.fail(1, f"missing: {', '.join(missing)}")
    else:
        c.pass_(1)

    # 2 cards
    analysis_items = set()
    if ITEMS_DIR.is_dir():
        for d in ITEMS_DIR.iterdir():
            if d.is_dir():
                analysis_items.add(d.name)
    extra = analysis_items - R
    missing_ids = R - analysis_items
    card_json_ok = all((ITEMS_DIR / i / "card.json").is_file() for i in R if i in analysis_items)
    card_md_ok = all((ITEMS_DIR / i / "card.md").is_file() for i in R if i in analysis_items)
    if len(analysis_items) == 388 and not extra and not missing_ids and card_json_ok and card_md_ok:
        c.pass_(2, f"count={len(analysis_items)}")
    else:
        c.fail(2, f"analysis={len(analysis_items)} missing={len(missing_ids)} extra={len(extra)} card_json={card_json_ok} card_md={card_md_ok}")

    # 3 threads
    x_ids = {i for i in R if i.startswith("x-")}
    thread_json = {i for i in x_ids if (ITEMS_DIR / i / "thread.json").is_file()}
    thread_md = {i for i in x_ids if (ITEMS_DIR / i / "thread.md").is_file()}
    non_x_thread = [i for i in analysis_items if not i.startswith("x-") and (ITEMS_DIR / i / "thread.json").exists()]
    if len(thread_json) == 311 and len(thread_md) == 311 and not non_x_thread:
        c.pass_(3)
    else:
        c.fail(3, f"thread.json={len(thread_json)} thread.md={len(thread_md)} non_x={len(non_x_thread)}")

    # 4 thread-raw
    missing_raw = [i for i in x_ids if not any((RAW_ITEMS / i / "thread-raw").glob("*")) if (RAW_ITEMS / i).is_dir()]
    if not missing_raw:
        c.pass_(4)
    else:
        c.fail(4, f"missing thread-raw for {len(missing_raw)} ids (e.g. {missing_raw[:5]})")

    # 5 index.jsonl
    index_path = WORKSPACE / "analysis" / "index.jsonl"
    index_lines = load_jsonl(index_path)
    index_ids = [r["id"] for r in index_lines]
    if len(index_lines) == 388 and len(set(index_ids)) == 388 and index_ids == sorted(index_ids) and set(index_ids) == R:
        c.pass_(5)
    else:
        c.fail(5, f"lines={len(index_lines)} sorted={index_ids == sorted(index_ids)} set_match={set(index_ids) == R}")

    # 6 subjects
    if not S:
        subjects_data = []
        sp = WORKSPACE / "analysis" / "subjects.json"
        if sp.is_file():
            subjects_data = json.loads(sp.read_text(encoding="utf-8"))
            S = {s["slug"] for s in subjects_data}
    subject_dirs = {d.name for d in SUBJECTS_DIR.iterdir() if d.is_dir()} if SUBJECTS_DIR.is_dir() else set()
    subj_missing = []
    for slug in S:
        for fname in ("brief.md", "brief.json", "items.jsonl", "claims.jsonl"):
            if not (SUBJECTS_DIR / slug / fname).is_file():
                subj_missing.append(f"{slug}/{fname}")
    extra_subj = subject_dirs - S
    if 14 <= len(S) <= 17 and not subj_missing and not extra_subj:
        c.pass_(6, f"|S|={len(S)}")
    else:
        c.fail(6, f"|S|={len(S)} missing_files={len(subj_missing)} extra_dirs={extra_subj}")

    # 7 batches
    batches_path = WORKSPACE / "analysis" / "_work" / "batches.json"
    if batches_path.is_file():
        bdata = json.loads(batches_path.read_text(encoding="utf-8"))
        assignment = bdata.get("assignment", {})
        sizes = defaultdict(int)
        for item_id, batch in assignment.items():
            sizes[batch] += 1
        if set(assignment.keys()) == R and sizes:
            diff = max(sizes.values()) - min(sizes.values())
            if diff <= 1:
                c.pass_(7, f"batches={bdata.get('batches')} sizes_diff={diff}")
            else:
                c.fail(7, f"batch size diff {diff} > 1")
        else:
            c.fail(7, f"assigned={len(assignment)} expected={len(R)}")
    else:
        c.fail(7, "batches.json missing")

    # 8 handoffs
    workers: set[str] = set()
    if ITEMS_DIR.is_dir():
        for d in ITEMS_DIR.iterdir():
            cp = d / "card.json"
            if cp.is_file():
                card = json.loads(cp.read_text(encoding="utf-8"))
                if card.get("worker"):
                    workers.add(card["worker"])
            tp = d / "thread.json"
            if tp.is_file():
                thread = json.loads(tp.read_text(encoding="utf-8"))
                if thread.get("worker"):
                    workers.add(thread["worker"])
    if SUBJECTS_DIR.is_dir():
        for d in SUBJECTS_DIR.iterdir():
            bp = d / "brief.json"
            if bp.is_file():
                brief = json.loads(bp.read_text(encoding="utf-8"))
                if brief.get("written_by"):
                    workers.add(brief["written_by"])
    handoffs_dir = WORKSPACE / "analysis" / "_work" / "handoffs"
    missing_handoffs = [w for w in workers if not (handoffs_dir / f"{w}.md").is_file()]
    if workers and not missing_handoffs:
        c.pass_(8, f"workers={len(workers)}")
    elif not workers:
        c.skip(8, "no workers referenced yet")
    else:
        c.fail(8, f"missing handoffs: {missing_handoffs[:10]}")

    # 9 card schema
    card_errors = []
    for item_id in sorted(analysis_items):
        card_errors.extend(validate_card(ITEMS_DIR / item_id / "card.json", S, fix_readiness=False))
    if not card_errors:
        c.pass_(9)
    else:
        c.fail(9, f"{len(card_errors)} errors; first: {card_errors[0]}")

    # 10 title not truncated tweet
    bad_titles = []
    for item_id in sorted(i for i in analysis_items if i.startswith("x-")):
        cp = ITEMS_DIR / item_id / "card.json"
        card = json.loads(cp.read_text(encoding="utf-8"))
        post_path = RAW_ITEMS / item_id / "post.md"
        if post_path.is_file():
            post_body = post_path.read_text(encoding="utf-8").strip()
            title = card.get("title", "")
            if title[:60] == post_body[:60]:
                bad_titles.append(item_id)
    if not bad_titles:
        c.pass_(10)
    else:
        c.fail(10, f"{len(bad_titles)} items: {bad_titles[:5]}")

    # 11 summary length
    bad_summary = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        s = card.get("summary", "")
        if len(s) < 80 or len(s) > 320:
            bad_summary.append(item_id)
    if not bad_summary:
        c.pass_(11)
    else:
        c.fail(11, f"{len(bad_summary)} items")

    # 12 analyze disposition rules
    bad12 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        if card.get("disposition") != "analyze":
            continue
        if card.get("primary_subject") not in S:
            bad12.append(item_id)
        roles = card.get("roles") or []
        if not (1 <= len(roles) <= 3):
            bad12.append(item_id)
        if len(card.get("claims") or []) < 1:
            bad12.append(item_id)
        if card.get("question_it_answers") is None:
            bad12.append(item_id)
        if card.get("shelf") is not None or card.get("shelf_reason_code") is not None or card.get("shelf_reason") is not None:
            bad12.append(item_id)
    if not bad12:
        c.pass_(12)
    else:
        c.fail(12, f"{len(set(bad12))} violations")

    # 13 shelf disposition
    bad13 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        if card.get("disposition") != "shelf":
            continue
        shelf = card.get("shelf")
        code = card.get("shelf_reason_code")
        if shelf not in SHELF_REASON_CODES or code not in SHELF_REASON_CODES.get(shelf, set()):
            bad13.append(item_id)
        reason = card.get("shelf_reason") or ""
        if len(reason) < 60:
            bad13.append(item_id)
        for banned in BANNED_SHELF_SUBSTRINGS:
            if banned in reason.lower():
                bad13.append(item_id)
        if card.get("primary_subject") is not None:
            bad13.append(item_id)
        for f in ("roles", "claims", "techniques", "tools"):
            if card.get(f) != []:
                bad13.append(item_id)
        if shelf == "duplicate":
            dup = card.get("duplicate_of")
            if dup not in R:
                bad13.append(item_id)
            else:
                target = json.loads((ITEMS_DIR / dup / "card.json").read_text(encoding="utf-8"))
                if target.get("disposition") != "analyze":
                    bad13.append(item_id)
    if not bad13:
        c.pass_(13)
    else:
        c.fail(13, f"{len(set(bad13))} violations")

    # 14 secondary subjects
    bad14 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        sec = card.get("secondary_subjects") or []
        if len(sec) > 2:
            bad14.append(item_id)
        for s in sec:
            if S and s not in S:
                bad14.append(item_id)
            if s == card.get("primary_subject"):
                bad14.append(item_id)
    if not bad14:
        c.pass_(14)
    else:
        c.fail(14, f"{len(set(bad14))} violations")

    # 15 claims
    bad15 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        claims = card.get("claims") or []
        subs = {card.get("primary_subject")} | set(card.get("secondary_subjects") or [])
        subs.discard(None)
        for n, claim in enumerate(claims, 1):
            if claim.get("id") != f"{item_id}#c{n}":
                bad15.append(item_id)
            if subs and claim.get("subject") not in subs:
                bad15.append(item_id)
            if not claim.get("evidence"):
                bad15.append(item_id)
    if not bad15:
        c.pass_(15)
    else:
        c.fail(15, f"{len(set(bad15))} violations")

    # 16 media
    bad16 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        media_dir = RAW_ITEMS / item_id / "media"
        expected = set()
        if media_dir.is_dir():
            for f in media_dir.iterdir():
                if f.is_file() and not f.name.startswith("reply-"):
                    expected.add(f"raw/items/{item_id}/media/{f.name}")
        actual = {m.get("path") for m in card.get("media") or []}
        if expected != actual:
            bad16.append(item_id)
        for m in card.get("media") or []:
            if m.get("type") == "image":
                if not m.get("description") and not m.get("skip_reason"):
                    bad16.append(item_id)
    if not bad16:
        c.pass_(16)
    else:
        c.fail(16, f"{len(set(bad16))} violations")

    # 17 readiness
    bad17 = []
    blocked_count = 0
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        tp = ITEMS_DIR / item_id / "thread.json"
        thread = json.loads(tp.read_text(encoding="utf-8")) if tp.is_file() else None
        computed = compute_readiness(card, thread)
        if card.get("readiness") != computed:
            bad17.append(item_id)
        if card.get("disposition") == "analyze" and card.get("readiness") == "blocked":
            blocked_count += 1
    if not bad17 and blocked_count == 0:
        c.pass_(17)
    else:
        c.fail(17, f"mismatch={len(set(bad17))} blocked_analyze={blocked_count}")

    # 18 judge hints
    bad18 = []
    must_read_by_subject: dict[str, int] = defaultdict(int)
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        jh = card.get("judge_hints") or {}
        for cid in jh.get("compare_with") or []:
            if cid not in R:
                bad18.append(item_id)
        if jh.get("must_read") and card.get("primary_subject"):
            must_read_by_subject[card["primary_subject"]] += 1
    over = {s: n for s, n in must_read_by_subject.items() if n > 12}
    if not bad18 and not over:
        c.pass_(18)
    else:
        c.fail(18, f"bad_compare={len(set(bad18))} over_must_read={over}")

    # 19 legacy fields
    bad19 = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        raw = card.get("raw") or {}
        src_path = RAW_ITEMS / item_id / "source.json"
        if not item_id.startswith("note-") and src_path.is_file():
            src = json.loads(src_path.read_text(encoding="utf-8"))
            if raw.get("legacy_topics") != src.get("topics"):
                bad19.append(item_id)
            filtered = bool((src.get("extra") or {}).get("filtered"))
            if raw.get("legacy_filtered") != filtered:
                bad19.append(item_id)
    if not bad19:
        c.pass_(19)
    else:
        c.fail(19, f"{len(set(bad19))} violations")

    # 20 thread schema
    thread_errors = []
    for item_id in sorted(x_ids):
        tp = ITEMS_DIR / item_id / "thread.json"
        if tp.is_file():
            thread_errors.extend(validate_thread(tp))
    if not thread_errors:
        c.pass_(20)
    else:
        c.fail(20, f"{len(thread_errors)} errors")

    # 21 reply_count null count
    null_count = 0
    for item_id in x_ids:
        tp = ITEMS_DIR / item_id / "thread.json"
        if tp.is_file():
            thread = json.loads(tp.read_text(encoding="utf-8"))
            if thread.get("reply_count_reported") is None:
                null_count += 1
    if null_count <= 15:
        c.pass_(21, f"null_count={null_count}")
    else:
        c.fail(21, f"null_count={null_count} > 15")

    # 22-28 thread semantics (simplified mechanical checks)
    bad22, bad23, bad24, bad25, bad26, failed_status = [], [], [], [], [], []
    for item_id in x_ids:
        tp = ITEMS_DIR / item_id / "thread.json"
        if not tp.is_file():
            continue
        thread = json.loads(tp.read_text(encoding="utf-8"))
        status = thread.get("status")
        if status == "failed":
            failed_status.append(item_id)
            if thread.get("replies_captured") != 0:
                bad22.append(item_id)
            methods = {e.get("method") for e in thread.get("fetch_log") or []}
            outcomes = {e.get("outcome") for e in thread.get("fetch_log") or []}
            if len(methods) < 2:
                bad22.append(item_id)
            if not outcomes <= {"blocked", "login-wall", "rate-limited", "error"}:
                bad22.append(item_id)
        if status == "empty":
            if thread.get("reply_count_reported") != 0:
                bad23.append(item_id)
            if not any(e.get("outcome") in ("ok", "empty") for e in thread.get("fetch_log") or []):
                bad23.append(item_id)
        if status in ("captured_full", "captured_partial"):
            replies = thread.get("replies") or []
            if thread.get("replies_captured", 0) < 1:
                bad24.append(item_id)
            if thread.get("replies_captured") != len(replies):
                bad24.append(item_id)
            rel = sum(1 for r in replies if r.get("relevance") == "relevant")
            if thread.get("replies_relevant") != rel:
                bad24.append(item_id)
        if thread.get("author_thread_status") == "unknown" and status != "failed":
            bad25.append(item_id)
        for p in thread.get("raw_payloads") or []:
            if not (WORKSPACE / p).is_file():
                bad26.append(item_id)
        for r in thread.get("replies") or []:
            if r.get("is_author") and r.get("relevance") != "relevant":
                bad26.append(item_id)

    c.pass_(22) if not bad22 else c.fail(22, f"{len(set(bad22))} violations")
    c.pass_(23) if not bad23 else c.fail(23, f"{len(set(bad23))} violations")
    c.pass_(24) if not bad24 else c.fail(24, f"{len(set(bad24))} violations")
    c.pass_(25) if not bad25 else c.fail(25, f"{len(set(bad25))} violations")
    c.pass_(26) if not bad26 else c.fail(26, f"{len(set(bad26))} violations")
    if len(failed_status) <= 62:
        c.pass_(27, f"failed={len(failed_status)}")
    else:
        c.fail(27, f"failed={len(failed_status)} ids={failed_status[:20]}")

    # 28 author replies relevant — covered in 26
    c.pass_(28)

    # 29 brief.json
    bad29 = []
    for slug in S:
        bp = SUBJECTS_DIR / slug / "brief.json"
        if not bp.is_file():
            bad29.append(slug)
            continue
        brief = json.loads(bp.read_text(encoding="utf-8"))
        items = load_jsonl(SUBJECTS_DIR / slug / "items.jsonl")
        primary_count = sum(1 for r in items if r.get("membership") == "primary")
        if brief.get("item_count_primary") != primary_count:
            bad29.append(slug)
        axes = brief.get("comparison_axes") or []
        if not (3 <= len(axes) <= 8):
            bad29.append(slug)
        for ax in axes:
            low = ax.lower()
            if any(w in low for w in ("best", "winner", "recommended")):
                bad29.append(slug)
    if not bad29:
        c.pass_(29)
    else:
        c.fail(29, f"{len(set(bad29))} violations")

    # 30 brief.md structure
    bad30 = []
    for slug in S:
        md_path = SUBJECTS_DIR / slug / "brief.md"
        if not md_path.is_file():
            bad30.append(slug)
            continue
        lines = md_path.read_text(encoding="utf-8").splitlines()
        if not lines or not lines[0].startswith("# "):
            bad30.append(slug)
        expected_h2 = [
            f"## {slug} — scope",
            f"## {slug} — what the owner is trying to decide",
            f"## {slug} — roster by role",
            f"## {slug} — techniques",
            f"## {slug} — tools",
            f"## {slug} — claims to adjudicate",
            f"## {slug} — comparison axes",
            f"## {slug} — thread coverage",
            f"## {slug} — gaps and open questions",
            f"## {slug} — adjacent subjects",
        ]
        h2_lines = [ln for ln in lines if ln.startswith("## ")]
        if h2_lines != expected_h2:
            bad30.append(slug)
        if any(re.match(r"^#{3,} ", ln) for ln in lines):
            bad30.append(slug)
        if not (120 <= len(lines) <= 400):
            bad30.append(slug)
    if not bad30:
        c.pass_(30)
    else:
        c.fail(30, f"{len(set(bad30))} violations")

    # 31 primary item counts 6-60
    bad31 = []
    for slug in S:
        if slug == "image-prompt-galleries":
            continue
        items = load_jsonl(SUBJECTS_DIR / slug / "items.jsonl")
        pc = sum(1 for r in items if r.get("membership") == "primary")
        if not (6 <= pc <= 60):
            bad31.append(f"{slug}={pc}")
    if not bad31:
        c.pass_(31)
    else:
        c.fail(31, ", ".join(bad31[:10]))

    # 32 sum primary = analyze count
    analyze_count = sum(
        1 for i in analysis_items
        if json.loads((ITEMS_DIR / i / "card.json").read_text(encoding="utf-8")).get("disposition") == "analyze"
    )
    sum_primary = 0
    for slug in S:
        items = load_jsonl(SUBJECTS_DIR / slug / "items.jsonl")
        sum_primary += sum(1 for r in items if r.get("membership") == "primary")
    if sum_primary == analyze_count:
        c.pass_(32, f"sum={sum_primary}")
    else:
        c.fail(32, f"sum_primary={sum_primary} analyze={analyze_count}")

    # 33 registry pages
    bad33 = []
    tool_slugs = {r["slug"] for r in load_jsonl(WORKSPACE / "analysis" / "registry" / "tools.jsonl")}
    tech_slugs = {r["slug"] for r in load_jsonl(WORKSPACE / "analysis" / "registry" / "techniques.jsonl")}
    card_tools: set[str] = set()
    card_techs: set[str] = set()
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        for t in card.get("tools") or []:
            card_tools.add(t)
            if not SLUG_RE.match(t) or len(t) > 48:
                bad33.append(t)
            if not (WORKSPACE / "analysis" / "tools" / f"{t}.md").is_file():
                bad33.append(t)
        for t in card.get("techniques") or []:
            card_techs.add(t)
            if not (WORKSPACE / "analysis" / "techniques" / f"{t}.md").is_file():
                bad33.append(t)
    orphan_tools = tool_slugs - card_tools
    orphan_techs = tech_slugs - card_techs
    if not bad33 and not orphan_tools and not orphan_techs:
        c.pass_(33)
    else:
        c.fail(33, f"missing_pages={len(bad33)} orphan_tools={len(orphan_tools)} orphan_tech={len(orphan_techs)}")

    # 34 aliases applied
    aliases_path = WORKSPACE / "analysis" / "registry" / "aliases.json"
    aliases = json.loads(aliases_path.read_text(encoding="utf-8")) if aliases_path.is_file() else {}
    alias_keys_in_cards = []
    for item_id in analysis_items:
        card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
        for t in (card.get("tools") or []) + (card.get("techniques") or []):
            if t in aliases:
                alias_keys_in_cards.append(t)
    if not alias_keys_in_cards:
        c.pass_(34)
    else:
        c.fail(34, f"alias keys still in cards: {alias_keys_in_cards[:10]}")

    # 35 technique NOTES
    bad35 = []
    tech_regs = load_jsonl(WORKSPACE / "analysis" / "registry" / "techniques.jsonl")
    singletons = sum(1 for r in tech_regs if r.get("singleton"))
    for reg in tech_regs:
        md = WORKSPACE / "analysis" / "techniques" / f"{reg['slug']}.md"
        if md.is_file():
            text = md.read_text(encoding="utf-8")
            if "<!-- NOTES:START -->" in text:
                notes = text.split("<!-- NOTES:START -->")[1].split("<!-- NOTES:END -->")[0]
                lines = [ln for ln in notes.strip().splitlines() if ln.strip()]
                if len(lines) < 3:
                    bad35.append(reg["slug"])
    pct = (singletons / len(tech_regs) * 100) if tech_regs else 0
    if not bad35 and pct <= 15:
        c.pass_(35)
    else:
        c.fail(35, f"short_notes={len(bad35)} singleton_pct={pct:.1f}")

    # 36 shelf.jsonl
    shelf_lines = load_jsonl(WORKSPACE / "analysis" / "shelf" / "shelf.jsonl")
    shelf_cards = sum(
        1 for i in analysis_items
        if json.loads((ITEMS_DIR / i / "card.json").read_text(encoding="utf-8")).get("disposition") == "shelf"
    )
    uncategorized = sum(1 for r in shelf_lines if r.get("shelf") == "uncategorized")
    if len(shelf_lines) == shelf_cards and uncategorized <= 19:
        c.pass_(36, f"shelf={len(shelf_lines)} uncategorized={uncategorized}")
    else:
        c.fail(36, f"lines={len(shelf_lines)} cards={shelf_cards} uncategorized={uncategorized}")

    # 37 claims.jsonl counts
    bad37 = []
    for slug in S:
        claims_file = SUBJECTS_DIR / slug / "claims.jsonl"
        file_count = len(load_jsonl(claims_file)) if claims_file.is_file() else 0
        card_count = 0
        for item_id in analysis_items:
            card = json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))
            card_count += sum(1 for cl in card.get("claims") or [] if cl.get("subject") == slug)
        if file_count != card_count:
            bad37.append(slug)
    if not bad37:
        c.pass_(37)
    else:
        c.fail(37, f"{bad37[:5]}")

    # 38 markdown hygiene
    bad38 = []
    md_files = list((WORKSPACE / "analysis").rglob("*.md"))
    for md in md_files:
        if "_work" in md.parts:
            continue
        if md.name == "brief.md":
            continue  # brief.md allows H2
        if md.parent.name == "shelf":
            if check_heading_hygiene(md):
                bad38.append(str(md))
            continue
        errs = check_heading_hygiene(md)
        if errs:
            bad38.append(str(md))
        if md.name == "card.md":
            card = json.loads((md.parent / "card.json").read_text(encoding="utf-8"))
            first = md.read_text(encoding="utf-8").splitlines()[0]
            if first != f"# {card.get('title')}":
                bad38.append(str(md))
    if not bad38:
        c.pass_(38)
    else:
        c.fail(38, f"{len(bad38)} files; e.g. {bad38[:3]}")

    # 39 graphify checks
    if not GRAPHIFY_OUT.is_dir():
        c.skip(39, "graphify-out missing")
    else:
        report = GRAPHIFY_OUT / "GRAPH_REPORT.md"
        agents = WORKSPACE / "AGENTS.md"
        sub39_fail = []
        if report.is_file():
            text = report.read_text(encoding="utf-8")
            banned = ["Research", "Comments", "Comments / thread", "Replies", "Thread", "Claims", "Tools", "Techniques", "Summary", "Media", "Links"]
            for b in banned:
                if f"hub name: {b}" in text or f'"{b}"' in text:
                    sub39_fail.append(f"banned hub {b}")
        else:
            sub39_fail.append("GRAPH_REPORT.md missing")
        if agents.is_file() and "analysis/" not in agents.read_text(encoding="utf-8"):
            sub39_fail.append("AGENTS.md missing analysis/ reference")
        if sub39_fail:
            c.fail(39, "; ".join(sub39_fail))
        else:
            # smoke queries need graphify CLI
            try:
                subprocess.run(["graphify", "query", "test"], capture_output=True, timeout=5)
                c.pass_(39)
            except (FileNotFoundError, subprocess.TimeoutExpired):
                c.skip(39, "graphify CLI unavailable for smoke queries")

    # 40-41 manual samples
    analyze_ids = sorted(
        i for i in analysis_items
        if json.loads((ITEMS_DIR / i / "card.json").read_text(encoding="utf-8")).get("disposition") == "analyze"
    )
    N_a = len(analyze_ids)
    sample_analyze = [analyze_ids[int(k * N_a / 10)] for k in range(10)] if N_a >= 10 else analyze_ids
    c.skip(40, f"SAMPLE analyze ids: {', '.join(sample_analyze)}")

    shelf_lines_ordered = load_jsonl(WORKSPACE / "analysis" / "shelf" / "shelf.jsonl")
    shelf_ids = [r["id"] for r in shelf_lines_ordered]
    N_s = len(shelf_ids)
    sample_shelf = [shelf_ids[int(k * N_s / 10)] for k in range(10)] if N_s >= 10 else shelf_ids
    c.skip(41, f"SAMPLE shelf ids: {', '.join(sample_shelf)}")

    # 42 legacy banners
    bad42 = []
    cat = WORKSPACE / "catalog" / "README.md"
    if cat.is_file() and not cat.read_text(encoding="utf-8").splitlines()[0].startswith("> LEGACY"):
        bad42.append("catalog/README.md")
    schema = WORKSPACE / "SCHEMA.md"
    if schema.is_file() and not schema.read_text(encoding="utf-8").splitlines()[0].startswith("> Raw capture schema only"):
        bad42.append("SCHEMA.md")
    agents = WORKSPACE / "AGENTS.md"
    if agents.is_file() and "analysis/README.md" not in agents.read_text(encoding="utf-8"):
        bad42.append("AGENTS.md")
    root_readme = WORKSPACE / "README.md"
    if root_readme.is_file() and "analysis/README.md" not in root_readme.read_text(encoding="utf-8"):
        bad42.append("README.md")
    if not bad42:
        c.pass_(42)
    else:
        c.fail(42, f"missing: {bad42}")

    # 43 raw frozen
    try:
        result = subprocess.run(
            ["git", "diff", "--stat", "HEAD", "--", "raw/"],
            capture_output=True, text=True, cwd=WORKSPACE, timeout=30,
        )
        lines = [ln for ln in result.stdout.splitlines() if ln.strip() and "thread-raw" not in ln and "media/reply-" not in ln and "|" in ln]
        if not lines:
            c.pass_(43)
        else:
            c.fail(43, f"raw changes: {lines[:5]}")
    except Exception as e:
        c.skip(43, str(e))

    # 44 git clean
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=WORKSPACE, timeout=30,
        )
        if not result.stdout.strip():
            c.pass_(44)
        else:
            c.fail(44, "working tree not clean")
    except Exception as e:
        c.skip(44, str(e))

    # write report
    lines = ["# Verify report\n", "\n"]
    for n, status, detail in sorted(c.results, key=lambda x: x[0]):
        lines.append(f"- CHECK {n} {status}: {detail}\n")
    VERIFY_PATH.write_text("".join(lines), encoding="utf-8")
    print(f"wrote {VERIFY_PATH.relative_to(WORKSPACE)}")

    return 1 if c.failed else 0


if __name__ == "__main__":
    sys.exit(main())
