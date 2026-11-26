# Changelog

## 0.1.0 (2026-11-26)

### Features
- Initial release of `web-fetch`, forked from Cyphid-Academy/Render-Fetch-MCP.
- Four-tier fetch pipeline: content negotiation (Accept: text/markdown) → plain HTTP + trafilatura → curl_cffi TLS impersonation → patchright headless Chromium.
- Structured envelope response: `content`, `tier_used`, `identity_mode`, `final_url`, `http_status`, `content_ok`, `truncated`, `next_offset`, `title`, `description`, `language`, `hint`, `timings_ms`.
- `content_ok` heuristics for bot walls, login walls, JS shells, parked domains, and implausibly short content, each with an actionable `hint`.
- Pagination via `offset` + `max_chars` with `next_offset`.
- CSS `selector` scoping across all tiers.
- `capture_page` tool for vision-ready screenshot tiling.
- stdio MCP server (default) and CLI (`web-fetch fetch <url>`).
- SSRF guards with manual redirect vetting; browser subresource guarding.
- Parked-domain detection (registrar parking pages).
- PDF text extraction (pypdf).
- Title/description/language metadata extraction via trafilatura.
- Headless/headed toggle.

### Notes
- Not yet published to PyPI (`web-fetch` name is taken); install via the curl installer or `pip install git+https://github.com/anywaye/web-fetch`.
