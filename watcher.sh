#!/data/data/com.termux/files/usr/bin/bash

REPO="$HOME/mkd"

echo "MKD — Fully Automatic Development Sync"
echo "======================================"
echo "[MKD] Automatic GitHub synchronization enabled."
echo "[MKD] Watching project for changes..."
echo "[MKD] Press Ctrl+C to stop."

cd "$REPO" || exit 1

LAST_STATE=""

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
            bash "$REPO/sync.sh"

            echo "[MKD] Sync cycle complete."
        fi

        LAST_STATE="$(git status --porcelain)"
    fi

    sleep 2
done
