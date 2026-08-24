from app.api.v1.schemas.item import ItemCreate, ItemResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.models import Item

async def create_item(payload:ItemCreate, db:AsyncSession) -> ItemResponse:
    item = Item(
        name = payload.name,
        tax = payload.tax
    )

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item