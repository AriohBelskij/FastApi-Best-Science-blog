import pytest
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
    author = Author(**get_author_payload)

    get_db.add(author)
    await get_db.commit()

    return author


@pytest.fixture(scope="session")
async def create_article(get_db, create_author, get_article_payload):
    article = Article(**get_article_payload)

    get_db.add(article)
    await get_db.commit()

    return article
