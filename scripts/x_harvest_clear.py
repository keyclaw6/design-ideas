#!/usr/bin/env python3
"""Harvest-clear X bookmarks and likes: capture, unsave via GraphQL, verify empty."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AB = shutil.which("agent-browser") or "agent-browser"
TAB = os.environ.get("X_AGENT_TAB", "t9")
AUTH = os.environ.get("X_AUTH_TOKEN", "")
CT0 = os.environ.get("X_CT0", "")
BEARER = os.environ.get(
    "X_BEARER_TOKEN",
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
)
QID = os.environ.get("X_DELETE_BOOKMARK_QID", "Wlmlj2-xzyS1GN3a6cj-mQ")
LIKES_HANDLE = os.environ.get("X_LIKES_HANDLE", "")


def require_env() -> None:
    if not os.environ.get("BU_CDP_URL"):
        sys.exit("Set BU_CDP_URL to agent-browser Chrome CDP")
    if not AUTH or not CT0:
        sys.exit("Set X_AUTH_TOKEN and X_CT0 (or run scripts/x_extract_cookies.py)")


def run(*args: str) -> str:
    subprocess.run([AB, "tab", TAB], capture_output=True)
    r = subprocess.run([AB, *args], capture_output=True, text=True)
    out = (r.stdout or "").strip()
    if out.startswith('"') and out.endswith('"'):
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            return out.strip('"')
    return out


def js(code: str):
    return run("eval", code)


def open_url(url: str, wait: float = 3.0) -> None:
    run("open", url)
    time.sleep(wait)


def inject_cookies() -> None:
    run("cookies", "set", "auth_token", AUTH, "--domain", ".x.com")
    run("cookies", "set", "ct0", CT0, "--domain", ".x.com")


def extract_ids() -> list[str]:
    raw = js(
        'JSON.stringify([...new Set([...document.querySelectorAll(\'a[href*="/status/"]\')]'
        ".map(a=>(a.href.match(/status\\/(\\d+)/)||[])[1]).filter(Boolean))])"
    )
    return json.loads(raw)


def collect_list(url: str) -> list[str]:
    open_url(url, 4)
    ids: set[str] = set()
    stale = 0
    for _ in range(20):
        ids |= set(extract_ids())
        js("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1.5)
        now = set(extract_ids())
        if now <= ids:
            stale += 1
        else:
            stale = 0
            ids |= now
        if stale >= 3:
            break
    return sorted(ids)


def media_list(tw: dict) -> list[dict]:
    raw = tw.get("media") or {}
    if isinstance(raw, dict):
        return list(raw.get("all") or raw.get("photos") or [])
    return raw if isinstance(raw, list) else []


def capture(tid: str) -> None:
    folder = ROOT / f"raw/items/x-{tid}"
    if (folder / "source.json").exists():
        return
    try:
        with urllib.request.urlopen(f"https://api.fxtwitter.com/i/status/{tid}", timeout=30) as resp:
            tw = json.load(resp).get("tweet") or {}
    except Exception as exc:
        print(f"CAPTURE FAIL x-{tid}: {exc}")
        tw = {}
    author = tw.get("author") or {}
    handle = author.get("screen_name", "unknown")
    text = (tw.get("text") or "").strip()
    title = re.sub(r"\s+", " ", text)[:120] or f"X post {tid}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "media").mkdir(exist_ok=True)
    paths = []
    for i, m in enumerate(media_list(tw)):
        url = m.get("url")
        if not url:
            continue
        dest = folder / "media" / f"media_{i}.jpg"
        try:
            urllib.request.urlretrieve(url, dest)
            paths.append(f"media/media_{i}.jpg")
        except OSError:
            pass
    (folder / "post.md").write_text(f"# {title}\n\n@{handle}\n\n{text}\n", encoding="utf-8")
    (folder / "comments.md").write_text("# Comments\n", encoding="utf-8")
    (folder / "research.md").write_text("# Research\n\nAuto-captured during harvest-clear loop.\n", encoding="utf-8")
    meta = {
        "id": f"x-{tid}",
        "url": f"https://x.com/{handle}/status/{tid}",
        "source_type": "x",
        "captured_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "title": title,
        "authors": [f"@{handle}"],
        "topics": [],
        "related_urls": [],
        "media": paths,
        "unsaved": False,
        "extra": {"tweet_id": tid, "author_handle": handle},
    }
    (folder / "source.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"CAPTURED x-{tid}")


def api_unsave(tid: str) -> None:
    req = urllib.request.Request(
        f"https://x.com/i/api/graphql/{QID}/DeleteBookmark",
        data=json.dumps({"variables": {"tweet_id": tid}, "queryId": QID}).encode(),
        headers={
            "content-type": "application/json",
            "x-csrf-token": CT0,
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type": "OAuth2Session",
            "authorization": f"Bearer {urllib.parse.unquote(BEARER)}",
            "cookie": f"auth_token={AUTH}; ct0={CT0}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.load(resp)
        print(f"UNSAVED x-{tid}: {body.get('data', body)}")
    except urllib.error.HTTPError as e:
        print(f"API FAIL x-{tid}: {e.code}")
        open_url(f"https://x.com/i/status/{tid}")
        js(
            "(()=>{const b=document.querySelector('button[data-testid=removeBookmark]');"
            "if(b){b.click();return 'clicked'}return 'none'})()"
        )
    src = ROOT / f"raw/items/x-{tid}/source.json"
    if src.exists():
        meta = json.loads(src.read_text())
        meta["unsaved"] = True
        meta.setdefault("extra", {})["unsaved_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        src.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def unlike(tid: str) -> None:
    open_url(f"https://x.com/i/status/{tid}")
    res = js(
        "(()=>{const b=document.querySelector('button[data-testid=unlike]');"
        "if(b){b.click();return 'ok'}return 'no'})()"
    )
    if res == "ok":
        src = ROOT / f"raw/items/x-{tid}/source.json"
        if src.exists():
            meta = json.loads(src.read_text())
            meta["unliked"] = True
            meta.setdefault("extra", {})["unliked_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            src.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        print(f"UNLIKED x-{tid}")


def likes_url() -> str:
    if LIKES_HANDLE:
        return f"https://x.com/{LIKES_HANDLE.lstrip('@')}/likes"
    open_url("https://x.com/home", 2)
    handle = js(
        '(()=>{const a=document.querySelector(\'a[data-testid="AppTabBar_Profile_Link"]\');'
        "return a?a.getAttribute('href'):null})()"
    )
    if handle and handle != "null":
        return f"https://x.com{handle}/likes"
    sys.exit("Set X_LIKES_HANDLE or ensure profile link is visible")


def main() -> None:
    require_env()
    inject_cookies()
    for round_num in range(1, 10):
        bm_ids = collect_list("https://x.com/i/bookmarks")
        print(f"ROUND {round_num} bookmarks: {len(bm_ids)}")
        if not bm_ids:
            break
        for tid in bm_ids:
            capture(tid)
        for tid in bm_ids:
            api_unsave(tid)
        time.sleep(2)

    for round_num in range(1, 5):
        like_ids = collect_list(likes_url())
        print(f"ROUND {round_num} likes: {len(like_ids)}")
        if not like_ids:
            break
        for tid in like_ids:
            capture(tid)
        for tid in like_ids:
            unlike(tid)
        time.sleep(2)

    left_bm = collect_list("https://x.com/i/bookmarks")
    left_lk = collect_list(likes_url())
    print(f"VERIFY bookmarks={left_bm} likes={left_lk}")
    if left_bm or left_lk:
        sys.exit(1)


if __name__ == "__main__":
    main()
