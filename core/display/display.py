"""
MKD Display Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

DISPLAY_VERSION = "0.1.0"


class Display:
    def __init__(self, width=640, height=480):
        if width <= 0 or height <= 0:
            raise ValueError("Display dimensions must be positive")

        self.width = width
        self.height = height
        self._buffer = [
            [0 for _ in range(width)]
            for _ in range(height)
        ]

    def set_pixel(self, x, y, value=1):
        self._validate_coordinates(x, y)
        self._buffer[y][x] = value

    def get_pixel(self, x, y):
        self._validate_coordinates(x, y)
        return self._buffer[y][x]

    def clear(self, value=0):
        for y in range(self.height):
            for x in range(self.width):
                self._buffer[y][x] = value

    def _validate_coordinates(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(
                f"Pixel coordinates out of bounds: ({x}, {y})"
            )

    def to_dict(self):
        return {
            "version": DISPLAY_VERSION,
            "width": self.width,
            "height": self.height,
        }
