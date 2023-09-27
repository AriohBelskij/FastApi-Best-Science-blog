import uuid as uuid
from sqlalchemy import Column, Integer, String, DateTime, UUID
from sqlalchemy.orm import relationship

from sqlalchemy.sql.functions import now

from src.article.models import Article
from src.comment.models import Comment
from src.database.database import Base


class Author(Base):
    __tablename__ = "authors"

    id: int = Column(Integer, primary_key=True)
    uuid: uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    name: str = Column(String, nullable=False)
    middle_name: str = Column(String, nullable=True)
    surname: str = Column(String, nullable=False)
    created_at: DateTime = Column(
        DateTime(), server_default=now(), nullable=False
    )
    updated_at: DateTime = Column(DateTime(), onupdate=now())
    field: str = Column(String, nullable=False)

    articles = relationship(Article, back_populates="authors")
    comments = relationship(Comment, back_populates="authors")
