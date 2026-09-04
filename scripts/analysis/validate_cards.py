#!/usr/bin/env python3
"""Validate card.json and thread.json; recompute readiness."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterator

WORKSPACE = Path(__file__).resolve().parents[2]
SUBJECTS_PATH = WORKSPACE / "analysis" / "subjects.json"

# --- §4.1 enums ---
SOURCE_TYPES = {"x", "github", "website", "note"}
DISPOSITIONS = {"analyze", "shelf"}
SHELVES = {"noise", "duplicate", "out-of-scope", "uncategorized"}
READINESS = {"ready", "ready-with-gaps", "blocked", "shelved"}
ROLES = {"tool", "technique", "example", "claim-source", "reference"}
ARTIFACT_TYPES = {
    "repo", "product", "paper", "article", "thread", "demo-video", "demo-image",
    "dataset", "course", "announcement", "opinion", "note",
}
PLATFORMS = {
    "claude-code", "codex", "cursor", "grok-bot", "gemini", "pi", "blender",
    "unreal", "three-js", "react", "remotion", "comfyui", "fal", "runway",
    "higgsfield", "kicad", "fusion", "openscad", "browser", "cli", "mcp", "other",
}
GAPS = {
    "thread-failed", "thread-partial", "media-undescribed",
    "linked-page-unfetched", "translation-needed", "paywalled",
}
CLAIM_KINDS = {
    "result", "recipe", "capability", "benchmark", "pricing",
    "availability", "opinion", "counter-claim",
}
EVIDENCE_SOURCES = {
    "post", "author-thread", "reply", "quoted-post",
    "linked-page", "media", "note",
}
CONFIDENCE = {"demonstrated", "stated", "contested", "unverified"}
MEDIA_TYPES = {"image", "video", "gif", "other"}
NUMBER_SOURCES = EVIDENCE_SOURCES

SHELF_REASON_CODES: dict[str, set[str]] = {
    "noise": {
        "engagement-bait", "promo-no-artifact", "availability-announcement",
        "empty-capture", "unrelated-personal",
    },
    "duplicate": {"same-artifact-no-new-angle"},
    "out-of-scope": {"real-artifact-no-subject"},
    "uncategorized": {"needs-triage"},
}

BANNED_SHELF_SUBSTRINGS = [
    "see post.md", "filtered noise", "no matching topic", "out of taxonomy",
]

CARD_KEYS = [
    "schema_version", "id", "source_type", "url", "title", "author",
    "published_at", "captured_at", "lang", "disposition", "shelf",
    "shelf_reason_code", "shelf_reason", "duplicate_of", "primary_subject",
    "secondary_subjects", "roles", "artifact_type", "platforms", "summary",
    "question_it_answers", "claims", "recipe_steps", "numbers", "techniques",
    "tools", "links", "media", "raw", "readiness", "gaps", "judge_hints",
    "worker", "written_at",
]

AUTHOR_KEYS = ["name", "handle", "url"]
LINKS_KEYS = ["canonical", "repo", "paper", "product", "other", "related_items"]
RAW_KEYS = ["folder", "post", "comments", "research", "legacy_topics", "legacy_filtered"]
JUDGE_HINTS_KEYS = ["compare_with", "must_read", "why_must_read"]
CLAIM_KEYS = [
    "id", "text", "kind", "evidence", "evidence_source", "evidence_ref",
    "confidence", "subject",
]
MEDIA_KEYS = ["path", "type", "description", "skip_reason", "carries_technique"]
NUMBER_KEYS = ["label", "value", "unit", "source"]

THREAD_KEYS = [
    "schema_version", "id", "tweet_id", "root_author_handle", "status",
    "author_thread_status", "reply_count_reported", "count_unavailable_reason",
    "quote_count_reported", "replies_captured", "replies_relevant",
    "replies_dropped_unfetched", "truncated", "author_thread", "replies",
    "quoted", "fetch_log", "raw_payloads", "worker", "written_at",
]

THREAD_STATUS = {"captured_full", "captured_partial", "empty", "failed"}
AUTHOR_THREAD_STATUS = {"none", "captured", "partial", "unknown"}
FETCH_METHODS = {
    "x-graphql-tweetdetail", "x-web-dom", "fxtwitter-api", "vxtwitter-api",
    "jina-fixupx", "syndication-embed", "nitter", "threadreader", "other",
}
FETCH_OUTCOMES = {"ok", "partial", "empty", "blocked", "login-wall", "rate-limited", "error"}
RELEVANCE = {"relevant", "noise"}
RELEVANCE_KINDS = {
    None, "link", "recipe", "number", "correction", "counter-claim",
    "alternative-tool", "answered-question", "author-continuation", "fact-check",
}

POST_KEYS = [
    "id", "author_handle", "created_at", "text", "text_en", "urls",
    "media_urls", "metrics",
]
METRICS_KEYS = ["likes", "replies", "reposts", "views"]
REPLY_EXTRA_KEYS = [
    "parent_id", "depth", "is_author", "relevance", "relevance_kind",
    "downloaded_media",
]
FETCH_LOG_KEYS = ["at", "method", "target", "outcome", "note"]

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def load_subjects() -> set[str]:
    if not SUBJECTS_PATH.is_file():
        return set()
    data = json.loads(SUBJECTS_PATH.read_text(encoding="utf-8"))
    return {s["slug"] for s in data}


def prefix_source_type(item_id: str) -> str | None:
    if item_id.startswith("x-"):
        return "x"
    if item_id.startswith("github-"):
        return "github"
    if item_id.startswith("web-"):
        return "website"
    if item_id.startswith("note-"):
        return "note"
    return None


def compute_readiness(card: dict[str, Any], thread: dict[str, Any] | None) -> str:
    if card.get("disposition") == "shelf":
        return "shelved"
    summary = card.get("summary") or ""
    claims = card.get("claims") or []
    primary = card.get("primary_subject")
    question = card.get("question_it_answers")
    media = card.get("media") or []
    gaps = card.get("gaps") or []

    blocked = False
    if not summary or len(summary) < 80:
        blocked = True
    if not claims:
        blocked = True
    if primary is None:
        blocked = True
    if question is None:
        blocked = True
    for m in media:
        if m.get("type") == "image":
            desc = m.get("description")
            skip = m.get("skip_reason")
            if not desc and not skip:
                blocked = True
                break

    if blocked:
        return "blocked"

    thread_partial = False
    if card.get("source_type") == "x" and thread is not None:
        status = thread.get("status")
        if status in ("failed", "captured_partial"):
            thread_partial = True

    if thread_partial or gaps:
        return "ready-with-gaps"
    return "ready"


def _err(prefix: str, msg: str) -> str:
    return f"{prefix}: {msg}"


def validate_card(
    card_path: Path,
    subjects: set[str],
    *,
    fix_readiness: bool = True,
) -> list[str]:
    errors: list[str] = []
    prefix = str(card_path)
    item_dir = card_path.parent
    item_id = item_dir.name

    if not card_path.is_file():
        return [_err(prefix, "card.json missing")]
    try:
        card = json.loads(card_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [_err(prefix, f"invalid JSON: {e}")]

    if not isinstance(card, dict):
        return [_err(prefix, "card must be an object")]

    for key in CARD_KEYS:
        if key not in card:
            errors.append(_err(prefix, f"missing key '{key}'"))

    if card.get("schema_version") != "1":
        errors.append(_err(prefix, "schema_version must be '1'"))
    if card.get("id") != item_id:
        errors.append(_err(prefix, f"id must equal folder name '{item_id}'"))

    expected_st = prefix_source_type(item_id)
    if expected_st and card.get("source_type") != expected_st:
        errors.append(_err(prefix, f"source_type must be '{expected_st}' from id prefix"))
    elif card.get("source_type") not in SOURCE_TYPES:
        errors.append(_err(prefix, f"invalid source_type '{card.get('source_type')}'"))

    if not isinstance(card.get("url"), str):
        errors.append(_err(prefix, "url must be string"))
    title = card.get("title")
    if not isinstance(title, str):
        errors.append(_err(prefix, "title must be string"))
    elif len(title) > 90:
        errors.append(_err(prefix, f"title length {len(title)} > 90"))

    author = card.get("author")
    if not isinstance(author, dict):
        errors.append(_err(prefix, "author must be object"))
    else:
        for k in AUTHOR_KEYS:
            if k not in author:
                errors.append(_err(prefix, f"author missing '{k}'"))

    for field in ("published_at", "captured_at", "lang", "written_at"):
        if field not in card:
            continue
        if field == "published_at" and card[field] is not None and not isinstance(card[field], str):
            errors.append(_err(prefix, "published_at must be string or null"))
        elif field != "published_at" and not isinstance(card.get(field), str):
            errors.append(_err(prefix, f"{field} must be string"))

    disp = card.get("disposition")
    if disp not in DISPOSITIONS:
        errors.append(_err(prefix, f"invalid disposition '{disp}'"))

    shelf = card.get("shelf")
    if shelf is not None and shelf not in SHELVES:
        errors.append(_err(prefix, f"invalid shelf '{shelf}'"))

    src = card.get("shelf_reason_code")
    if src is not None and not isinstance(src, str):
        errors.append(_err(prefix, "shelf_reason_code must be string or null"))

    summary = card.get("summary", "")
    if not isinstance(summary, str):
        errors.append(_err(prefix, "summary must be string"))
    elif disp == "analyze" and (len(summary) < 80 or len(summary) > 320):
        errors.append(_err(prefix, f"summary length {len(summary)} not in 80-320 for analyze"))

    if disp == "analyze":
        if shelf is not None:
            errors.append(_err(prefix, "shelf must be null when disposition=analyze"))
        if card.get("shelf_reason_code") is not None:
            errors.append(_err(prefix, "shelf_reason_code must be null when analyze"))
        if card.get("shelf_reason") is not None:
            errors.append(_err(prefix, "shelf_reason must be null when analyze"))
        ps = card.get("primary_subject")
        if ps is None:
            errors.append(_err(prefix, "primary_subject required when analyze"))
        elif subjects and ps not in subjects:
            errors.append(_err(prefix, f"primary_subject '{ps}' not in subjects.json"))
        roles = card.get("roles")
        if not isinstance(roles, list) or not (1 <= len(roles) <= 3):
            errors.append(_err(prefix, "roles must have length 1-3 when analyze"))
        else:
            for r in roles:
                if r not in ROLES:
                    errors.append(_err(prefix, f"invalid role '{r}'"))
        claims = card.get("claims")
        if not isinstance(claims, list) or len(claims) < 1:
            errors.append(_err(prefix, "claims must have >= 1 entry when analyze"))
        if card.get("question_it_answers") is None:
            errors.append(_err(prefix, "question_it_answers required when analyze"))
    elif disp == "shelf":
        if shelf is None:
            errors.append(_err(prefix, "shelf required when disposition=shelf"))
        elif shelf in SHELF_REASON_CODES:
            code = card.get("shelf_reason_code")
            if code not in SHELF_REASON_CODES.get(shelf, set()):
                errors.append(_err(prefix, f"shelf_reason_code '{code}' invalid for shelf '{shelf}'"))
        if card.get("primary_subject") is not None:
            errors.append(_err(prefix, "primary_subject must be null when shelved"))
        reason = card.get("shelf_reason")
        if not isinstance(reason, str) or len(reason) < 60:
            errors.append(_err(prefix, "shelf_reason must be >= 60 chars when shelved"))
        elif reason:
            low = reason.lower()
            for banned in BANNED_SHELF_SUBSTRINGS:
                if banned in low:
                    errors.append(_err(prefix, f"shelf_reason contains banned substring '{banned}'"))
        for empty_field in ("roles", "claims", "techniques", "tools"):
            val = card.get(empty_field)
            if val != []:
                errors.append(_err(prefix, f"{empty_field} must be [] when shelved"))
        if shelf == "duplicate":
            dup = card.get("duplicate_of")
            if not isinstance(dup, str):
                errors.append(_err(prefix, "duplicate_of required when shelf=duplicate"))

    sec = card.get("secondary_subjects")
    if not isinstance(sec, list) or len(sec) > 2:
        errors.append(_err(prefix, "secondary_subjects must be array length 0-2"))
    else:
        primary = card.get("primary_subject")
        for s in sec:
            if subjects and s not in subjects:
                errors.append(_err(prefix, f"secondary_subject '{s}' not in subjects.json"))
            if s == primary:
                errors.append(_err(prefix, f"secondary_subjects must exclude primary '{s}'"))

    if card.get("artifact_type") not in ARTIFACT_TYPES:
        errors.append(_err(prefix, f"invalid artifact_type '{card.get('artifact_type')}'"))

    platforms = card.get("platforms")
    if not isinstance(platforms, list) or len(platforms) > 4:
        errors.append(_err(prefix, "platforms must be array length 0-4"))
    else:
        for p in platforms:
            if p not in PLATFORMS:
                errors.append(_err(prefix, f"invalid platform '{p}'"))

    gaps = card.get("gaps")
    if not isinstance(gaps, list):
        errors.append(_err(prefix, "gaps must be array"))
    else:
        for g in gaps:
            if g not in GAPS:
                errors.append(_err(prefix, f"invalid gap '{g}'"))

    # claims detail
    claims = card.get("claims") or []
    if isinstance(claims, list):
        expected_n = 1
        subjects_for_claims = {card.get("primary_subject")} | set(sec or [])
        subjects_for_claims.discard(None)
        for claim in claims:
            if not isinstance(claim, dict):
                errors.append(_err(prefix, "claim must be object"))
                continue
            for ck in CLAIM_KEYS:
                if ck not in claim:
                    errors.append(_err(prefix, f"claim missing '{ck}'"))
            cid = claim.get("id")
            if cid != f"{item_id}#c{expected_n}":
                errors.append(_err(prefix, f"claim id '{cid}' expected '{item_id}#c{expected_n}'"))
            expected_n += 1
            if claim.get("kind") not in CLAIM_KINDS:
                errors.append(_err(prefix, f"invalid claim kind '{claim.get('kind')}'"))
            if claim.get("evidence_source") not in EVIDENCE_SOURCES:
                errors.append(_err(prefix, f"invalid evidence_source '{claim.get('evidence_source')}'"))
            if claim.get("confidence") not in CONFIDENCE:
                errors.append(_err(prefix, f"invalid confidence '{claim.get('confidence')}'"))
            if not claim.get("evidence"):
                errors.append(_err(prefix, "claim evidence must be non-empty"))
            subj = claim.get("subject")
            if subjects_for_claims and subj not in subjects_for_claims:
                errors.append(_err(prefix, f"claim subject '{subj}' not in primary/secondary"))

    # media
    media = card.get("media")
    if isinstance(media, list):
        for m in media:
            if not isinstance(m, dict):
                errors.append(_err(prefix, "media entry must be object"))
                continue
            for mk in MEDIA_KEYS:
                if mk not in m:
                    errors.append(_err(prefix, f"media missing '{mk}'"))
            if m.get("type") not in MEDIA_TYPES:
                errors.append(_err(prefix, f"invalid media type '{m.get('type')}'"))
            if m.get("type") == "image":
                desc = m.get("description")
                skip = m.get("skip_reason")
                if not desc and not skip:
                    errors.append(_err(prefix, "image media requires description or skip_reason"))

    # links, raw, judge_hints
    links = card.get("links")
    if isinstance(links, dict):
        for lk in LINKS_KEYS:
            if lk not in links:
                errors.append(_err(prefix, f"links missing '{lk}'"))

    raw = card.get("raw")
    if isinstance(raw, dict):
        for rk in RAW_KEYS:
            if rk not in raw:
                errors.append(_err(prefix, f"raw missing '{rk}'"))

    jh = card.get("judge_hints")
    if isinstance(jh, dict):
        for jk in JUDGE_HINTS_KEYS:
            if jk not in jh:
                errors.append(_err(prefix, f"judge_hints missing '{jk}'"))
        cw = jh.get("compare_with")
        if not isinstance(cw, list) or len(cw) > 6:
            errors.append(_err(prefix, "judge_hints.compare_with must be array length 0-6"))

    # techniques/tools slugs
    for field in ("techniques", "tools"):
        val = card.get(field)
        if not isinstance(val, list):
            errors.append(_err(prefix, f"{field} must be array"))
        else:
            max_len = 5 if field == "techniques" else 8
            if disp == "analyze" and len(val) > max_len:
                errors.append(_err(prefix, f"{field} length {len(val)} > {max_len}"))
            for slug in val:
                if not isinstance(slug, str) or not SLUG_RE.match(slug) or len(slug) > 48:
                    errors.append(_err(prefix, f"invalid {field} slug '{slug}'"))

    # readiness recompute
    thread_path = item_dir / "thread.json"
    thread = None
    if thread_path.is_file():
        try:
            thread = json.loads(thread_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    computed = compute_readiness(card, thread)
    if card.get("readiness") not in READINESS:
        errors.append(_err(prefix, f"invalid readiness '{card.get('readiness')}'"))
    elif fix_readiness and card.get("readiness") != computed:
        card["readiness"] = computed
        card_path.write_text(json.dumps(card, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return errors


def validate_post(obj: Any, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(obj, dict):
        return [f"{label}: must be object"]
    for k in POST_KEYS:
        if k not in obj:
            errors.append(f"{label}: missing '{k}'")
    metrics = obj.get("metrics")
    if isinstance(metrics, dict):
        for mk in METRICS_KEYS:
            if mk not in metrics:
                errors.append(f"{label}: metrics missing '{mk}'")
    return errors


def validate_reply(obj: Any, label: str) -> list[str]:
    errors = validate_post(obj, label)
    if not isinstance(obj, dict):
        return errors
    for k in REPLY_EXTRA_KEYS:
        if k not in obj:
            errors.append(f"{label}: missing '{k}'")
    if obj.get("relevance") not in RELEVANCE:
        errors.append(f"{label}: invalid relevance '{obj.get('relevance')}'")
    rk = obj.get("relevance_kind")
    if rk not in RELEVANCE_KINDS:
        errors.append(f"{label}: invalid relevance_kind '{rk}'")
    return errors


def validate_thread(thread_path: Path) -> list[str]:
    errors: list[str] = []
    prefix = str(thread_path)
    item_dir = thread_path.parent
    item_id = item_dir.name

    if not thread_path.is_file():
        return []
    try:
        thread = json.loads(thread_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [_err(prefix, f"invalid JSON: {e}")]

    if not isinstance(thread, dict):
        return [_err(prefix, "thread must be object")]

    for key in THREAD_KEYS:
        if key not in thread:
            errors.append(_err(prefix, f"missing key '{key}'"))

    if thread.get("schema_version") != "1":
        errors.append(_err(prefix, "schema_version must be '1'"))
    if thread.get("id") != item_id:
        errors.append(_err(prefix, f"id must equal folder '{item_id}'"))

    tweet_id = thread.get("tweet_id")
    if not isinstance(tweet_id, str) or not tweet_id.isdigit():
        errors.append(_err(prefix, "tweet_id must be numeric string"))
    elif item_id.startswith("x-") and tweet_id != item_id[2:]:
        errors.append(_err(prefix, f"tweet_id '{tweet_id}' must match id suffix"))

    if thread.get("status") not in THREAD_STATUS:
        errors.append(_err(prefix, f"invalid status '{thread.get('status')}'"))
    if thread.get("author_thread_status") not in AUTHOR_THREAD_STATUS:
        errors.append(_err(prefix, f"invalid author_thread_status"))

    rc = thread.get("reply_count_reported")
    cur = thread.get("count_unavailable_reason")
    if rc is not None and not isinstance(rc, int):
        errors.append(_err(prefix, "reply_count_reported must be int or null"))
    if rc is None and cur is None:
        errors.append(_err(prefix, "count_unavailable_reason required when reply_count_reported null"))

    for arr_name in ("author_thread", "replies", "quoted", "raw_payloads"):
        if not isinstance(thread.get(arr_name), list):
            errors.append(_err(prefix, f"{arr_name} must be array"))

    replies = thread.get("replies") or []
    if isinstance(replies, list):
        for i, r in enumerate(replies):
            errors.extend(validate_reply(r, f"{prefix} replies[{i}]"))

    for arr_name in ("author_thread", "quoted"):
        arr = thread.get(arr_name) or []
        if isinstance(arr, list):
            for i, p in enumerate(arr):
                errors.extend(validate_post(p, f"{prefix} {arr_name}[{i}]"))

    fetch_log = thread.get("fetch_log")
    if isinstance(fetch_log, list):
        if len(fetch_log) < 1:
            errors.append(_err(prefix, "fetch_log must have >= 1 entry"))
        for i, entry in enumerate(fetch_log):
            if not isinstance(entry, dict):
                errors.append(_err(prefix, f"fetch_log[{i}] must be object"))
                continue
            for fk in FETCH_LOG_KEYS:
                if fk not in entry:
                    errors.append(_err(prefix, f"fetch_log[{i}] missing '{fk}'"))
            if entry.get("method") not in FETCH_METHODS:
                errors.append(_err(prefix, f"fetch_log[{i}] invalid method"))
            if entry.get("outcome") not in FETCH_OUTCOMES:
                errors.append(_err(prefix, f"fetch_log[{i}] invalid outcome"))
    else:
        errors.append(_err(prefix, "fetch_log must be array"))

    return errors


def iter_card_dirs(target: Path) -> Iterator[Path]:
    if target.name == "card.json" or (target / "card.json").is_file():
        yield target if target.is_dir() else target.parent
        return
    if target.is_dir():
        for child in sorted(target.iterdir()):
            if child.is_dir() and (child / "card.json").is_file():
                yield child
            elif child.is_dir():
                sub = child / "card.json"
                if sub.is_file():
                    yield child


def resolve_targets(path_arg: str) -> list[Path]:
    target = Path(path_arg)
    if not target.is_absolute():
        target = WORKSPACE / target
    if not target.exists():
        return []
    if target.is_dir() and (target / "card.json").is_file():
        return [target]
    if target.is_dir() and target.parent.name == "items":
        return [target]
    if target.is_dir():
        items_root = target
        if target.name != "items" and (target / "items").is_dir():
            items_root = target / "items"
        dirs = []
        for child in sorted(items_root.iterdir()):
            if child.is_dir():
                dirs.append(child)
        return dirs
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate analysis cards and threads.")
    parser.add_argument("path", help="analysis/items or analysis/items/<id>")
    args = parser.parse_args()

    subjects = load_subjects()
    targets = resolve_targets(args.path)
    if not targets:
        print(f"error: no items found at {args.path}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for item_dir in targets:
        card_path = item_dir / "card.json"
        all_errors.extend(validate_card(card_path, subjects, fix_readiness=True))
        thread_path = item_dir / "thread.json"
        if thread_path.is_file():
            all_errors.extend(validate_thread(thread_path))

    for e in all_errors:
        print(e)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
