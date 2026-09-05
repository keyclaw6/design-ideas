#!/usr/bin/env python3
"""leftover20: ReasoningBank blog + Slite nine-name vendor pages. No 429 hammer."""
from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("/workspace/analysis/_work/captures/leftover20-2026-09-05")
OUT.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (compatible; analysis-corpus/1.0; +https://example.invalid)"
CTX = ssl.create_default_context()


class TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_title = False
        self.title = ""
        self.visible: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        if tag in {"script", "style", "noscript"}:
            self._skip = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style", "noscript"}:
            self._skip = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._skip:
            t = " ".join(data.split())
            if t:
                self.visible.append(t)


def fetch(url: str, timeout: int = 25) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=timeout) as resp:
            body = resp.read()
            return {
                "url": url,
                "final": getattr(resp, "url", url),
                "status": getattr(resp, "status", 200),
                "bytes": len(body),
                "ctype": resp.headers.get("Content-Type"),
                "error": None,
                "body": body,
            }
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return {
            "url": url,
            "final": getattr(e, "url", url),
            "status": e.code,
            "bytes": len(body),
            "ctype": e.headers.get("Content-Type") if e.headers else None,
            "error": f"HTTPError {e.code}",
            "body": body,
        }
    except Exception as e:
        return {
            "url": url,
            "final": None,
            "status": None,
            "bytes": 0,
            "ctype": None,
            "error": f"{type(e).__name__}: {e}",
            "body": b"",
        }


def summarize(rec: dict, slug: str) -> dict:
    body = rec.pop("body", b"")
    out = {k: rec[k] for k in rec}
    if not body:
        return out
    ctype = (rec.get("ctype") or "").lower()
    text = body.decode("utf-8", "replace")
    if "json" in ctype or (body[:1] in {b"{", b"["} and "html" not in ctype):
        path = OUT / f"{slug}.json"
        try:
            data = json.loads(text)
            path.write_text(json.dumps(data, indent=2)[:200_000], encoding="utf-8")
            out["saved"] = str(path)
            if isinstance(data, dict):
                out["json_summary"] = {
                    "full_name": data.get("full_name") or data.get("name"),
                    "stars": data.get("stargazers_count"),
                    "license": (data.get("license") or {}).get("spdx_id")
                    if isinstance(data.get("license"), dict)
                    else data.get("license"),
                    "description": (data.get("description") or "")[:200],
                }
        except Exception as e:
            path.write_bytes(body[:40_000])
            out["parse_error"] = str(e)
        return out
    parser = TitleParser()
    try:
        parser.feed(text)
    except Exception:
        pass
    out["title"] = parser.title.strip() or None
    visible = " ".join(parser.visible)
    (OUT / f"{slug}-visible.txt").write_text(visible[:40_000], encoding="utf-8")
    out["visible_len"] = len(visible)
    (OUT / f"{slug}-excerpt.html").write_text(text[:20_000], encoding="utf-8")
    return out


URLS = {
    "gh-reasoning-bank": "https://api.github.com/repos/google-research/reasoning-bank",
    "rb-blog-a": "https://research.google/blog/reasoningbank-scaling-agent-self-evolving-with-reasoning-memory/",
    "rb-blog-b": "https://research.google/blog/reasoningbank/",
    "rb-readme": "https://raw.githubusercontent.com/google-research/reasoning-bank/main/README.md",
    "mem0": "https://mem0.ai",
    "gh-mem0": "https://api.github.com/repos/mem0ai/mem0",
    "letta": "https://www.letta.com",
    "gh-letta": "https://api.github.com/repos/letta-ai/letta",
    "zep": "https://www.getzep.com",
    "gh-graphiti": "https://api.github.com/repos/getzep/graphiti",
    "gorgias": "https://www.gorgias.com",
    "gorgias-cortex": "https://www.gorgias.com/cortex",
}


def main() -> None:
    pages = {}
    for slug, url in URLS.items():
        print(f"GET {slug} {url}", flush=True)
        rec = fetch(url)
        pages[slug] = summarize(rec, slug)
        pages[slug].pop("body", None)
        print(
            f"  -> {pages[slug].get('status')} {pages[slug].get('bytes')} {pages[slug].get('final')} {pages[slug].get('title') or pages[slug].get('json_summary')}",
            flush=True,
        )
        time.sleep(0.4)
    path = Path("/workspace/analysis/_work/captures/leftover20-2026-09-05.json")
    path.write_text(
        json.dumps({"fetched_at": "2026-09-05T08:40:00Z", "pages": pages}, indent=2),
        encoding="utf-8",
    )
    print("wrote", path)


if __name__ == "__main__":
    main()
