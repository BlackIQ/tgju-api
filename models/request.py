# Libs
from sqlalchemy import Uuid  # SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column  # SQLAlchemy ORM
import uuid  # UUID

# Application
from base.model import BaseModel  # Base Model


# Request
class Request(BaseModel):
    __tablename__ = "requests"

    # Columns
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    request_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        default=uuid.uuid4,
        nullable=False,
        unique=True,
        index=True,
    )
    endpoint: Mapped[str] = mapped_column(
        nullable=False,
    )
    ip_address: Mapped[str | None] = mapped_column(
        nullable=False,
    )
    user_agent: Mapped[str | None] = mapped_column(
        nullable=True,
    )
    client_id: Mapped[str | None] = mapped_column(
        nullable=True,
    )
