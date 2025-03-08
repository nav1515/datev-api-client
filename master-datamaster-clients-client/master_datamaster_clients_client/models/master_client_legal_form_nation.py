from enum import Enum

class MasterClientLegalFormNation(str, Enum):
    AT = "AT"
    CZ = "CZ"
    DE = "DE"
    ES = "ES"
    FI = "FI"
    GB = "GB"
    LI = "LI"
    PT = "PT"
    SE = "SE"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
