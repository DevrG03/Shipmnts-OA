from pydantic import BaseModel, ConfigDict

class ItemCreate(BaseModel):
    name:str
    tax:int

class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id:int
    name:str
    tax:int