from typing import Tuple

from asyncpg import Connection

from app.infra.postgresql.dao.base import BaseDAO


class RoleDAO(BaseDAO):
    __slots__ = ('connect',)

    def __init__(self, connect: Connection):
        self.connect = connect

    async def create_type(self, role_names: Tuple[str]) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                CREATE TYPE roles AS ENUM $1;
            ''', role_names
            )
