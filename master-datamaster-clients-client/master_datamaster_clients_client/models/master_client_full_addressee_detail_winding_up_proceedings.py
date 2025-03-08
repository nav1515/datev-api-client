from enum import Enum

class MasterClientFullAddresseeDetailWindingUpProceedings(str, Enum):
    IA = "IA"
    IL = "IL"
    INABW = "INABW"
    INLIQ = "INLIQ"

    def __str__(self) -> str:
        return str(self.value)
