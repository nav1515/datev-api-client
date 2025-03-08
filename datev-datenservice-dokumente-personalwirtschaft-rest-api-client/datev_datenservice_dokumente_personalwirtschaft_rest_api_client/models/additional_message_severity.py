from enum import Enum

class AdditionalMessageSeverity(str, Enum):
    ERROR = "error"
    INFORMATION = "information"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
