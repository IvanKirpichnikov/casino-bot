from contextlib import suppress
import logging

from asyncpg import Connection, Pool, DuplicateObjectError

from app.core.enums import RolesType


logger = logging.getLogger(__name__)


async def _create_users_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'users')
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            tid BIGINT UNIQUE NOT NULL,
            cid BIGINT UNIQUE NOT NULL,
            language VARCHAR(2) DEFAULT 'en',
            role ROLES,
            datetime TIMESTAMPTZ UNIQUE NOT NULL
        );
    ''')


async def _create_referrers_table(connect: Connection) -> None:
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS referrers(
            id INT PRIMARY KEY REFERENCES users ON DELETE CASCADE,
            referrer_id INT REFERENCES referrals(id) ON DELETE CASCADE
        );
    ''')


async def _create_referrals_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'referral')
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS referrals(
            id INT PRIMARY KEY REFERENCES users ON DELETE CASCADE,
            referrers_count INT DEFAULT 0,
            deep_link TEXT
        );
    ''')


async def _create_roles_enum(connect: Connection) -> None:
    logger.debug('Creating type %r', 'roles')
    await connect.execute('''
        CREATE TYPE roles AS ENUM {};
    '''.format(tuple(RolesType.get_all()))
    )


async def create_postgres_data(pool: Pool) -> None:
    async with pool.acquire() as connect:
        with suppress(DuplicateObjectError):
            await _create_roles_enum(connect)
        await _create_referrals_table(connect)
        await _create_users_table(connect)
        await _create_referrers_table(connect)
