from uuid import UUID

import pytest
from sqlalchemy import insert
from sqlalchemy.exc import DBAPIError

from src.comment.models import Comment


async def test_comment_created_with_valid_data(
    get_db, get_comment_payload, create_article
):
    query = insert(Comment).returning(Comment)
    response = await get_db.execute(query, get_comment_payload)
    await get_db.commit()
    comment_instance = response.scalar_one()

    assert comment_instance.id is not None
    assert isinstance(comment_instance.uuid, UUID)
    assert comment_instance.body == "Some text of comment"


async def test_comment_not_create_with_invalid_data(
    get_db, get_invalid_comment_payload, create_article
):
    with pytest.raises(DBAPIError):
        query = insert(Comment).returning(Comment)
        response = await get_db.execute(query, get_invalid_comment_payload)

        await get_db.commit()
        result = response.scalar_one_or_none()

        assert result is None
