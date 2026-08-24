from pydantic import BaseModel, DictConfig

class ItemCreate(BaseModel):
    name:str
    tax:int

class ItemResponse(BaseModel):
    model_config = DictConfig(from_attributes=True)

    id:int
    name:str
    tax:int