#!/usr/bin/env python3
"""Read X auth_token + ct0 from Cursor browser partition SQLite.

Usage:
  python3 scripts/x_extract_cookies.py              # print export lines
  python3 scripts/x_extract_cookies.py --inject       # agent-browser cookies set
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

PARTITION = Path.home() / ".config/Cursor/Partitions/cursor-browser/Cookies"
NAMES = ("auth_token", "ct0")


def read_cookies(db_path: Path) -> dict[str, str]:
    tmp = Path("/tmp/cursor-cookies-copy")
    shutil.copy2(db_path, tmp)
    con = sqlite3.connect(tmp)
    out: dict[str, str] = {}
    for name in NAMES:
        row = con.execute(
            "SELECT value FROM cookies WHERE name=? AND host_key LIKE '%x.com%' LIMIT 1",
            (name,),
        ).fetchone()
        if row:
            out[name] = row[0]
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inject", action="store_true", help="inject via agent-browser")
    parser.add_argument("--partition", type=Path, default=PARTITION)
    args = parser.parse_args()

    if not args.partition.exists():
        print(f"Cookie DB not found: {args.partition}", file=sys.stderr)
        sys.exit(1)

    cookies = read_cookies(args.partition)
    missing = [n for n in NAMES if n not in cookies]
    if missing:
        print(f"Missing cookies: {missing}", file=sys.stderr)
        sys.exit(1)

    auth, ct0 = cookies["auth_token"], cookies["ct0"]
    print(f"export X_AUTH_TOKEN='{auth}'")
    print(f"export X_CT0='{ct0}'")

    if args.inject:
        cdp = os.environ.get("BU_CDP_URL")
        if not cdp:
            print("Set BU_CDP_URL for --inject", file=sys.stderr)
            sys.exit(1)
        ab = shutil.which("agent-browser") or "agent-browser"
        for tab in ("x", "t9"):
            subprocess.run([ab, "tab", tab], capture_output=True)
        subprocess.run([ab, "cookies", "set", "auth_token", auth, "--domain", ".x.com"], check=True)
        subprocess.run([ab, "cookies", "set", "ct0", ct0, "--domain", ".x.com"], check=True)
        print("Injected auth_token + ct0 into agent-browser", file=sys.stderr)


if __name__ == "__main__":
    main()
