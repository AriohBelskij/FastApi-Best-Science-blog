from app.models.article import Article
from app.repositories.base import BaseRepository


class ArticleRepository(BaseRepository):
    model = Article
