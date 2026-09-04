#!/usr/bin/env python3
"""Fetch thread metadata and raw payloads for x-* items."""

from __future__ import annotations

import argparse
import json
import re
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

WORKSPACE = Path(__file__).resolve().parents[2]
RAW_ITEMS = WORKSPACE / "raw" / "items"
TIMEOUT = 20
MAX_PAYLOAD = 2 * 1024 * 1024


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def fetch_url(url: str) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": "analysis-thread-fetch/1.0"})
    with urlopen(req, timeout=TIMEOUT) as resp:
        data = resp.read(MAX_PAYLOAD + 1)
        if len(data) > MAX_PAYLOAD:
            data = data[:MAX_PAYLOAD]
        ctype = resp.headers.get("Content-Type", "")
        return data, ctype


def ext_for_content(ctype: str, data: bytes) -> str:
    if "json" in ctype or (data[:1] == b"{" or data[:1] == b"["):
        return "json"
    if "html" in ctype:
        return "html"
    return "txt"


def save_payload(item_dir: Path, method: str, data: bytes, ext: str) -> str:
    thread_raw = item_dir / "thread-raw"
    thread_raw.mkdir(parents=True, exist_ok=True)
    fname = f"{method}-{utc_stamp()}.{ext}"
    path = thread_raw / fname
    path.write_bytes(data)
    return str(path.relative_to(WORKSPACE))


def parse_tweet_id(item_id: str) -> str:
    if item_id.startswith("x-"):
        return item_id[2:]
    return item_id


def load_handle(item_id: str, handle_arg: str | None) -> str | None:
    if handle_arg:
        return handle_arg.lstrip("@")
    source_path = RAW_ITEMS / item_id / "source.json"
    if source_path.is_file():
        source = json.loads(source_path.read_text(encoding="utf-8"))
        extra = source.get("extra") or {}
        h = extra.get("author_handle")
        if h:
            return str(h).lstrip("@")
    return None


def try_vxtwitter(handle: str, tweet_id: str, item_dir: Path, log: list) -> dict:
    url = f"https://api.vxtwitter.com/{handle}/status/{tweet_id}"
    print(f"attempt vxtwitter-api {url}", file=sys.stderr)
    try:
        data, ctype = fetch_url(url)
        rel = save_payload(item_dir, "vxtwitter-api", data, ext_for_content(ctype, data))
        log.append({"method": "vxtwitter-api", "url": url, "path": rel, "ok": True})
        parsed = json.loads(data.decode("utf-8"))
        tweet = parsed.get("tweet") or parsed
        reply_count = tweet.get("replies") or tweet.get("reply_count")
        quote_count = tweet.get("quotes") or tweet.get("quote_count")
        quoted = tweet.get("quote") or tweet.get("quoted_status")
        return {
            "reply_count": reply_count,
            "quote_count": quote_count,
            "quoted": quoted,
            "payload": rel,
        }
    except Exception as e:
        log.append({"method": "vxtwitter-api", "url": url, "error": str(e), "ok": False})
        print(f"vxtwitter-api failed: {e}", file=sys.stderr)
        return {}


def try_fxtwitter(handle: str, tweet_id: str, item_dir: Path, log: list) -> dict:
    url = f"https://api.fxtwitter.com/{handle}/status/{tweet_id}"
    print(f"attempt fxtwitter-api {url}", file=sys.stderr)
    try:
        data, ctype = fetch_url(url)
        rel = save_payload(item_dir, "fxtwitter-api", data, ext_for_content(ctype, data))
        log.append({"method": "fxtwitter-api", "url": url, "path": rel, "ok": True})
        parsed = json.loads(data.decode("utf-8"))
        tweet = parsed.get("tweet") or parsed
        reply_count = tweet.get("replies") or tweet.get("reply_count")
        quote_count = tweet.get("quotes") or tweet.get("quote_count")
        quoted = tweet.get("quote") or tweet.get("quoted_status")
        return {
            "reply_count": reply_count,
            "quote_count": quote_count,
            "quoted": quoted,
            "payload": rel,
        }
    except Exception as e:
        log.append({"method": "fxtwitter-api", "url": url, "error": str(e), "ok": False})
        print(f"fxtwitter-api failed: {e}", file=sys.stderr)
        return {}


