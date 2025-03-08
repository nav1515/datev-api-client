from enum import Enum

class MasterClientFullAddresseeType(str, Enum):
    LEGAL_PERSON = "legal_person"
    NATURAL_PERSON = "natural_person"

    def __str__(self) -> str:
        return str(self.value)
