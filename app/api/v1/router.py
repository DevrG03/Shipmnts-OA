from fastapi import APIRouter
from app.api.v1.endpoints import health

api_v1_router = APIRouter()
api_v1_router.include_router(health.router)

# During the interview, add your new endpoint router here:
# from app.api.v1.endpoints import items
# api_v1_router.include_router(items.router)
