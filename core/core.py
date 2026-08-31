"""
MKD Core Integration
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from .system import get_system_info
from .events import EventDispatcher, Event
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

    def queue_event(self, event):
        if not self.runtime.is_running():
            raise RuntimeError("MKD Core is not running")

        if not isinstance(event, Event):
            raise TypeError("queue_event() requires an MKD Event")

        self.runtime.queue_event(event)

    def process_events(self):
        if not self.runtime.is_running():
            raise RuntimeError("MKD Core is not running")

        processed = 0

        while self.runtime.pending_events() > 0:
            self.runtime.process_next(self.events)
            processed += 1

        return processed

    def pending_events(self):
        return self.runtime.pending_events()

    def status(self):
        return {
            "system": self.system,
            "runtime": self.runtime.state,
            "pending_events": self.runtime.pending_events(),
        }
