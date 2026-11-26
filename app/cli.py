"""CLI entry point for web-fetch.

Usage:
  web-fetch                       # run as MCP server over stdio (default)
  web-fetch --http                # run as HTTP MCP server (remote mode)
  web-fetch fetch <url>           # one-shot fetch, prints markdown to stdout
"""
from __future__ import annotations

import argparse
import asyncio
import sys


def _run_stdio() -> None:
    from .server import mcp

    mcp.run()


def _run_http() -> None:
    import os

    os.execvp("python", ["python", "main.py"])  # delegate to legacy remote entrypoint


def _one_shot(url: str, **kwargs) -> int:
    from . import fetch

    async def _go():
        result = await fetch.fetch_markdown(url, **kwargs)
        import json

        print(json.dumps(result, indent=2) if isinstance(result, dict) else result)

    asyncio.run(_go())
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="web-fetch")
    sub = parser.add_subparsers(dest="cmd")

    p_fetch = sub.add_parser("fetch", help="Fetch a URL and print the result")
    p_fetch.add_argument("url")
    p_fetch.add_argument("--selector", default=None)
    p_fetch.add_argument("--max-chars", type=int, default=None)
    p_fetch.add_argument("--offset", type=int, default=0)
    p_fetch.add_argument("--headless", action="store_true", default=True)

    parser.add_argument("--http", action="store_true", help="Run HTTP MCP server instead of stdio")
    parser.add_argument("--version", action="store_true")

    args = parser.parse_args(argv)

    if args.version:
        from . import config

        print(config.VERSION)
        return 0

    if args.http:
        _run_http()
        return 0

    if args.cmd == "fetch":
        kwargs = {"selector": args.selector, "offset": args.offset}
        if args.max_chars is not None:
            kwargs["max_chars"] = args.max_chars
        kwargs["headless"] = args.headless
        return _one_shot(args.url, **kwargs)

    # default: stdio MCP server
    _run_stdio()
    return 0


if __name__ == "__main__":
    sys.exit(main())
