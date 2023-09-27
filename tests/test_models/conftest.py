import pytest
from sqlalchemy import insert

from app.models.article import Article
from app.models.author import Author


@pytest.fixture(scope="session")
def get_author_payload() -> dict:
    return {"name": "John", "surname": "Doe", "field": "CS"}


@pytest.fixture(scope="session")
def get_author_invalid_payload() -> dict:
    return {"name": 1, "surname": "Doe", "field": 235}


@pytest.fixture(scope="session")
def get_article_payload() -> dict:
    return {
        "research_field": "CS",
        "summary": "some text",
        "title": "some title",
        "content": "some content",
        "status": "self_check",
        "author_id": 1,
    }


@pytest.fixture(scope="session")
def get_article_invalid_payload() -> dict:
    return {
        "research_field": 1,
        "summary": "some text",
        "title": None,
        "content": "some content",
        "status": 1,
        "author_id": 1,
    }


@pytest.fixture(scope="session")
def get_comment_payload() -> dict:
    return {"body": "Some text of comment", "author_id": 1, "article_id": 1}


@pytest.fixture(scope="session")
def get_invalid_comment_payload() -> dict:
    return {"body": 666, "author_id": 1, "article_id": 1}


@pytest.fixture(scope="session")
async def create_author(get_db, get_author_payload):
    query = insert(Author).returning(Author)
    response = await get_db.execute(query, get_author_payload)
    return response.scalar_one()


@pytest.fixture(scope="session")
async def create_article(get_db, create_author, get_article_payload):
    query = insert(Article).returning(Article)
    response = await get_db.execute(query, get_article_payload)
    return response.scalar_one()
