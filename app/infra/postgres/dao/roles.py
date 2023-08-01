from typing import List

from asyncpg import Connection

from app.core.interfaces.dao.roles import AbstractRole
from app.core.dto.roles import RolesDTO


class RoleDAO(AbstractRole):
    __slots__ = ('connect',)

    def __init__(self, connect: Connection):
        self.connect = connect

    async def get(self) -> RolesDTO:
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await connect.cursor('''
                SELECT enum_range(NULL::roles):
            ''')
            data = await cursor.fetchrow()
            return RolesDTO()

