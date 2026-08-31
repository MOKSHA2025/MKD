"""
MKD Configuration Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

CONFIG_VERSION = "0.1.0"


class Config:
    def __init__(self):
        self._values = {
            "system.name": "MOKSHA KERNEL DESKTOP EXPERIMENT",
            "system.version": "0.1.0",
            "runtime.mode": "development",
            "runtime.debug": True,
        }

    def get(self, key, default=None):
        return self._values.get(key, default)

    def set(self, key, value):
        self._values[key] = value

    def has(self, key):
        return key in self._values

    def to_dict(self):
        return dict(self._values)
