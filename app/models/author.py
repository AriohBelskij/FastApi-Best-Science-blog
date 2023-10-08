from typing import List, Optional, TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models import Base

if TYPE_CHECKING:
    from .article import Article
    from .comment import Comment

__all__ = ["Author"]


class Author(Base):
    name: Mapped[str]
    middle_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    surname: Mapped[str]
    field: Mapped[str]

    articles: Mapped[List["Article"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    comments: Mapped[List["Comment"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )
