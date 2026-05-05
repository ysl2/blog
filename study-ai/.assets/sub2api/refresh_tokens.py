#!/usr/bin/env python3
import json
import os
import sys
from urllib import error, parse, request


BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8080/api/v1")
ADMIN_KEY = os.environ.get(
    "ADMIN_KEY",
    "your-admin-key-here",
)


def pretty_print(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def request_json(method, url, admin_key, payload=None):
    headers = {"x-api-key": admin_key}
    body = None

    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode("utf-8")

    req = request.Request(url, data=body, headers=headers, method=method)

    try:
        with request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
    except error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        print(f"request failed: HTTP {exc.code}", file=sys.stderr)
        if message:
            print(message, file=sys.stderr)
        sys.exit(1)
    except error.URLError as exc:
        print(f"request failed: {exc.reason}", file=sys.stderr)
        sys.exit(1)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print("request failed: response is not valid JSON", file=sys.stderr)
        print(raw, file=sys.stderr)
        sys.exit(1)


def add_account_names(result, account_by_id):
    data = result.get("data", {})
    if not isinstance(data, dict):
        return

    for key in ("errors", "warnings"):
        rows = data.get(key)
        if not isinstance(rows, list):
            continue

        for row in rows:
            if not isinstance(row, dict):
                continue

            account_id = row.get("account_id")
            account = account_by_id.get(account_id)
            row["account_name"] = account.get("name", "") if account else ""


def main():
    query = parse.urlencode(
        {
            "page": 1,
            "page_size": 1000,
            "type": "oauth",
        }
    )
    list_url = f"{BASE_URL}/admin/accounts?{query}"

    resp = request_json("GET", list_url, ADMIN_KEY)

    if str(resp.get("code", "")) != "0":
        print("list accounts failed:")
        pretty_print(resp)
        return 1

    items = resp.get("data", {}).get("items", [])
    account_by_id = {item["id"]: item for item in items if "id" in item}
    account_ids = list(account_by_id.keys())

    if not account_ids:
        print("no matching accounts")
        return 0

    refresh_url = f"{BASE_URL}/admin/accounts/batch-refresh"
    refresh_resp = request_json("POST", refresh_url, ADMIN_KEY, {"account_ids": account_ids})
    add_account_names(refresh_resp, account_by_id)
    pretty_print(refresh_resp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
