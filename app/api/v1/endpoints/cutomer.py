from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db
from app.api.v1.schemas.customer import CustomerCreate,CustomerResponse
from app.application.services.customer_service import create_customer, get_customer

router = APIRouter(prefix="/cutomer", tags=["Customer"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_customer(payload:CustomerCreate, db:AsyncSession = Depends(get_db)) -> CustomerResponse:
    return await create_customer(payload, db)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def fetch_customer(id:int, db:AsyncSession = Depends(get_db)) -> CustomerResponse:
    return await get_customer(id, db)