from typing import Generic, TypeVar
from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    message: str


class StandardResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T
    message: str = "Operation successful"


class PaginatedResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(from_attributes=True)

    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int
