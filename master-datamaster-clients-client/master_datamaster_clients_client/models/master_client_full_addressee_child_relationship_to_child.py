from enum import Enum

class MasterClientFullAddresseeChildRelationshipToChild(str, Enum):
    ADOPT = "ADOPT"
    ENKEL = "ENKEL"
    LEIBL = "LEIBL"
    PFLEG = "PFLEG"
    STIEF = "STIEF"

    def __str__(self) -> str:
        return str(self.value)
