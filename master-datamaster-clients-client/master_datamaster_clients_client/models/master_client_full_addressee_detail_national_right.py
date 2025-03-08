from enum import Enum

class MasterClientFullAddresseeDetailNationalRight(str, Enum):
    AT = "AT"
    DE = "DE"

    def __str__(self) -> str:
        return str(self.value)
