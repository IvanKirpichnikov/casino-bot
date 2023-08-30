import logging
from datetime import datetime

from asyncpg import Connection

from app.core.dto import UserLanguageDTO
from app.core.interfaces.dao.user import AbstractUserDAO


logger = logging.getLogger(__name__)


class UserDAO(AbstractUserDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def add(self, tid: int, cid: int, dtutc: datetime) -> None:
        logger.warning(
            'Added user to database. tid=%r, cid=%r',
            tid, cid
        )
        await self.connect.execute(
            '''
                INSERT INTO users(tid, cid, datetime)
                VALUES($1, $2, $3)
                ON CONFLICT DO NOTHING;
            ''',
            tid, cid, dtutc
        )
    
    async def delete(self, tid: int) -> None:
        logger.warning('Delete user. tid=%r', tid)
        await self.connect.execute(
            'DELETE FROM users WHERE tid = $1;',
            tid
        )
    
    async def get_language(self, tid: int) -> UserLanguageDTO:
        # logger.info('')
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await connect.cursor(
                'SELECT language FROM users WHERE tid = $1',
                tid
            )
            data = await cursor.fetchrow()
            return UserLanguageDTO(language=data.get('language'))
    
    async def update_language(self, tid: int, language: str) -> None:
        await self.connect.execute(
            'UPDATE users SET language = $2 WHERE tid = $1;',
            tid, language
        )
