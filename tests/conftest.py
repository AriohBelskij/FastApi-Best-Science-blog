import asyncio
from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.core.database import get_async_session, Base, metadata
from app.core.config import (
    DB_HOST_TEST,
    DB_NAME_TEST,
    DB_PASS_TEST,
    DB_PORT_TEST,
    DB_USER_TEST,
)
from app.main import app

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
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop


@pytest.fixture(scope="session")
async def get_db():
    connection = await engine_test.connect()
    transaction = await connection.begin()
    async_session_maker.configure(bind=connection)

    async with async_session_maker() as session:
        yield session

    await transaction.rollback()
    await connection.close()
