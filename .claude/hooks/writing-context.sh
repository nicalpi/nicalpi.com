#!/usr/bin/env bash
# SessionStart hook: lean writing-pipeline state so every session opens knowing
# what is queued and what is mid-flight. No network, under 10 lines of output.
set -u
cd "${CLAUDE_PROJECT_DIR:-$(pwd)}" 2>/dev/null || exit 0
mem=.writings-memory
[ -d "$mem" ] || exit 0

open=$(grep -c '^- \[ \]' "$mem/ideas.md" 2>/dev/null); open=${open:-0}
shipped=$(grep -c '^- \[x\]' "$mem/ideas.md" 2>/dev/null); shipped=${shipped:-0}
echo "[writing] ideas: $open open · $shipped shipped · /quick-log to add"

for dir in "$mem"/*/; do
  [ -d "$dir" ] || continue
  slug=$(basename "$dir")
  case "$slug" in research|drafts) continue ;; esac
  stage="outline"
  next="/writing-plan $slug"
  if [ -f "$dir/plan.md" ]; then
    stage="plan"; next="/writing-post $slug"
    grep -q '^status: drafting' "$dir/plan.md" 2>/dev/null && stage="drafting"
  fi
  if [ -f "$dir/outline.md" ] && grep -A1 '^## Reader' "$dir/outline.md" 2>/dev/null | grep -q '_pending_'; then
    stage="outline (unapproved)"; next="/writing-outline $slug"
  fi
  echo "[writing] in flight: $slug · $stage · next: $next"
done

echo "[writing] flow: /quick-log → /writing-outline → /writing-plan → /writing-post · target 2 posts/week"
exit 0
