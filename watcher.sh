#!/data/data/com.termux/files/usr/bin/bash

echo "MKD — Fully Automatic Development Sync"
echo "======================================"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"

if [ "$REPO_ROOT" != "$HOME/mkd" ]; then
    echo "[ERROR] Not running inside ~/mkd"
    exit 1
fi

echo "[MKD] Automatic GitHub synchronization enabled."
echo "[MKD] Watching project for changes..."
echo "[MKD] Press Ctrl+C to stop."

LAST_STATE="$(git status --porcelain)"

while true; do
    CURRENT_STATE="$(git status --porcelain)"

    if [ "$CURRENT_STATE" != "$LAST_STATE" ]; then
        if [ -n "$CURRENT_STATE" ]; then
            echo
            echo "[MKD AUTO-SYNC] Change detected."
            echo "$CURRENT_STATE"
            echo "[MKD] Waiting for changes to settle..."
            sleep 3
            echo "[MKD] Synchronizing with GitHub..."
            ./sync.sh
        fi

        LAST_STATE="$(git status --porcelain)"
    fi

    sleep 2
done
