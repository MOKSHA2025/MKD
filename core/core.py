"""
MKD Core Integration
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from .system import get_system_info
from .events import EventDispatcher
from .runtime import Runtime


class MKDCore:
    def __init__(self):
        self.system = get_system_info()
        self.runtime = Runtime()
        self.events = EventDispatcher()

    def start(self):
        return self.runtime.start()

    def stop(self):
        return self.runtime.stop()

    def status(self):
        return {
            "system": self.system,
            "runtime": self.runtime.state,
        }
