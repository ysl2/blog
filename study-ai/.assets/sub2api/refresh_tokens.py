#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime
from urllib import error, parse, request


BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8080/api/v1")
ADMIN_KEY = os.environ.get(
    "ADMIN_KEY",
    "your-admin-key-here",
)
EXPORT_DIR = os.environ.get("EXPORT_DIR", "~/.vocal/sub2api")
REGION_CHECK_URL = "https://www.cloudflare.com/cdn-cgi/trace"
GOOGLE_CHECK_URL = "https://www.google.com/generate_204"
PRECHECK_TIMEOUT = 5


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


def get_exit_country(timeout=PRECHECK_TIMEOUT):
    try:
        with request.urlopen(REGION_CHECK_URL, timeout=timeout) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except error.URLError as exc:
        print(f"region check failed: {exc.reason}", file=sys.stderr)
        return None
    except TimeoutError as exc:
        print(f"region check failed: {exc}", file=sys.stderr)
        return None

    for line in text.splitlines():
        key, sep, value = line.partition("=")
        if sep and key == "loc":
            return value.strip().upper()

    print("region check failed: country code not found", file=sys.stderr)
    return None


def can_access_google(timeout=PRECHECK_TIMEOUT):
    req = request.Request(
        GOOGLE_CHECK_URL,
        headers={"User-Agent": "refresh_tokens.py/1.0"},
        method="GET",
    )

    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return resp.status < 400
    except error.HTTPError as exc:
        # A Google HTTP response still proves the route reached google.com.
        if exc.code < 500:
            return True
        print(f"google.com check failed: HTTP {exc.code}", file=sys.stderr)
    except error.URLError as exc:
        print(f"google.com check failed: {exc.reason}", file=sys.stderr)
    except TimeoutError as exc:
        print(f"google.com check failed: {exc}", file=sys.stderr)

    return False


def preflight_checks():
    country = get_exit_country()
    if not country:
        print("cannot determine current exit country; skip refresh", file=sys.stderr)
        return 1

    print(f"current exit country: {country}")
    if country == "CN":
        print("current exit country is CN; skip refresh")
        return 0

    if not can_access_google():
        print("google.com is not reachable; skip refresh", file=sys.stderr)
        return 1

    print("google.com reachable")
    return None


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


def ensure_success(resp, action):
    if str(resp.get("code", "")) == "0":
        return True

    print(f"{action} failed:")
    pretty_print(resp)
    return False


def export_all_accounts():
    query = parse.urlencode({"include_proxies": "true"})
    export_url = f"{BASE_URL}/admin/accounts/data?{query}"
    resp = request_json("GET", export_url, ADMIN_KEY)

    if not ensure_success(resp, "export accounts"):
        return 1

    data = resp.get("data")
    if not isinstance(data, dict):
        print("export accounts failed: response data is not an object", file=sys.stderr)
        return 1

    accounts = data.get("accounts")
    proxies = data.get("proxies")
    if not isinstance(accounts, list):
        print("export accounts failed: response data.accounts is not a list", file=sys.stderr)
        return 1
    if proxies is not None and not isinstance(proxies, list):
        print("export accounts failed: response data.proxies is not a list", file=sys.stderr)
        return 1

    export_dir = os.path.expanduser(EXPORT_DIR)
    filename = f"sub2api-account-{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    path = os.path.join(export_dir, filename)

    try:
        os.makedirs(export_dir, exist_ok=True)
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    except OSError as exc:
        print(f"export accounts failed: cannot write {path}: {exc}", file=sys.stderr)
        return 1

    print(f"exported accounts: {len(accounts)}")
    print(f"exported proxies: {len(proxies) if isinstance(proxies, list) else 0}")
    print(f"export file: {path}")
    return 0


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

    if not ensure_success(resp, "list accounts"):
        return 1

    items = resp.get("data", {}).get("items", [])
    account_by_id = {item["id"]: item for item in items if "id" in item}
    account_ids = list(account_by_id.keys())

    if not account_ids:
        print("no matching accounts")
        return export_all_accounts()

    refresh_url = f"{BASE_URL}/admin/accounts/batch-refresh"
    refresh_resp = request_json("POST", refresh_url, ADMIN_KEY, {"account_ids": account_ids})
    add_account_names(refresh_resp, account_by_id)
    pretty_print(refresh_resp)
    if not ensure_success(refresh_resp, "refresh accounts"):
        return 1

    return export_all_accounts()


if __name__ == "__main__":
    preflight_status = preflight_checks()
    if preflight_status is not None:
        sys.exit(preflight_status)

    sys.exit(main())
