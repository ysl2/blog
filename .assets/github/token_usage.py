#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request


API = "https://api.github.com"


def utc_from_epoch(value):
    if not value:
        return None
    return dt.datetime.fromtimestamp(value, dt.timezone.utc).isoformat()


def request_json(method, url, token, body=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-token-status-check",
        "Authorization": f"Bearer {token}",
    }
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            text = resp.read().decode("utf-8")
            return resp.status, dict(resp.headers), json.loads(text) if text else None
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            payload = {"raw": text}
        return exc.code, dict(exc.headers), payload


def print_rate_resource(name, item):
    if not item:
        print(f"{name}: missing")
        return
    print(f"{name}:")
    print(f"  limit:     {item.get('limit')}")
    print(f"  used:      {item.get('used')}")
    print(f"  remaining: {item.get('remaining')}")
    print(f"  reset:     {utc_from_epoch(item.get('reset'))}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""))
    parser.add_argument("--probe-graphql", action="store_true")
    args = parser.parse_args()

    token = args.token.strip()
    if not token:
        print("Missing token. Use --token ... or set GITHUB_TOKEN.", file=sys.stderr)
        return 2

    status, headers, user = request_json("GET", f"{API}/user", token)
    print("User check:")
    print(f"  status: {status}")
    print(f"  login:  {user.get('login') if isinstance(user, dict) else None}")
    print(f"  id:     {user.get('id') if isinstance(user, dict) else None}")
    print(f"  scopes: {headers.get('x-oauth-scopes')}")
    print(f"  header core limit:     {headers.get('x-ratelimit-limit')}")
    print(f"  header core remaining: {headers.get('x-ratelimit-remaining')}")
    print()

    status, headers, payload = request_json("GET", f"{API}/rate_limit", token)
    print("Rate limit:")
    print(f"  status: {status}")
    resources = payload.get("resources", {}) if isinstance(payload, dict) else {}
    print_rate_resource("core", resources.get("core"))
    print_rate_resource("graphql", resources.get("graphql"))
    print_rate_resource("search", resources.get("search"))
    print()

    core = resources.get("core") or {}
    graphql = resources.get("graphql") or {}
    if status == 200:
        if core.get("limit") == 60:
            print("WARNING: REST core limit is 60, which looks like unauthenticated-level quota.")
        if graphql.get("limit") == 0:
            print("WARNING: GraphQL limit is 0, so GraphQL is currently unusable for this token.")

    if args.probe_graphql:
        query = {"query": "{ viewer { login } rateLimit { limit cost used remaining resetAt } }"}
        status, _headers, payload = request_json("POST", f"{API}/graphql", token, query)
        print()
        print("GraphQL probe:")
        print(f"  status: {status}")
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    raise SystemExit(main())
