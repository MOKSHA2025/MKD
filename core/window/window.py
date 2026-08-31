"""
MKD Window Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

WINDOW_VERSION = "0.1.0"


class Window:
    def __init__(self, x=0, y=0, width=100, height=100, title="MKD Window"):
        if width <= 0 or height <= 0:
            raise ValueError("Window dimensions must be positive")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.visible = True

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def move(self, x, y):
        self.x = x
        self.y = y

    def resize(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Window dimensions must be positive")

        self.width = width
        self.height = height

    def to_dict(self):
        return {
            "version": WINDOW_VERSION,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "title": self.title,
            "visible": self.visible,
        }
