from enum import Enum

class FindAllOrderby(str, Enum):
    NAME = "name"
    NAMEASC = "name+asc"
    NAMEDESC = "name+desc"
    NUMBER = "number"
    NUMBERASC = "number+asc"
    NUMBERDESC = "number+desc"

    def __str__(self) -> str:
        return str(self.value)
