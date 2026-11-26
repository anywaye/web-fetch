#!/usr/bin/env sh
set -eu

# Install web-fetch (MCP server + CLI) from GitHub.
# Usage: curl -fsSL https://raw.githubusercontent.com/anywaye/web-fetch/master/install.sh | sh

REPO="anywaye/web-fetch"
BRANCH="${WEB_FETCH_BRANCH:-master}"
PY="${PYTHON:-python3}"

# Prefer uv if available, else pipx, else pip --user.
if command -v uv >/dev/null 2>&1; then
  uv tool install "git+https://github.com/${REPO}@${BRANCH}" --force
elif command -v pipx >/dev/null 2>&1; then
  pipx install "git+https://github.com/${REPO}@${BRANCH}" --force
else
  "$PY" -m pip install --user "git+https://github.com/${REPO}@${BRANCH}"
fi

# Install the headless browser used by the rendering tier.
if command -v web-fetch >/dev/null 2>&1; then
  web-fetch --version 2>/dev/null || true
fi
echo "Installing Chromium for patchright (one-time, ~100MB)..."
python3 -m patchright install chromium 2>/dev/null || "$PY" -m patchright install chromium

echo "Installed web-fetch. Add it to your MCP client as:"
echo '  { "command": "web-fetch" }  (stdio)'
