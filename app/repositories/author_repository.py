from app.models.author import Author
from app.repositories.base import BaseRepository


class AuthorRepository(BaseRepository):
    model = Author
