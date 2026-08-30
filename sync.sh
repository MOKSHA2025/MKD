#!/bin/bash

set -e

echo "======================================"
echo "   MKD — Git Synchronization"
echo "======================================"

# Ensure we are inside the MKD repository
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

if [ "$REPO_ROOT" != "$HOME/mkd" ]; then
    echo "[ERROR] Not running inside ~/mkd"
    exit 1
fi

echo "[MKD] Checking repository status..."

if [ -z "$(git status --porcelain)" ]; then
    echo "[MKD] No changes detected."
    exit 0
fi

echo "[MKD] Changes detected:"
git status --short

echo
echo "[MKD] Staging changes..."
git add .

echo "[MKD] Creating commit..."
git commit -m "sync: MKD development update $(date '+%Y-%m-%d %H:%M:%S')"

echo "[MKD] Pushing to GitHub..."
git push origin main

echo
echo "[MKD] Synchronization complete."
echo "======================================"
