# Import all ORM models here so Alembic detects them for autogenerate migrations
from alembic.util import status
from app.infrastructure.database.base import Base  # noqa: F401

# Example: When you create a model during the interview:
# from app.infrastructure.database.user_model import UserModel  # noqa: F401

from sqlalchemy import String, Float, CheckConstraint, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from app.domain.enums import CustomerCategory, InvoiceStatus
from app.domain.exceptions import ValidationDomainError
from datetime import datetime

# Customer 
# id
# Name
# Category
# Address
# Opening_balance



class Customer(Base):
    __tablename__ = "customers"

    id:Mapped[int] = mapped_column(primary_key = "True")
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    category:Mapped[CustomerCategory] = mapped_column(String(8), nullable=False)
    address:Mapped[str] = mapped_column(String(500), nullable =False)
    opening_balance:Mapped[float] = mapped_column(Float(2),nullable =False)

    __table_args__ = (
        CheckConstraint("opening_balance >= 0", name="check_balance_positive"),
    )

    @validates("opening_balance")
    def constraint_balance(self,key,val):
        if val <= 0:
            raise ValidationDomainError(f"{key} must be greater than or equal to 0.")
        return val

    # Relationships
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="customer")


class Item(Base):
    __tablename__ = "items"

    id:Mapped[int] = mapped_column(primary_key = "True")
    unit_price:Mapped[float] = mapped_column(Float(2))
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    tax: Mapped[int] = mapped_column(Integer,nullable =False)

    __table_args__ = (
        CheckConstraint("tax >= 0 and  tax <= 28", name="check_tax"),
    )

    @validates("tax")
    def constraint_balance(self,key,val):
        if val <= 0:
            raise ValidationDomainError(f"{key} must be greater than or equal to 0 and less than or equal to 28.")
        return val

    invoices: Mapped[list["Invoice"]] = relationship(back_populates="items")
    

# Invoice
# Id
# cutomer_id(FK->customer)
# Items
# Item_id
# Unit_price
# qnty
# Status (Enum)
# timestamp


class Invoice(Base):
    __tablename__ = "invoices"

    id:Mapped[str] = mapped_column(primary_key = "True")
    customer_id:Mapped[int] = mapped_column(ForeignKey("customers.id"))
    status: Mapped[InvoiceStatus] = mapped_column(String(32), nullable=False, server_default = InvoiceStatus.DRAFT)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())

    # Relationship
    items:Mapped[list["Item"]] = relationship(
        back_populates="invoices",
    )
    