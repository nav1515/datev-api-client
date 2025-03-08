from enum import Enum

class MasterClientFullAddresseeDetailCurrentMaritalStatus(str, Enum):
    GS = "GS"
    GT = "GT"
    LE = "LE"
    PA = "PA"
    PE = "PE"
    PL = "PL"
    VH = "VH"
    VW = "VW"

    def __str__(self) -> str:
        return str(self.value)
