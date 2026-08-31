"""
MKD Error Core
MOKSHA KERNEL DESKTOP EXPERIMENT
"""

ERROR_VERSION = "0.1.0"


class MKDError(Exception):
    """Base exception for MKD."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "message": self.message,
        }


class MKDCoreError(MKDError):
    """General MKD core error."""


class MKDRuntimeError(MKDCoreError):
    """Runtime lifecycle or execution error."""


class MKDEventError(MKDCoreError):
    """Event processing error."""


class MKDConfigurationError(MKDCoreError):
    """Configuration error."""
