from enum import Enum

class JobInfoState(str, Enum):
    AUTO_DELETED = "auto-deleted"
    CORRUPTED = "corrupted"
    DELETED = "deleted"
    IMPORTED = "imported"
    UPLOADED = "uploaded"

    def __str__(self) -> str:
        return str(self.value)
