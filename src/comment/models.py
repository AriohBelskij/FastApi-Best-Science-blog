import uuid as uuid
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UUID,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship

from sqlalchemy.sql.functions import now

from src.database.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id: int = Column(Integer, primary_key=True, index=True)
    uuid: uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    body: str = Column(Text, nullable=False)
    created_at: DateTime = Column(
        DateTime(), server_default=now(), nullable=False
    )
    conclusion: str = Column(String, nullable=True)

    author_id: int = Column(
        Integer,
        ForeignKey("author.id", ondelete="CASCADE"),
        name="author_comment",
    )
    author = relationship("Author", back_populates="comments")

    article_id = Column(
        Integer,
        ForeignKey("article.id", ondelete="CASCADE"),
        name="article_comment",
    )
    article = relationship("Article", back_populates="comments")
