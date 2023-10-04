from asyncpg import Connection

from src.core.dto import UserDTO
from src.core.interfaces.dao.referrer import AbstractReferrerDAO


class ReferrerDAO(AbstractReferrerDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def get_my_referrer(self, tid: int) -> UserDTO:
        cursor = await self.connect.cursor(
            '''
            '''
        )
