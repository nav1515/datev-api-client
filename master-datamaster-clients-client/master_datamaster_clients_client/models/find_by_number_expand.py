from enum import Enum

class FindByNumberExpand(str, Enum):
    NONE = "none"
    ORGANIZATIONS = "organizations"
    VALUE_2 = "*"

    def __str__(self) -> str:
        return str(self.value)