def try_jina_fixupx(handle: str, tweet_id: str, item_dir: Path, log: list) -> dict:
    url = f"https://r.jina.ai/http://fixupx.com/{handle}/status/{tweet_id}"
    print(f"attempt jina-fixupx {url}", file=sys.stderr)
    try:
        data, ctype = fetch_url(url)
        rel = save_payload(item_dir, "jina-fixupx", data, ext_for_content(ctype, data))
        log.append({"method": "jina-fixupx", "url": url, "path": rel, "ok": True})
        text = data.decode("utf-8", errors="replace")
        reply_count = None
        m = re.search(r"(\d+)\s+repl", text, re.I)
        if m:
            reply_count = int(m.group(1))
        return {"reply_count": reply_count, "quote_count": None, "payload": rel, "text_len": len(text)}
    except Exception as e:
        log.append({"method": "jina-fixupx", "url": url, "error": str(e), "ok": False})
        print(f"jina-fixupx failed: {e}", file=sys.stderr)
        return {}


def try_syndication(tweet_id: str, item_dir: Path, log: list) -> dict:
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&token=x"
    print(f"attempt syndication-embed {url}", file=sys.stderr)
    try:
        data, ctype = fetch_url(url)
        rel = save_payload(item_dir, "syndication-embed", data, ext_for_content(ctype, data))
        log.append({"method": "syndication-embed", "url": url, "path": rel, "ok": True})
        parsed = json.loads(data.decode("utf-8"))
        reply_count = parsed.get("conversation_count") or parsed.get("reply_count")
        quote_count = parsed.get("quote_count")
        return {"reply_count": reply_count, "quote_count": quote_count, "payload": rel}
    except Exception as e:
        log.append({"method": "syndication-embed", "url": url, "error": str(e), "ok": False})
        print(f"syndication-embed failed: {e}", file=sys.stderr)
        return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch thread raw payloads for an x-* item.")
    parser.add_argument("--id", required=True, help="Item id, e.g. x-2095549461737111905")
    parser.add_argument("--handle", help="Author handle (without @)")
    args = parser.parse_args()

    item_id = args.id
    if not item_id.startswith("x-"):
        print(json.dumps({"error": "id must start with x-", "id": item_id}))
        return 0

    item_dir = RAW_ITEMS / item_id
    if not item_dir.is_dir():
        print(json.dumps({"error": "raw item folder missing", "id": item_id}))
        return 0

    tweet_id = parse_tweet_id(item_id)
    handle = load_handle(item_id, args.handle)
    if not handle:
        print(json.dumps({"error": "handle missing; pass --handle or set source.json extra.author_handle", "id": item_id}))
        return 0

    methods_tried: list[str] = []
    payload_paths: list[str] = []
    attempt_log: list[dict] = []
    reply_count = None
    quote_count = None
    quoted = None

    try:
        for name, fn in (
            ("vxtwitter-api", lambda: try_vxtwitter(handle, tweet_id, item_dir, attempt_log)),
            ("fxtwitter-api", lambda: try_fxtwitter(handle, tweet_id, item_dir, attempt_log)),
            ("jina-fixupx", lambda: try_jina_fixupx(handle, tweet_id, item_dir, attempt_log)),
            ("syndication-embed", lambda: try_syndication(tweet_id, item_dir, attempt_log)),
        ):
            methods_tried.append(name)
            result = fn()
            if result.get("payload"):
                payload_paths.append(result["payload"])
            if result.get("reply_count") is not None:
                reply_count = result["reply_count"]
            if result.get("quote_count") is not None:
                quote_count = result["quote_count"]
            if result.get("quoted") is not None:
                quoted = result["quoted"]
    except Exception:
        traceback.print_exc(file=sys.stderr)

    summary = {
        "id": item_id,
        "tweet_id": tweet_id,
        "handle": handle,
        "reply_count": reply_count,
        "quote_count": quote_count,
        "quoted": quoted is not None,
        "methods_tried": methods_tried,
        "payload_paths": payload_paths,
        "attempts": attempt_log,
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
