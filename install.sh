#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "ERROR: python3 not found. Please install Python 3 and retry."
  exit 1
fi

echo "Creating virtual environment..."
"$PYTHON_BIN" -m venv .venv

echo "Upgrading pip..."
"./.venv/bin/python" -m pip install --upgrade pip

echo "Installing requirements..."
"./.venv/bin/python" -m pip install -r requirements.txt

echo "Launching MP3 Downloader GUI..."
"./.venv/bin/python" "mp3_downloader_gui.py"
