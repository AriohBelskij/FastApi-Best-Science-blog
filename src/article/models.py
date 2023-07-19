import uuid as uuid
from sqlalchemy import Column, Integer, String, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from src.database.database import Base


class Article(Base):
    __tablename__ = "article"

    id: int = Column(Integer, primary_key=True, nullable=False)
    uuid: uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    research_field: str = Column(String, nullable=False)
    summary: str = Column(String, nullable=False)
    created_at: DateTime = Column(
        DateTime(), server_default=now(), nullable=False
    )
    updated_at: DateTime = Column(DateTime(), onupdate=now())
    title: str = Column(String, nullable=False)
    content: str = Column(String, nullable=False)
    status: str = Column(String, nullable=False, default="self_check")

    author_id: int = Column(
        Integer, ForeignKey("author.id"), name="author_article"
    )
    author = relationship("Author", back_populates="article")

    comment = relationship(
        "Comment",
        back_populates="article",
        uselist=False,
        cascade="all, delete-orphan",
    )
