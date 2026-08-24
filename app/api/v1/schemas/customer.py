from pydantic import BaseModel,ConfigDict
from app.domain.enums import CustomerCategory

class CustomerCreate(BaseModel):
    name:str
    category:CustomerCategory
    address: str
    opening_balance: int

class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:int
    name:str
    category:CustomerCategory
    address: str
    opening_balance: int