from app.infrastructure.database.models import Customer
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas.customer import CustomerCreate,CustomerResponse
from sqlalchemy import select

async def create_customer(payload: CustomerCreate, db: AsyncSession)->CustomerResponse:
    customer = Customer(
        name = payload.name,
        category = payload.category,
        address = payload.address,
        opening_balance = payload.opening_balance
    )
    
    db.add(customer)
    await db.commit()
    await db.refresh(customer)
    return customer


async def get_customer(id:int, db:AsyncSession):
    result = await db.scalar(select(Customer).where(Customer.id == id))
    return result