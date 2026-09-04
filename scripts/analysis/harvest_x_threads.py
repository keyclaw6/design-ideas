#!/usr/bin/env python3
"""Fetch logged-out x.com status pages and extract conversation tweets.

Saves HTML under raw/items/<id>/thread-raw/ and a parsed JSON sidecar
analysis/_work/reports/thread-harvest/<id>.json
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import random
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

FULL_TEXT_RE = re.compile(r'full_text:"((?:\\.|[^"\\])*)"')
CLIENT_TWEET_RE = re.compile(r"client:VHdlZXQ6([A-Za-z0-9+/=]+)")
SCREEN_RE = re.compile(r'screen_name:"([^"]+)"')
CREATED_MS_RE = re.compile(r"created_at_ms:(\d+)")
COUNTS_RE = re.compile(
    r"favorite_count:(\d+),reply_count:(\d+),retweet_count:(\d+),quote_count:(\d+)"
)
VIEWS_RE = re.compile(r'__typename:"ViewCountInfo",count:"(\d+)"')
IN_REPLY_RE = re.compile(r'in_reply_to_status_id_str:"(\d+)"')
TCO_RE = re.compile(r"https?://t\.co/[A-Za-z0-9]+")
REPLY_COUNT_RE = re.compile(r"reply_count:(\d+)")
QUOTE_COUNT_RE = re.compile(r"quote_count:(\d+)")


def unescape(s: str) -> str:
    try:
        return json.loads(f'"{s}"')
    except Exception:
        return (
            s.replace("\\n", "\n")
            .replace("\\t", "\t")
            .replace('\\"', '"')
            .replace("\\\\", "\\")
        )


def _b64_tweet_id(b64: str) -> str | None:
    import base64

    try:
        pad = "=" * (-len(b64) % 4)
        raw = base64.b64decode(b64 + pad).decode("utf-8", "replace")
    except Exception:
        return None
    if raw.startswith("Tweet:"):
        return raw.split(":", 1)[1]
    if raw.isdigit():
        return raw
    return None


def parse_status_html(html: str, root_id: str) -> dict:
    tweets: list[dict] = []
    seen: set[str] = set()
    for b64 in dict.fromkeys(CLIENT_TWEET_RE.findall(html)):
        tid = _b64_tweet_id(b64)
        if not tid or tid in seen:
            continue
        token = f"client:VHdlZXQ6{b64}"
        # slice around this tweet's records
        idx = html.find(token)
        if idx < 0:
            continue
        window = html[idx : idx + 8000]
        text_m = FULL_TEXT_RE.search(window)
        if not text_m:
            continue
        seen.add(tid)
        counts = COUNTS_RE.search(window)
        views = VIEWS_RE.search(window)
        created_ms = CREATED_MS_RE.search(window)
        in_reply = IN_REPLY_RE.search(window)
        # author: look a bit before the tweet token for screen_name
        pre = html[max(0, idx - 2500) : idx + 1500]
        names = SCREEN_RE.findall(pre)
        created_at = None
        if created_ms:
            created_at = datetime.fromtimestamp(
                int(created_ms.group(1)) / 1000, tz=timezone.utc
            ).strftime("%Y-%m-%dT%H:%M:%SZ")
        text = unescape(text_m.group(1))
        tweets.append(
            {
                "id": tid,
                "author_handle": names[-1] if names else None,
                "created_at": created_at,
                "text": text,
                "in_reply_to": in_reply.group(1) if in_reply else None,
                "metrics": {
                    "likes": int(counts.group(1)) if counts else None,
                    "replies": int(counts.group(2)) if counts else None,
                    "reposts": int(counts.group(3)) if counts else None,
                    "views": int(views.group(1)) if views else None,
                    "quotes": int(counts.group(4)) if counts else None,
                },
                "urls": TCO_RE.findall(text),
            }
        )

    root_counts = REPLY_COUNT_RE.findall(html)
    quote_counts = QUOTE_COUNT_RE.findall(html)
    # first reply_count in page is usually the root
    reply_count = int(root_counts[0]) if root_counts else None
    quote_count = int(quote_counts[0]) if quote_counts else None
    return {
        "root_id": root_id,
        "reply_count_reported": reply_count,
        "quote_count_reported": quote_count,
        "tweets": tweets,
        "unique_ids": sorted(seen),
    }


def fetch_html(url: str, timeout: int = 20) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        return e.code, body


def process_item(item_dir: Path) -> dict:
    src = json.loads((item_dir / "source.json").read_text())
    extra = src.get("extra") or {}
    handle = extra.get("author_handle") or (src.get("authors") or [""])[0].lstrip("@")
    tid = extra.get("tweet_id") or item_dir.name.split("-", 1)[1]
    url = f"https://x.com/{handle}/status/{tid}"
    status, html = fetch_html(url)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    raw_dir = item_dir / "thread-raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"x-web-dom-{stamp}.html"
    if len(html) > 2_000_000:
        html = html[:2_000_000]
    raw_path.write_text(html, encoding="utf-8")

    parsed = parse_status_html(html, tid) if status == 200 and html else {
        "root_id": tid,
        "reply_count_reported": None,
        "quote_count_reported": None,
        "tweets": [],
        "unique_ids": [],
    }
    parsed.update(
        {
            "item_id": item_dir.name,
            "handle": handle,
            "http_status": status,
            "url": url,
            "html_bytes": len(html),
            "raw_path": str(raw_path.relative_to(WORKSPACE)),
        }
    )
    out_dir = WORKSPACE / "analysis" / "_work" / "reports" / "thread-harvest"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{item_dir.name}.json").write_text(
        json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {
        "id": item_dir.name,
        "http": status,
        "tweets": len(parsed.get("tweets") or []),
        "reply_count": parsed.get("reply_count_reported"),
        "html_bytes": len(html),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--ids", nargs="*", default=[])
    args = parser.parse_args()

    items = sorted(
        p for p in (WORKSPACE / "raw" / "items").iterdir() if p.name.startswith("x-")
    )
    if args.ids:
        want = set(args.ids)
        items = [p for p in items if p.name in want]
    if args.limit:
        items = items[: args.limit]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = []
        for p in items:
            time.sleep(random.uniform(0.05, 0.15))
            futs.append(ex.submit(process_item, p))
        for i, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            try:
                res = fut.result()
            except Exception as e:
                res = {"id": "?", "error": str(e)[:160]}
            results.append(res)
            if i % 25 == 0:
                print(f"... {i}/{len(items)} last={res}")

    ok = [r for r in results if r.get("http") == 200]
    with_tweets = [r for r in ok if (r.get("tweets") or 0) > 1]
    print(
        f"done n={len(results)} http200={len(ok)} with_extra_tweets={len(with_tweets)}"
    )
    summary = WORKSPACE / "analysis" / "_work" / "reports" / "thread-harvest-summary.json"
    summary.write_text(json.dumps(results, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
