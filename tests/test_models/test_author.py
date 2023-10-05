from datetime import datetime
from uuid import UUID

import pytest
from sqlalchemy import insert
from sqlalchemy.exc import DBAPIError

from app.models.author import Author


async def test_author_created_with_valid_data(get_db, get_author_payload):
    query = insert(Author).returning(Author)
    response = await get_db.execute(query, get_author_payload)
    await get_db.commit()
    author_instance = response.scalar_one()

    assert author_instance.id is not None
    assert isinstance(author_instance.uuid, UUID)
    assert author_instance.name == "John"
    assert author_instance.middle_name is None
    assert author_instance.field == "CS"
    assert isinstance(author_instance.created_at, datetime)


async def test_author_not_create_with_invalid_data(
    get_db, get_author_invalid_payload
):
    with pytest.raises(DBAPIError):
        query = insert(Author).returning(Author)
        response = await get_db.execute(query, get_author_invalid_payload)

        await get_db.commit()
        result = response.scalar_one_or_none()

        assert result is None
