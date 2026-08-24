import uuid
from select import select
from app.api.v1.schemas.invoice import InvoiceCreate, InvoiceResponse, InvoiceSubmitResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.models import Invoice
from app.domain.enums import InvoiceStatus

async def create_invoice(payload: InvoiceCreate, db: AsyncSession)->InvoiceResponse:
    invoice = Invoice(
        id = str(uuid.uuid4()),
        customer_id = payload.customer_id,
        status = payload.status,
        items = payload.items,
    )

    db.add(invoice)
    await db.commit()
    await db.refresh(invoice)
    return invoice

async def submit_invoice(id:int, db:AsyncSession) -> InvoiceSubmitResponse:
    invoice = await db.scalar(select(Invoice).where(Invoice.id == id))
    invoice.net_total = sum(item.unit_price * item.qnty for item in invoice.items)
    invoice.tax = invoice.net_total * (item.tax / 100 for item in invoice.items)
    invoice.grand_total = invoice.net_total + invoice.tax
    invoice.unpaid_amount = invoice.grand_total - invoice.customer.opening_balance
    invoice.status = InvoiceStatus.SUBMITTED

    result = InvoiceSubmitResponse(
        id = invoice.id,
        status = invoice.status,
        grand_total = invoice.grand_total,
        unpaid_amount = invoice.unpaid_amount
    )

    await db.commit()
    await db.refresh(invoice)
    return result
    