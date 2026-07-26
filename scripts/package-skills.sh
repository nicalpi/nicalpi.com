#!/usr/bin/env bash
# Package the authoring skills as zips for upload to Claude Web
# (claude.ai → Settings → Capabilities → Skills → Upload skill).
# Each zip contains <skill-name>/SKILL.md (+ any reference files).
set -euo pipefail
cd "$(dirname "$0")/.."

SKILLS=(
  field-note-think field-note-write
  progress-think progress-write
  post-think post-write
  social-image
  nicalpi-brand
)

OUT=dist/claude-web-skills
rm -rf "$OUT"
mkdir -p "$OUT"

for name in "${SKILLS[@]}"; do
  src=".claude/skills/$name"
  [ -f "$src/SKILL.md" ] || { echo "skip $name (no SKILL.md)"; continue; }
  (cd .claude/skills && zip -q -r "../../$OUT/$name.zip" "$name" -x '*/.*')
  echo "✓ $OUT/$name.zip"
done
