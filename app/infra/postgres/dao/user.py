from datetime import datetime

from asyncpg import Connection

from app.core.dto import UserLanguageDTO
from app.core.enums import LanguagesType
from app.core.interfaces.dao.user import AbstractUserDAO


class UserDAO(AbstractUserDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def add(self, tid: int, cid: int, dtutc: datetime) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                INSERT INTO users(tid, cid, datetime)
                VALUES($1, $2, $3)
                ON CONFLICT DO NOTHING;
            ''', tid, cid, dtutc
            )
    
    async def delete(self, tid: int) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                DELETE FROM users WHERE tid = $1;
            ''', tid
            )
    
    async def get_language(self, tid: int) -> UserLanguageDTO:
        cursor = await self.connect.cursor('''
            SELECT language FROM users
            WHERE tid = $1
        ''', tid
        )
        data = await cursor.fetchrow()
        return UserLanguageDTO(language=data.get('language'))
    
    async def update_language(self, tid: int, lang_code: str) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                UPDATE users SET language = $1
                WHERE tid = $2;
            ''')
