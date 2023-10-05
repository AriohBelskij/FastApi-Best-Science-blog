from uuid import UUID
from sqlalchemy import select
from app.models.comment import Comment


async def test_comment_created_with_valid_data(
    get_db, get_comment_payload, create_article
):
    comment = Comment(**get_comment_payload)
    get_db.add(comment)
    await get_db.commit()

    query = select(Comment)
    response = await get_db.execute(query)

    comment_instance = response.scalar()

    assert comment_instance.id is not None
    assert isinstance(comment_instance.uuid, UUID)
    assert comment_instance.body == "Some text of comment"
