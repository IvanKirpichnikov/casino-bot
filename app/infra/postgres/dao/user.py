from datetime import datetime

from asyncpg import Connection

from app.core.interfaces.dao.user import AbstractUser


class UserDAO(AbstractUser):
    __slots__ = ('connect',)

    def __init__(self, connect: Connection):
        self.connect = connect

    async def add(self, tid: int, cid: int, dtutc: datetime) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                INSERT INTO users(tid, cid, datetime) VALUES($1, $2, $3)
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
