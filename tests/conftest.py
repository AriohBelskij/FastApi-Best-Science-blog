import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.database.database import get_async_session, Base, metadata
from src.config import (
    DB_HOST_TEST,
    DB_NAME_TEST,
    DB_PASS_TEST,
    DB_PORT_TEST,
    DB_USER_TEST,
)
from src.main import app

# DATABASE
DATABASE_URL_TEST = (
    f"postgresql+asyncpg://{DB_USER_TEST}:"
    f"{DB_PASS_TEST}@{DB_HOST_TEST}"
    f":{DB_PORT_TEST}/{DB_NAME_TEST}"
)

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(
    engine_test, class_=AsyncSession, expire_on_commit=False
)
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def get_db():
    con = await engine_test.connect()
    transaction = await con.begin()

    async with async_session_maker() as session:
        yield session

    await transaction.rollback()
    await con.close()


def get_author_payload(
    name: str = "John", surname: str = "Doe", field: str = "Cs"
) -> dict:
    return {"name": name, "surname": surname, "field": field}


def get_article_payload(
    research_field: str = "CS",
    summary: str = "some text",
    title: str = "some title",
    content: str = "some content",
    status: str = "self_check",
    author_id: int = 1,
) -> dict:
    return {
        "research_field": research_field,
        "summary": summary,
        "title": title,
        "content": content,
        "status": status,
        "author_id": author_id,
    }


def get_comment_payload(
    body: str = "Some text of comment", author_id: int = 1, article_id: int = 1
) -> dict:
    return {"body": body, "author_id": author_id, "article_id": article_id}
