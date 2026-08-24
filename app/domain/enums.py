from enum import StrEnum

class InvoiceStatus(StrEnum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"

class CustomerCategory(StrEnum):
    B2B = "B2B"
    B2C = "B2C"