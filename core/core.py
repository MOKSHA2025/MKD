"""
MKD Core Integration
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from .system import get_system_info
from .events import EventDispatcher, Event
from .runtime import Runtime
from .config import Config
from .logging import get_logger


class MKDCore:
    def __init__(self):
        self.logger = get_logger("MKD-CORE")
        self.system = get_system_info()
        self.config = Config()
        self.runtime = Runtime()
        self.events = EventDispatcher()

        self.logger.info("Core initialized")

    def start(self):
        result = self.runtime.start()

        if result:
            self.logger.info("Runtime started")
        else:
            self.logger.warning("Runtime already running")

        return result

    def stop(self):
        result = self.runtime.stop()

        if result:
            self.logger.info("Runtime stopped")
        else:
            self.logger.warning("Runtime already stopped")

        return result

    def queue_event(self, event):
        if not self.runtime.is_running():
            raise RuntimeError("MKD Core is not running")

        if not isinstance(event, Event):
            raise TypeError("queue_event() requires an MKD Event")

        self.runtime.queue_event(event)
        self.logger.info(f"Event queued: {event.event_type}")

    def process_events(self):
        if not self.runtime.is_running():
            raise RuntimeError("MKD Core is not running")

        processed = 0

        while self.runtime.pending_events() > 0:
            self.runtime.process_next(self.events)
            processed += 1

        if processed:
            self.logger.info(f"Events processed: {processed}")

        return processed

    def pending_events(self):
        return self.runtime.pending_events()

    def status(self):
        return {
            "system": self.system,
            "runtime": self.runtime.state,
            "pending_events": self.runtime.pending_events(),
            "config": self.config.to_dict(),
        }
