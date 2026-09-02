"""
MKD Window Manager
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

WINDOW_MANAGER_VERSION = "0.1.0"


class WindowManager:
    def __init__(self):
        self._windows = {}
        self._next_id = 1
        self._active_window = None

    def create_window(self, window):
        window_id = self._next_id
        self._next_id += 1

        self._windows[window_id] = window
        self._active_window = window_id

        return window_id

    def get_window(self, window_id):
        return self._windows.get(window_id)

    def destroy_window(self, window_id):
        if window_id not in self._windows:
            return False

        del self._windows[window_id]

        if self._active_window == window_id:
            self._active_window = None

        return True

    def list_windows(self):
        return list(self._windows.keys())

    def get_active_window(self):
        if self._active_window is None:
            return None

        return self._windows.get(self._active_window)

    def set_active_window(self, window_id):
        if window_id not in self._windows:
            return False

        self._active_window = window_id
        return True

    def to_dict(self):
        return {
            "version": WINDOW_MANAGER_VERSION,
            "window_count": len(self._windows),
            "active_window": self._active_window,
        }
