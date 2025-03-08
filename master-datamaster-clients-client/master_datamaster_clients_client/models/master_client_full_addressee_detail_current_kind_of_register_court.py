from enum import Enum

class MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt(str, Enum):
    FIR = "FIR"
    GEN = "GEN"
    GES = "GES"
    GRB = "GRB"
    GRU = "GRU"
    HAN = "HAN"
    PAR = "PAR"
    PRT = "PRT"
    VER = "VER"

    def __str__(self) -> str:
        return str(self.value)
