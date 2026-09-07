#!/usr/bin/env python3
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from parse_tnr_create import parse
from parse_tnr_status import items_from, match


def test_create_identifier():
    raw = json.dumps({"identifier": 0, "uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee", "key": "-----BEGIN OPENSSH PRIVATE KEY-----\nabc\n-----END OPENSSH PRIVATE KEY-----"})
    d = parse(raw)
    assert d["TNR_INDEX"] == "0"
    assert d["INSTANCE_ID"] == "0"
    assert d["HAS_KEY"] == "1"


def test_status_map():
    data = {"0": {"id": "0", "uuid": "u-1", "status": "RUNNING", "ip": "1.2.3.4", "port": 22}}
    items = items_from(data)
    assert match(items[0], "0")
    assert match(items[0], "u-1")


def test_status_list():
    data = [{"id": "3", "uuid": "u-3", "status": "STARTING", "ip": None, "port": 22}]
    items = items_from(data)
    assert match(items[0], "3")


if __name__ == "__main__":
    test_create_identifier()
    test_status_map()
    test_status_list()
    print("ok")
