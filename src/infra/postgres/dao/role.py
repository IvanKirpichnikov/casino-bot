from typing import List

from asyncpg import Connection

from src.core.interfaces.dao.role import AbstractRoleDAO
from src.core.dto import RoleDTO


class RoleDAO(AbstractRoleDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def get_roles(self) -> RoleDTO:
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await connect.cursor('''
                SELECT enum_range(NULL::roles) AS enums:
            ''')
            data = await cursor.fetchrow()
            return RoleDTO()
