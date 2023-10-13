from app.models.author import Author
from repositories.base import BaseRepository


class AuthorRepository(BaseRepository):
    model = Author
