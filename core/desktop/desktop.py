DESKTOP_VERSION = "0.1.0"


class Desktop:
    def __init__(self, display, window_manager):
        if display is None:
            raise ValueError("Display is required")

        if window_manager is None:
            raise ValueError("Window manager is required")

        self.display = display
        self.window_manager = window_manager

    def get_display(self):
        return self.display

    def get_window_manager(self):
        return self.window_manager

    def to_dict(self):
        return {
            "version": DESKTOP_VERSION,
            "display": self.display.to_dict(),
            "window_manager": self.window_manager.to_dict(),
        }
