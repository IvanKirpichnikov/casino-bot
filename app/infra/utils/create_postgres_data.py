import logging

from asyncpg import Connection, Pool


logger = logging.getLogger(__name__)


async def _create_users_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'users')
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id       SERIAL      PRIMARY KEY,
            tid      BIGINT      UNIQUE NOT NULL,
            cid      BIGINT      UNIQUE NOT NULL,
            language VARCHAR(2)  DEFAULT 'en',
            datetime TIMESTAMPTZ UNIQUE NOT NULL,
            role     TEXT
        );
    ''')


async def _create_referrers_table(connect: Connection) -> None:
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS referrers(
            PRIMARY KEY (id),
            id          INT REFERENCES users ON DELETE CASCADE,
            referrer_id INT REFERENCES referrals(id) ON DELETE CASCADE
        );
    ''')


async def _create_referrals_table(connect: Connection) -> None:
    logger.debug('Creating table %r', 'referral')
    await connect.execute('''
        CREATE TABLE IF NOT EXISTS referrals(
            PRIMARY KEY (id),
            id              INT REFERENCES users ON DELETE CASCADE,
            referrers_count INT DEFAULT 0,
            deep_link       TEXT
        );
    ''')


async def create_postgres_data(pool: Pool) -> None:
    async with pool.acquire() as connect:
        await _create_users_table(connect)
        await _create_referrals_table(connect)
        await _create_referrers_table(connect)
