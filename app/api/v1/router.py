from fastapi import APIRouter
from app.api.v1.endpoints import health, item, customer, invoice

api_v1_router = APIRouter()
api_v1_router.include_router(health.router)
api_v1_router.include_router(item.router)
api_v1_router.include_router(customer.router)
api_v1_router.include_router(invoice.router)


# During the interview, add your new endpoint router here:
# from app.api.v1.endpoints import items
# api_v1_router.include_router(items.router)
