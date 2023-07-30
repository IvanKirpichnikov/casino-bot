from logging import getLogger

from asyncpg import Connection

from app.core.enums.roles_type import RoleType


logger = getLogger(__name__)

async def _create_users_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'users')
    async with connect.transaction():
        await connect.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                tid BIGINT UNIQUE NOT NULL,
                cid BIGINT UNIQUE NOT NULL,
                role roles,
                datetime TIMESTAMPTZ UNIQUE NOT NULL
            );
        ''')


async def _create_referral_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'refferal')
    async with connect.transaction():
        await connect.execute('''
            CREATE TABLE IF NOT EXISTS referral(
                id INT PRIMARY KEY REFERENCES users ON DELETE CASCADE,
                referrers_count INT DEFAULT 0,
                referral_link TEXT
            );
        ''')

    
async def _create_roles_enum(connect: Connection) -> None:
    logger.debug('Creating type %r', 'roles')
    async with connect.transaction():
        await connect.execute('''
            CREATE TYPE roles AS ENUM $1:
        ''', RoleType.get_all()
        )

async def create(connect: Connection) -> None:
    await _create_roles_enum(connect)
    await _create_users_table(connect)
    await _create_referral_table(connect)
