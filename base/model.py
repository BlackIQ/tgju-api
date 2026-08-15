# Libs
from sqlalchemy import DateTime, func  # SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # SQLAlchemy ORM
from datetime import datetime  # Datetime


# Base Class: Model
class BaseModel(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
