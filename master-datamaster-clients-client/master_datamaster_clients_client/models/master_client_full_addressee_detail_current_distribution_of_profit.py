from enum import Enum

class MasterClientFullAddresseeDetailCurrentDistributionOfProfit(str, Enum):
    ANDERER = "ANDERER"
    BRUCH = "BRUCH"
    BRUCHAUTO = "BRUCHAUTO"
    EINKAP = "EINKAP"
    GEZKAP = "GEZKAP"
    KOPFMKOMP = "KOPFMKOMP"
    KOPFOKOMP = "KOPFOKOMP"
    PROZENT = "PROZENT"

    def __str__(self) -> str:
        return str(self.value)
