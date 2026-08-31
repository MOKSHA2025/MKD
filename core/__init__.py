"""
MKD Core Package
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

from .core import MKDCore

from .system import (
    MKD_NAME,
    MKD_VERSION,
    MKD_STATUS,
    get_system_info,
)

from .events import (
    EVENT_SYSTEM,
    EVENT_VERSION,
    EVENT_KEYBOARD,
    EVENT_MOUSE,
    EVENT_SYSTEM_EVENT,
    SUPPORTED_EVENTS,
    Event,
    create_event,
    EventDispatcher,
)

from .runtime import (
    RUNTIME_VERSION,
    STATE_STOPPED,
    STATE_RUNNING,
    Runtime,
)

from .config import (
    CONFIG_VERSION,
    Config,
)

from .logging import (
    LOGGING_VERSION,
    Logger,
    get_logger,
)

from .errors import (
    ERROR_VERSION,
    MKDError,
    MKDCoreError,
    MKDRuntimeError,
    MKDEventError,
    MKDConfigurationError,
)

__all__ = [
    "MKDCore",

    "MKD_NAME",
    "MKD_VERSION",
    "MKD_STATUS",
    "get_system_info",

    "EVENT_SYSTEM",
    "EVENT_VERSION",
    "EVENT_KEYBOARD",
    "EVENT_MOUSE",
    "EVENT_SYSTEM_EVENT",
    "SUPPORTED_EVENTS",
    "Event",
    "create_event",
    "EventDispatcher",

    "RUNTIME_VERSION",
    "STATE_STOPPED",
    "STATE_RUNNING",
    "Runtime",

    "CONFIG_VERSION",
    "Config",

    "LOGGING_VERSION",
    "Logger",
    "get_logger",

    "ERROR_VERSION",
    "MKDError",
    "MKDCoreError",
    "MKDRuntimeError",
    "MKDEventError",
    "MKDConfigurationError",
]
