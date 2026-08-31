"""
MKD Logging Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

LOGGING_VERSION = "0.1.0"

LEVEL_INFO = "INFO"
LEVEL_WARNING = "WARNING"
LEVEL_ERROR = "ERROR"


class Logger:
    def __init__(self, name="MKD"):
        self.name = name

    def _log(self, level, message):
        print(f"[{level}] [{self.name}] {message}")

    def info(self, message):
        self._log(LEVEL_INFO, message)

    def warning(self, message):
        self._log(LEVEL_WARNING, message)

    def error(self, message):
        self._log(LEVEL_ERROR, message)


def get_logger(name="MKD"):
    return Logger(name)
