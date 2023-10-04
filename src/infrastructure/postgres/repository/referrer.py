from asyncpg import Connection

from src.application.models.dto import UserDTO
from src.application.interfaces.repository.referrer import AbstractReferrerDAO


class ReferrerDAO(AbstractReferrerDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def get_my_referrer(self, tid: int) -> UserDTO:
        cursor = await self.connect.cursor(
            '''
            '''
        )
