from app.models.comment import Comment
from app.repositories.base import BaseRepository


class CommentRepository(BaseRepository):
    model = Comment
