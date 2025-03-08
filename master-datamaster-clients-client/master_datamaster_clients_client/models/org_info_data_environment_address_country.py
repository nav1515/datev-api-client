from enum import Enum

class OrgInfoDataEnvironmentAddressCountry(str, Enum):
    AT = "AT"
    DE = "DE"

    def __str__(self) -> str:
        return str(self.value)
