import uuid as uuid
from sqlalchemy import Column, Integer, String, DateTime, UUID

from sqlalchemy.sql.functions import now
from src.database.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    surname = Column(String, nullable=False)
    created_at = Column(DateTime(), server_default=now(), nullable=False)
    updated_at = Column(DateTime(), onupdate=now())
    field = Column(String, nullable=False)
