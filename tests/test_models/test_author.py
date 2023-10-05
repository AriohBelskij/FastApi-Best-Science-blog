from datetime import datetime
from uuid import UUID
from sqlalchemy import select
from app.models.author import Author


async def test_author_created_with_valid_data(get_db, get_author_payload):
    author = Author(**get_author_payload)
    get_db.add(author)
    await get_db.commit()

    query = select(Author)
    response = await get_db.execute(query)
    author_instance = response.scalar()

    assert author_instance.id is not None
    assert isinstance(author_instance.uuid, UUID)
    assert author_instance.name == "John"
    assert author_instance.middle_name is None
    assert author_instance.field == "CS"
    assert isinstance(author_instance.created_at, datetime)


async def test_authors_generate_with_different_uuid(
    get_db, get_author_payload, create_author
):
    author = Author(**get_author_payload)
    get_db.add(author)
    await get_db.commit()

    assert author.uuid != create_author.uuid
