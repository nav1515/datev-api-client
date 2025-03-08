from enum import Enum

class MasterClientFullMarriageStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
