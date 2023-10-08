from datetime import datetime
from typing import Optional

from sqlalchemy import UUID, DateTime
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)
import uuid as uuid

from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    """# noqa
    Base class for all models. Using the __abstract__ method, we restrict the creation of an instance
     of a class. Using the @declared_attr.directive decorator, we declare the __tablename__ method,
      which sets the table name for all child classes based on the name of the child class, making
       it plural.
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[uuid] = mapped_column(
        UUID(as_uuid=True), nullable=False, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime, onupdate=now(), nullable=True
    )
