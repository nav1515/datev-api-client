from enum import Enum

class MasterClientFullContainerTransparencyRegister(str, Enum):
    DISCREPANCIES_FOUND = "discrepancies_found"
    ENTRIES_CORRECT = "entries_correct"
    NO_INSPECTION = "no_inspection"

    def __str__(self) -> str:
        return str(self.value)
