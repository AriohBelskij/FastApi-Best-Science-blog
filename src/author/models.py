import uuid as uuid
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime

from sqlalchemy_utils import UUIDType
from src.database.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    surname = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    updated_at = Column(TIMESTAMP, nullable=True, default=datetime.now)
    field = Column(String, nullable=False)
