from typing import Any

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model: Any = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_one(self, new_obj: dict) -> model:
        """
        :param new_obj:
        :return: self.model:
        Take dict with new obj args and create this in database"""

        query = insert(self.model).returning(self.model)

        response = await self.session.execute(query, new_obj)

        await self.session.commit()

        return response.scalar()

    ...
