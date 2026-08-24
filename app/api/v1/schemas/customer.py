from pydantic import BaseModel,ConfigDict
from app.domain.enums import CustomerCategory

class CustomerCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    name:str
    category:CustomerCategory
    address: str
    opening_balance: int

class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id:int
    name:str
    category:CustomerCategory
    address: str
    opening_balance: int