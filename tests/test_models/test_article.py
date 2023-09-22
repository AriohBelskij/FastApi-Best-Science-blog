from datetime import datetime
from uuid import UUID

import pytest
from sqlalchemy import insert
from sqlalchemy.exc import DBAPIError

from src.article.models import Article


async def test_article_created_with_valid_data(
    get_db, get_article_payload, create_author
):
    query = insert(Article).returning(Article)
    response = await get_db.execute(query, get_article_payload)

    await get_db.commit()

    article_instance = response.scalar_one()

    assert article_instance.id is not None
    assert isinstance(article_instance.uuid, UUID)
    assert article_instance.research_field == "CS"
    assert article_instance.summary == "some text"
    assert article_instance.author_id == 1
    assert isinstance(article_instance.created_at, datetime)


async def test_article_not_create_with_invalid_data(
    get_db, get_article_invalid_payload
):
    with pytest.raises(DBAPIError):
        query = (
            insert(Article)
            .values(**get_article_invalid_payload)
            .returning(Article)
        )
        response = await get_db.execute(query)

        await get_db.commit()
        result = response.scalar_one_or_none()

        assert result is None
