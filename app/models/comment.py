from typing import Optional, TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models import Base

if TYPE_CHECKING:
    from .author import Author
    from .article import Article

__all__ = ["Comment"]


class Comment(Base):
    body: Mapped[str] = mapped_column(Text(), nullable=False)
    conclusion: Mapped[Optional[str]] = mapped_column(nullable=True)

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="CASCADE"), name="autor_comment"
    )
    author: Mapped["Author"] = relationship(back_populates="comments")

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id", ondelete="CASCADE"), name="article_comment"
    )
    article: Mapped["Article"] = relationship(back_populates="comments")
