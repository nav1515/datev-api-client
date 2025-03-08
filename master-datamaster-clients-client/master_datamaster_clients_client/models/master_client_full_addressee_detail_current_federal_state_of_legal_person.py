from enum import Enum

class MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson(str, Enum):
    BAY = "BAY"
    BBG = "BBG"
    BDW = "BDW"
    BER = "BER"
    BGL = "BGL"
    BRE = "BRE"
    HBG = "HBG"
    HES = "HES"
    KTN = "KTN"
    MLB = "MLB"
    NOE = "NOE"
    NRS = "NRS"
    NRW = "NRW"
    OOE = "OOE"
    RLP = "RLP"
    SAA = "SAA"
    SAC = "SAC"
    SAR = "SAR"
    SBG = "SBG"
    STM = "STM"
    SWH = "SWH"
    THG = "THG"
    TIR = "TIR"
    VBG = "VBG"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
