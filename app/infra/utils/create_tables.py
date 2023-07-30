from asyncpg import Connection

from app.core.enums.roles_type import RoleType


async def _create_users_table(connect: Connection) -> None:
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


async def _create_roles_enum(connect: Connection) -> None:
    async with connect.transaction():
        await connect.execute('''
            CREATE TYPE roles AS ENUM $1:
        ''', RoleType.get_all()
                              )
