#!/data/data/com.termux/files/usr/bin/bash

REPO="$HOME/mkd"

echo "MKD — Fully Automatic Development Sync"
echo "======================================"
echo "[MKD] Automatic GitHub synchronization enabled."
echo "[MKD] Watching project for changes..."
echo "[MKD] Press Ctrl+C to stop."

cd "$REPO" || exit 1

LAST_COMMIT="$(git rev-parse HEAD)"
LAST_STATUS="$(git status --porcelain)"

while true; do
    CURRENT_STATUS="$(git status --porcelain)"
    CURRENT_COMMIT="$(git rev-parse HEAD)"

    if [ "$CURRENT_STATUS" != "$LAST_STATUS" ]; then
        if [ -n "$CURRENT_STATUS" ]; then
            echo
            echo "[MKD AUTO-SYNC] Change detected."
            echo "$CURRENT_STATUS"
            echo "[MKD] Waiting for changes to settle..."
            sleep 3

            echo "[MKD] Running synchronization..."
            bash "$REPO/sync.sh"

            CURRENT_STATUS="$(git status --porcelain)"
            CURRENT_COMMIT="$(git rev-parse HEAD)"

            if [ "$CURRENT_COMMIT" != "$LAST_COMMIT" ]; then
                echo "[MKD] Commit created successfully."
                LAST_COMMIT="$CURRENT_COMMIT"
            fi
        fi

        LAST_STATUS="$CURRENT_STATUS"
    fi

    sleep 2
done
