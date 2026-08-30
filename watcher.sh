#!/bin/bash

set -e

echo "======================================"
echo "   MKD — Development Watcher"
echo "======================================"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

if [ "$REPO_ROOT" != "$HOME/mkd" ]; then
    echo "[ERROR] Not running inside ~/mkd"
    exit 1
fi

echo "[MKD] Watching project for changes..."
echo "[MKD] Press Ctrl+C to stop."

LAST_STATE="$(git status --porcelain)"

while true; do
    CURRENT_STATE="$(git status --porcelain)"

    if [ "$CURRENT_STATE" != "$LAST_STATE" ]; then
        echo
        echo "[MKD WATCHER] Project change detected."
        echo "--------------------------------------"

        if [ -n "$CURRENT_STATE" ]; then
            echo "$CURRENT_STATE"
        else
            echo "[MKD] Working tree clean."
        fi

        echo "--------------------------------------"
        LAST_STATE="$CURRENT_STATE"
    fi

    sleep 2
done
