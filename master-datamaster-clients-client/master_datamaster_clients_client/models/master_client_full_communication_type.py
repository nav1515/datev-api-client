from enum import Enum

class MasterClientFullCommunicationType(str, Enum):
    EMAIL = "email"
    FAX = "fax"
    OTHER = "other"
    PHONE = "phone"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
