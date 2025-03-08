from enum import Enum

class MasterClientFullAddresseeDetailPaperOfIdentity(str, Enum):
    ES = "ES"
    EZ = "EZ"
    FS = "FS"
    IN = "IN"
    IS = "IS"
    PA = "PA"
    PB = "PB"
    RP = "RP"
    SA = "SA"
    SK = "SK"
    UK = "UK"

    def __str__(self) -> str:
        return str(self.value)
