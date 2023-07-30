from logging import getLogger

from asyncpg import Connection

from app.core.enums.roles_type import RoleType


logger = getLogger(__name__)

async def _create_users_table(connect: Connection) -> None:
    logger.debug('Create table %r', 'users')
    async with connect.transaction():
        await connect.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL,
                tid BIGINT,
                cid BIGINT,
                role roles,
                datetime TIMESTAMPTZ,
                PRIMARY KEY(id, tid, cid)
            );
        ''')


async def _create_roles_enum(connect: Connection) -> None:
    logger.debug('create type %r', 'roles')
    async with connect.transaction():
        await connect.execute('''
            CREATE TYPE roles AS ENUM $1:
        ''', RoleType.get_all()
        )

async def creates(connect: Connection) -> None:
    await _create_roles_enum(connect)
    await _create_users_table(connect)
