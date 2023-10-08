from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.base import Base

if TYPE_CHECKING:
    from .author import Author
    from .comment import Comment

__all__ = ["Article"]


class Article(Base):
    research_field: Mapped[str]
    summary: Mapped[str]
    title: Mapped[str]
    content: Mapped[str]
    status: Mapped[str] = mapped_column(nullable=False, default="self_check")

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="CASCADE")
    )

    author: Mapped["Author"] = relationship(back_populates="articles")

    comments: Mapped[List["Comment"]] = relationship(
        back_populates="article", cascade="all, delete-orphan"
    )
