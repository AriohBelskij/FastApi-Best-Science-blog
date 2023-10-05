from datetime import datetime
from uuid import UUID

from sqlalchemy import select


from app.models.article import Article


async def test_article_created_with_valid_data(
    get_db, get_article_payload, create_author
):
    article = Article(**get_article_payload)
    get_db.add(article)
    await get_db.commit()

    query = select(Article)
    response = await get_db.execute(query)

    article_instance = response.scalar()

    assert article_instance.id is not None
    assert isinstance(article_instance.uuid, UUID)
    assert article_instance.research_field == "CS"
    assert article_instance.summary == "some text"
    assert article_instance.author_id == 1
    assert isinstance(article_instance.created_at, datetime)
