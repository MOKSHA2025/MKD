"""
MKD Runtime Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from collections import deque

RUNTIME_VERSION = "0.2.0"

STATE_STOPPED = "stopped"
STATE_RUNNING = "running"


class Runtime:
    def __init__(self):
        self.state = STATE_STOPPED
        self.event_queue = deque()

    def start(self):
        if self.state == STATE_RUNNING:
            return False

        self.state = STATE_RUNNING
        return True

    def stop(self):
        if self.state == STATE_STOPPED:
            return False

        self.state = STATE_STOPPED
        self.event_queue.clear()
        return True

    def is_running(self):
        return self.state == STATE_RUNNING

    def queue_event(self, event):
        if not self.is_running():
            raise RuntimeError("MKD Runtime is not running")

        self.event_queue.append(event)

    def process_next(self, dispatcher):
        if not self.is_running():
            raise RuntimeError("MKD Runtime is not running")

        if not self.event_queue:
            return 0

        event = self.event_queue.popleft()
        return dispatcher.dispatch(event)

    def pending_events(self):
        return len(self.event_queue)
