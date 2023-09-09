from datetime import datetime
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.author.models import Author
from src.article.models import Article
from src.comment.models import Comment
from tests.conftest import (
    get_author_payload,
    get_article_payload,
    get_comment_payload,
)


async def get_instance_from_table(
    model: Any, session: AsyncSession, id_: int = 1
) -> Any:
    query = select(model).where(model.id == id_)
    result = await session.execute(query)

    object_instance = result.scalar_one()
    return object_instance


async def create_obj_in_table(
    model: Any, session: AsyncSession, payload: dict
) -> Any:
    obj = model(**payload)
    session.add(obj)
    await session.commit()
    return await get_instance_from_table(model, session)


async def check_object_properties(obj) -> None:
    assert obj is not None
    assert obj.uuid is not None
    assert obj.id is not None
    assert isinstance(obj.created_at, datetime)


async def test_author_table_created(get_db):
    author_instance = await create_obj_in_table(
        model=Author, session=get_db, payload=get_author_payload()
    )
    await check_object_properties(author_instance)


async def test_article_table_created(get_db):
    article_instance = await create_obj_in_table(
        model=Article, session=get_db, payload=get_article_payload()
    )

    await check_object_properties(article_instance)


async def test_comment_table_created(get_db):
    comment_instance = await create_obj_in_table(
        model=Comment, session=get_db, payload=get_comment_payload()
    )

    await check_object_properties(comment_instance)
    assert comment_instance.article_id == 1
    assert comment_instance.author_id == 1
