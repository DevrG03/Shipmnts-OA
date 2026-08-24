from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.infrastructure.database.models import Item
from app.domain.enums import InvoiceStatus

class InvoiceCreate(BaseModel):
    id:str
    customer_id:int
    status: InvoiceStatus
    date: datetime
    items:list[Item]

class InvoiceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id:str
    customer_id:int
    status: InvoiceStatus
    date: datetime
    items:list[Item]
    net_total: float
    total_tax: float
    grand_total: float
    unpaid_amount: float
    status: str

class InvoiceSubmitResponse(BaseModel):
    id:str
    status: InvoiceStatus
    grand_total: float
    unpaid_amount: float
    