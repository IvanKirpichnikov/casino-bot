from datetime import datetime

from asyncpg import Connection

from app.infra.postgresql.dao.base import BaseDAO


class UserDAO(BaseDAO):
    __slots__ = ('connect',)

    def __init__(self, connect: Connection):
        self.connect = connect

    async def create_table(self) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id SERIAL,
                    tid BIGINT,
                    cid BIGINT,
                    role SMALLINT REFERENCES roles(name) ON DELETE CASCADE,
                    datetime TIMESTAMPTZ,
                    PRIMARY KEY(id, tid, cid, datetime)
                );
            ''')

    async def add(self, tid: int, cid: int, datetimeutc: datetime) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                INSERT INTO users(tid, cid, datetime) VALUES($1, $2, $3)
                ON CONFLICT DO NOTHING;
            ''', tid, cid, datetimeutc
            )

    async def delete(self, tid: int) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                DELETE FROM users WHERE tid = $1;
            ''', tid
            )
