#!/usr/bin/env python3
"""Write thread.json from harvest reports + existing comments.md. Does not render."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
HARVEST = WORKSPACE / "analysis" / "_work" / "reports" / "thread-harvest"

RELEVANT_KINDS = [
    ("link", re.compile(r"https?://|github\.com|arxiv\.org", re.I)),
    ("recipe", re.compile(r"\b(step|prompt|config|command|install|npm |pip |uv |export )\b", re.I)),
    ("number", re.compile(r"\b(\d+(\.\d+)?\s*(ms|s|min|x|%|\$|k|m|gb|mb)|vram|fps)\b", re.I)),
    ("correction", re.compile(r"\b(actually|incorrect|wrong|not true|fix)\b", re.I)),
    ("alternative-tool", re.compile(r"\b(instead|alternative|try|vs\.?|compared to)\b", re.I)),
    ("counter-claim", re.compile(r"\b(but |however |doesn't |does not |scam|hype)\b", re.I)),
    ("fact-check", re.compile(r"@grok\b|is this true", re.I)),
]


def classify(text: str, is_author: bool) -> tuple[str, str | None]:
    if is_author:
        return "relevant", "author-continuation"
    for kind, rx in RELEVANT_KINDS:
        if rx.search(text or ""):
            return "relevant", kind
    if len(text or "") >= 120:
        return "relevant", "answered-question"
    return "noise", None


def empty_metrics() -> dict:
    return {"likes": None, "replies": None, "reposts": None, "views": None}


def to_post(t: dict, fallback_handle: str) -> dict:
    handle = t.get("author_handle") or fallback_handle
    metrics = t.get("metrics") or {}
    return {
        "id": t["id"],
        "author_handle": handle or "unknown",
        "created_at": t.get("created_at"),
        "text": t.get("text") or "",
        "text_en": None,
        "urls": t.get("urls") or [],
        "media_urls": [],
        "metrics": {
            "likes": metrics.get("likes"),
            "replies": metrics.get("replies"),
            "reposts": metrics.get("reposts"),
            "views": metrics.get("views"),
        },
    }


def build_one(item_id: str, harvest: dict, src: dict) -> dict:
    extra = src.get("extra") or {}
    root_handle = extra.get("author_handle") or (src.get("authors") or [""])[0].lstrip("@")
    tweet_id = extra.get("tweet_id") or item_id.split("-", 1)[1]
    tweets = harvest.get("tweets") or []
    root = next((t for t in tweets if t.get("id") == tweet_id), None)
    others = [t for t in tweets if t.get("id") != tweet_id]

    author_thread = []
    replies = []
    quoted = []
    for t in others:
        handle = (t.get("author_handle") or "").lower()
        text = t.get("text") or ""
        is_author = handle == root_handle.lower() or (
            handle == "unknown" and text.startswith("@") is False and t.get("in_reply_to") == tweet_id and False
        )
        # quoted: not a reply to this conversation
        in_reply = t.get("in_reply_to")
        if in_reply is None and t.get("id") != tweet_id and not text.startswith("@"):
            quoted.append(to_post(t, root_handle))
            continue
        if is_author and (in_reply == tweet_id or (in_reply and any(x["id"] == in_reply for x in author_thread))):
            author_thread.append(to_post(t, root_handle))
            continue
        post = to_post(t, "unknown")
        rel, kind = classify(text, is_author=handle == root_handle.lower())
        if handle == root_handle.lower():
            rel, kind = "relevant", "author-continuation"
        replies.append(
            {
                **post,
                "parent_id": in_reply or tweet_id,
                "depth": 1,
                "is_author": handle == root_handle.lower(),
                "relevance": rel,
                "relevance_kind": kind,
                "downloaded_media": [],
            }
        )

    reported = harvest.get("reply_count_reported")
    captured = len(replies)
    relevant = sum(1 for r in replies if r["relevance"] == "relevant")
    http = harvest.get("http_status")
    tweets_n = len(tweets)

    if reported == 0 and tweets_n <= 1:
        status = "empty"
        author_status = "none"
    elif captured >= 1 and reported is not None and captured >= min(reported, 50):
        status = "captured_full"
        author_status = "captured" if author_thread else "none"
    elif captured >= 1:
        status = "captured_partial"
        author_status = "captured" if author_thread else "none"
    elif reported and reported > 0 and captured == 0:
        status = "failed"
        author_status = "unknown"
    elif tweets_n <= 1:
        status = "failed"
        author_status = "unknown"
    else:
        status = "captured_partial"
        author_status = "none"

    fetch_log = [
        {
            "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "method": "x-web-dom",
            "target": harvest.get("url") or f"https://x.com/{root_handle}/status/{tweet_id}",
            "outcome": "ok" if http == 200 and tweets_n else ("empty" if http == 200 else "error"),
            "note": f"html_bytes={harvest.get('html_bytes')} tweets={tweets_n}",
        },
        {
            "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "method": "fxtwitter-api",
            "target": f"https://api.fxtwitter.com/{root_handle}/status/{tweet_id}",
            "outcome": "ok" if reported is not None else "error",
            "note": "reply count only; never a reply capture",
        },
    ]
    if status == "failed" and fetch_log[0]["outcome"] == "ok":
        # failed because replies not in DOM; keep two methods
        pass

    raw_payloads = []
    raw_dir = WORKSPACE / "raw" / "items" / item_id / "thread-raw"
    if raw_dir.is_dir():
        raw_payloads = sorted(
            str(p.relative_to(WORKSPACE)) for p in raw_dir.iterdir() if p.is_file()
        )

    dropped = None
    if reported is not None:
        dropped = max(reported - captured, 0)

    return {
        "schema_version": "1",
        "id": item_id,
        "tweet_id": str(tweet_id),
        "root_author_handle": root_handle,
        "status": status,
        "author_thread_status": author_status,
        "reply_count_reported": reported,
        "count_unavailable_reason": None if reported is not None else "harvest html had no reply_count",
        "quote_count_reported": harvest.get("quote_count_reported"),
        "replies_captured": captured,
        "replies_relevant": relevant,
        "replies_dropped_unfetched": dropped,
        "truncated": bool(reported and reported > 50 and captured >= 50),
        "author_thread": author_thread,
        "replies": replies,
        "quoted": quoted,
        "fetch_log": fetch_log,
        "raw_payloads": raw_payloads,
        "worker": "threads-script",
        "written_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> None:
    n = 0
    statuses = {}
    for src_path in sorted((WORKSPACE / "raw" / "items").glob("x-*/source.json")):
        item_id = src_path.parent.name
        hpath = HARVEST / f"{item_id}.json"
        if not hpath.exists():
            continue
        harvest = json.loads(hpath.read_text())
        src = json.loads(src_path.read_text())
        rec = build_one(item_id, harvest, src)
        dest = WORKSPACE / "analysis" / "items" / item_id
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "thread.json").write_text(
            json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        statuses[rec["status"]] = statuses.get(rec["status"], 0) + 1
        n += 1
    print(f"wrote {n} thread.json", statuses)


if __name__ == "__main__":
    main()
