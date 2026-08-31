"""
MKD Event Dispatcher
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from .events import Event


class EventDispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, event_type, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    def dispatch(self, event):
        if not isinstance(event, Event):
            raise TypeError("dispatch() requires an MKD Event")

        handlers = self._handlers.get(event.event_type, [])

        for handler in handlers:
            handler(event)

        return len(handlers)
