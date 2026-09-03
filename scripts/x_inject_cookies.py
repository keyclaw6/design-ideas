#!/usr/bin/env python3
"""Inject X session cookies into agent-browser Chrome via CDP.

Usage:
  export BU_CDP_URL=http://127.0.0.1:PORT
  export X_AUTH_TOKEN='...' X_CT0='...'
  python3 scripts/x_inject_cookies.py

Get values from a browser where you are logged into X:
  DevTools → Application → Cookies → https://x.com → auth_token, ct0
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
import uuid

try:
    import websocket
except ImportError:
    print("pip install websocket-client", file=sys.stderr)
    raise


def cdp_url() -> str:
    base = os.environ.get("BU_CDP_URL", "").rstrip("/")
    if not base:
        print("Set BU_CDP_URL to agent-browser Chrome CDP", file=sys.stderr)
        sys.exit(1)
    return base


def connect(ws_url: str):
    ws = websocket.create_connection(ws_url, timeout=10)
    mid = 0

    def send(method: str, params: dict | None = None):
        nonlocal mid
        mid += 1
        ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg.get("result", {})

    return ws, send


def main() -> None:
    auth = os.environ.get("X_AUTH_TOKEN", "").strip()
    ct0 = os.environ.get("X_CT0", "").strip()
    if not auth or not ct0:
        print("Set X_AUTH_TOKEN and X_CT0 env vars", file=sys.stderr)
        sys.exit(1)

    base = cdp_url()
    pages = json.loads(urllib.request.urlopen(f"{base}/json/list", timeout=5).read())
    page = next((p for p in pages if p.get("type") == "page"), None)
    if not page:
        print("No CDP page target found", file=sys.stderr)
        sys.exit(1)

    ws, send = connect(page["webSocketDebuggerUrl"])
    send("Network.enable")
    for name, value in (("auth_token", auth), ("ct0", ct0)):
        send(
            "Network.setCookie",
            {
                "name": name,
                "value": value,
                "domain": ".x.com",
                "path": "/",
                "secure": True,
                "httpOnly": name == "auth_token",
                "sameSite": "None",
            },
        )
    send("Page.navigate", {"url": "https://x.com/i/bookmarks"})
    ws.close()
    print("Cookies injected; navigated to bookmarks. Verify login in browser.")


if __name__ == "__main__":
    main()
