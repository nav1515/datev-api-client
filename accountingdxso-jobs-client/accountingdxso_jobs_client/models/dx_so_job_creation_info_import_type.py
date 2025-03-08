from enum import Enum

class DXSoJobCreationInfoImportType(str, Enum):
    ACCOUNTSPAYABLELEDGERIMPORT = "accountsPayableLedgerImport"
    ACCOUNTSRECEIVABLELEDGERIMPORT = "accountsReceivableLedgerImport"
    CASHLEDGERIMPORT = "cashLedgerImport"

    def __str__(self) -> str:
        return str(self.value)
