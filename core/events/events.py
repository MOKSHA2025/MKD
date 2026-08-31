"""
MKD Event Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

EVENT_SYSTEM = "MKD_EVENT_CORE"
EVENT_VERSION = "0.2.0"

EVENT_KEYBOARD = "keyboard"
EVENT_MOUSE = "mouse"
EVENT_SYSTEM_EVENT = "system"

SUPPORTED_EVENTS = {
    EVENT_KEYBOARD,
    EVENT_MOUSE,
    EVENT_SYSTEM_EVENT,
}


class Event:
    def __init__(self, event_type, data=None):
        if event_type not in SUPPORTED_EVENTS:
            raise ValueError(
                f"Unsupported MKD event type: {event_type}"
            )

        self.event_type = event_type
        self.data = data

    def to_dict(self):
        return {
            "type": self.event_type,
            "data": self.data,
        }


def create_event(event_type, data=None):
    return Event(event_type, data)
