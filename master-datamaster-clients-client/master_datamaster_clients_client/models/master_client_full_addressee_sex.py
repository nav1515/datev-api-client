from enum import Enum

class MasterClientFullAddresseeSex(str, Enum):
    DIVERSE = "diverse"
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
