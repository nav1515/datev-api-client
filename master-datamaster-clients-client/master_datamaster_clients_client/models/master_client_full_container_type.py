from enum import Enum

class MasterClientFullContainerType(str, Enum):
    INDIVIDUAL_ENTERPRISE = "individual_enterprise"
    LEGAL_PERSON = "legal_person"
    NATURAL_PERSON = "natural_person"
    UNDEFINED = "undefined"

    def __str__(self) -> str:
        return str(self.value)
