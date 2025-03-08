from enum import Enum

class MasterClientFullAddressType(str, Enum):
    CORPORATE_CLIENT = "corporate_client"
    POST_OFFICE_BOX = "post_office_box"
    STREET = "street"

    def __str__(self) -> str:
        return str(self.value)
