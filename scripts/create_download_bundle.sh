#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/downloads"
OUT_FILE="$OUT_DIR/mergepdf_project.zip"

mkdir -p "$OUT_DIR"
rm -f "$OUT_FILE"

cd "$ROOT_DIR"
zip -r "$OUT_FILE" README.md pyproject.toml requirements.txt src .gitignore >/dev/null

echo "Created: $OUT_FILE"
