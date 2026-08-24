from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db
from app.api.v1.schemas.item import ItemCreate,ItemResponse
from app.application.services.item_service import create_item

router = APIRouter(prefix="/item", tags=["Item"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_item(payload:ItemCreate, db:AsyncSession = Depends(get_db)) -> ItemResponse:
    return await create_item(payload, db)

