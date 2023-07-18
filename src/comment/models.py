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
    __tablename__ = "comment"

    id: int = Column(Integer, primary_key=True)
    uuid: uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    body: str = Column(Text, nullable=False)
    created_at: DateTime = Column(
        DateTime(), server_default=now(), nullable=False
    )
    conclusion: str = Column(String, nullable=True)

    author_id: int = Column(
        Integer, ForeignKey("author.id"), name="author_comment"
    )
    author = relationship("Author", back_populates="comment")

    article_id = Column(
        Integer, ForeignKey("article.id"), name="article_comment"
    )
