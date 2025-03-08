from enum import Enum

class DocumentType(str, Enum):
    ATTACHMENT = "Attachment"
    CREDITNOTE = "CreditNote"
    DELIVERYNOTE = "DeliveryNote"
    GENERAL = "General"
    INVOICE = "Invoice"
    ORDER = "Order"
    OTHER = "Other"
    PRIVATEATTACHMENT = "PrivateAttachment"

    def __str__(self) -> str:
        return str(self.value)
