from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import get_db
from app.api.v1.schemas.invoice import InvoiceCreate,InvoiceResponse
from app.application.services.invoice_service import create_invoice, submit_invoice

router = APIRouter(prefix="/invoice", tags=["Invoice"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_invoice(payload:InvoiceCreate, db:AsyncSession = Depends(get_db)) -> InvoiceResponse:
    return await create_invoice(payload, db)

@router.post("/{id}/submit", status_code=status.HTTP_200_OK)
async def update_invoice(id=id, db:AsyncSession = Depends(get_db)) -> InvoiceResponse:
    return await submit_invoice(id, db)