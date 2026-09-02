from core.window import Window

DESKTOP_VERSION = "0.1.1"


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

    def create_window(self, x, y, width, height, title):
        window = Window(x, y, width, height, title)
        return self.window_manager.create_window(window)

    def get_window(self, window_id):
        return self.window_manager.get_window(window_id)

    def list_windows(self):
        return self.window_manager.list_windows()

    def get_active_window(self):
        return self.window_manager.get_active_window()

    def to_dict(self):
        return {
            "version": DESKTOP_VERSION,
            "display": self.display.to_dict(),
            "window_manager": self.window_manager.to_dict(),
        }
