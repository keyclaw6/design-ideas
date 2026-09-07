#!/usr/bin/env python3
"""Parse `tnr status --json`. Prints STATUS\\tIP\\tPORT. Handles list or id→item map."""
from __future__ import annotations

import json
import sys


def items_from(data):
    if isinstance(data, list):
        return data
    if not isinstance(data, dict):
        return []
    if "instances" in data:
        return data["instances"] if isinstance(data["instances"], list) else list(data["instances"].values())
    if "data" in data and isinstance(data["data"], list):
        return data["data"]
    # map of identifier -> InstanceListItem
    out = []
    for k, v in data.items():
        if isinstance(v, dict) and ("status" in v or "uuid" in v or "gpuType" in v or "id" in v):
            row = dict(v)
            row.setdefault("id", k)
            out.append(row)
        elif k in {"id", "uuid", "status"}:
            return [data]
    return out


def match(it: dict, iid: str) -> bool:
    sid = str(it.get("id") or it.get("instance_id") or it.get("identifier") or it.get("num") or it.get("index") or "")
    uuid = str(it.get("uuid") or "")
    return sid == iid or uuid == iid or str(it.get("num")) == iid or str(it.get("index")) == iid


def main() -> None:
    iid = sys.argv[1]
    raw = sys.stdin.read().strip() or "{}"
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(2)
    for it in items_from(data):
        if not isinstance(it, dict) or not match(it, iid):
            continue
        st = str(it.get("status") or it.get("state") or "").upper()
        ip = it.get("ip") or it.get("publicIp") or it.get("public_ip") or it.get("ssh_host") or ""
        if ip is None:
            ip = ""
        port = it.get("ssh_port") or it.get("port") or 22
        print(f"{st}\t{ip}\t{port}")
        sys.exit(0 if st == "RUNNING" and ip else 1)
    sys.exit(1)


if __name__ == "__main__":
    main()
