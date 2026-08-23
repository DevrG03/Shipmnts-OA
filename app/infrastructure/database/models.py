# Import all ORM models here so Alembic detects them for autogenerate migrations
from app.infrastructure.database.base import Base  # noqa: F401

# Example: When you create a model during the interview:
# from app.infrastructure.database.user_model import UserModel  # noqa: F401
