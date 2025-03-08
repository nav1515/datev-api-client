from enum import Enum

class FindAllIsConsultantClient(str, Enum):
    OF_ACTIVE_CORPORATE_STRUCTURE = "of-active-corporate-structure"

    def __str__(self) -> str:
        return str(self.value)
