from enum import Enum

class MasterClientFullAddresseeDetailCurrentConsideration(str, Enum):
    ARBEITSU = "ARBEITSU"
    AUSBILDG = "AUSBILDG"
    BEHINDERG = "BEHINDERG"
    FEHLAUSB = "FEHLAUSB"
    FREIDST = "FREIDST"
    FREIWEHR = "FREIWEHR"
    GRDDST = "GRDDST"
    UEBERGANG = "UEBERGANG"

    def __str__(self) -> str:
        return str(self.value)
