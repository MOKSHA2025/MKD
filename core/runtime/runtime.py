"""
MKD Runtime Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

RUNTIME_VERSION = "0.1.0"

STATE_STOPPED = "stopped"
STATE_RUNNING = "running"


class Runtime:
    def __init__(self):
        self.state = STATE_STOPPED

    def start(self):
        if self.state == STATE_RUNNING:
            return False

        self.state = STATE_RUNNING
        return True

    def stop(self):
        if self.state == STATE_STOPPED:
            return False

        self.state = STATE_STOPPED
        return True

    def is_running(self):
        return self.state == STATE_RUNNING
