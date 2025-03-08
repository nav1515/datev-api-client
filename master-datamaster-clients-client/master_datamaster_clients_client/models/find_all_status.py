from enum import Enum

class FindAllStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
