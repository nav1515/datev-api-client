from enum import Enum

class DocumentTypeCategory(str, Enum):
    INVOICES_RECEIVED = "invoices_received"
    OTHER_DOCUMENTS = "other_documents"
    OUTGOING_INVOICES = "outgoing_invoices"
    PERSONNEL_DOCUMENTS = "personnel_documents"
    TRAVEL_EXPENSE_DOCUMENTS = "travel_expense_documents"

    def __str__(self) -> str:
        return str(self.value)
