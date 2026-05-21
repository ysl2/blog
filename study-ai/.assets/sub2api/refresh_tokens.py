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
ACCOUNT_PAGE_SIZE = 1000


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
            if account is None:
                normalized_id = normalize_account_id(account_id)
                if normalized_id is not None:
                    account = account_by_id.get(normalized_id)
            row["account_name"] = account.get("name", "") if account else ""


def ensure_success(resp, action):
    if str(resp.get("code", "")) == "0":
        return True

    print(f"{action} failed:")
    pretty_print(resp)
    return False


def normalize_account_id(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        value = value.strip()
        if value.isdigit():
            return int(value)
    return None


def string_value(value):
    return value.strip() if isinstance(value, str) else ""


def list_all_oauth_accounts():
    page = 1
    total = None
    accounts = []
    seen_ids = set()

    while True:
        query = parse.urlencode(
            {
                "page": page,
                "page_size": ACCOUNT_PAGE_SIZE,
                "type": "oauth",
            }
        )
        list_url = f"{BASE_URL}/admin/accounts?{query}"
        resp = request_json("GET", list_url, ADMIN_KEY)

        if not ensure_success(resp, "list accounts"):
            return None

        data = resp.get("data")
        if not isinstance(data, dict):
            print("list accounts failed: response data is not an object", file=sys.stderr)
            return None

        items = data.get("items")
        if not isinstance(items, list):
            print("list accounts failed: response data.items is not a list", file=sys.stderr)
            return None

        if total is None:
            try:
                total = int(data.get("total"))
            except (TypeError, ValueError):
                total = None

        for item in items:
            if not isinstance(item, dict):
                continue
            account_id = normalize_account_id(item.get("id"))
            if account_id is None or account_id in seen_ids:
                continue
            seen_ids.add(account_id)
            item["id"] = account_id
            accounts.append(item)

        if not items:
            break
        if total is not None and len(accounts) >= total:
            break
        page += 1

    print(f"matching oauth accounts: {len(accounts)}")
    return accounts


def export_all_accounts():
    query = parse.urlencode({"include_proxies": "true"})
    export_url = f"{BASE_URL}/admin/accounts/data?{query}"
    resp = request_json("GET", export_url, ADMIN_KEY)

    if not ensure_success(resp, "export accounts"):
        return 1, None

    data = resp.get("data")
    if not isinstance(data, dict):
        print("export accounts failed: response data is not an object", file=sys.stderr)
        return 1, None

    accounts = data.get("accounts")
    proxies = data.get("proxies")
    if not isinstance(accounts, list):
        print("export accounts failed: response data.accounts is not a list", file=sys.stderr)
        return 1, None
    if proxies is not None and not isinstance(proxies, list):
        print("export accounts failed: response data.proxies is not a list", file=sys.stderr)
        return 1, None

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
        return 1, None

    print(f"exported accounts: {len(accounts)}")
    print(f"exported proxies: {len(proxies) if isinstance(proxies, list) else 0}")
    print(f"export file: {path}")
    return 0, data


def print_non_free_openai_emails(export_data):
    accounts = export_data.get("accounts") if isinstance(export_data, dict) else None
    if not isinstance(accounts, list):
        print("list non-free failed: exported accounts is not a list", file=sys.stderr)
        return

    emails = []
    seen_emails = set()
    openai_oauth_count = 0
    missing_plan_accounts = []

    for account in accounts:
        if not isinstance(account, dict):
            continue

        platform = string_value(account.get("platform")).lower()
        account_type = string_value(account.get("type")).lower()
        if platform != "openai" or account_type != "oauth":
            continue

        openai_oauth_count += 1
        account_label = string_value(account.get("name")) or f"id:{account.get('id', 'unknown')}"
        credentials = account.get("credentials")
        if not isinstance(credentials, dict):
            missing_plan_accounts.append(account_label)
            continue

        email = string_value(credentials.get("email"))
        plan_type = string_value(credentials.get("plan_type"))

        if not plan_type:
            missing_plan_accounts.append(account_label)
        if not email or not plan_type:
            continue
        if plan_type.lower() == "free":
            continue

        email_key = email.lower()
        if email_key in seen_emails:
            continue
        seen_emails.add(email_key)
        emails.append(email)

    print()
    print(f"{'total openai oauth':<19}: {openai_oauth_count}")
    print(f"{'non-free emails':<19}: {len(emails)}")
    print(f"{'missing plan_type':<19}: {len(missing_plan_accounts)}")

    print()
    print("non-free emails:")
    if emails:
        for email in emails:
            print(f"  {email}")
    else:
        print("  none")

    print()
    print("missing plan_type accounts:")
    if missing_plan_accounts:
        for account in missing_plan_accounts:
            print(f"  {account}")
    else:
        print("  none")


def main():
    accounts = list_all_oauth_accounts()
    if accounts is None:
        return 1

    account_by_id = {item["id"]: item for item in accounts if "id" in item}
    account_ids = list(account_by_id.keys())

    if account_ids:
        refresh_url = f"{BASE_URL}/admin/accounts/batch-refresh"
        refresh_resp = request_json("POST", refresh_url, ADMIN_KEY, {"account_ids": account_ids})
        add_account_names(refresh_resp, account_by_id)
        pretty_print(refresh_resp)
        if not ensure_success(refresh_resp, "refresh accounts"):
            return 1
    else:
        print("no matching oauth accounts")

    export_status, export_data = export_all_accounts()
    if export_status != 0:
        return export_status

    print_non_free_openai_emails(export_data)
    return 0


if __name__ == "__main__":
    preflight_status = preflight_checks()
    if preflight_status is not None:
        sys.exit(preflight_status)

    sys.exit(main())
