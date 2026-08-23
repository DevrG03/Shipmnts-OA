from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db

# Wire shared dependencies here using Depends(get_db)
# Example during interview:
# def get_item_repository(db: AsyncSession = Depends(get_db)) -> ItemRepository:
#     return ItemRepository(db)
#
# def get_item_service(repo: ItemRepository = Depends(get_item_repository)) -> ItemService:
#     return ItemService(repo)
