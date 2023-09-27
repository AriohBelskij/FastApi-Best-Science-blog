import uuid as uuid
from sqlalchemy import Column, Integer, String, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from src.database.database import Base


class Article(Base):
    __tablename__ = "articles"

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
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE"),
        name="author_article",
    )
    authors = relationship(
        "Author", back_populates="articles", foreign_keys="Article.author_id"
    )

    comments = relationship("Comment", back_populates="articles")
