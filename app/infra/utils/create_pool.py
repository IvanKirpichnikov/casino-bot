from asyncpg import Pool, create_pool as pool

from app.core.configs.config import Config


async def create_pool(config: Config) -> Pool:
    psql = config.PSQL
    return pool(
        user=psql.user,
        password=psql.password,
        database=psql.database,
        host=psql.host,
        port=psql.port
    )
