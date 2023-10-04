import asyncpg

from src.application.configs.config import Config


class Postgresql:
    def __init__(self, config: Config) -> None:
        self._config = config
    
    @property
    async def pool(self) -> asyncpg.Pool:
        psql = self._config.work.psql
        return await asyncpg.create_pool(
            user=psql.user,
            password=psql.password,
            database=psql.database,
            host=psql.host,
            port=psql.port
        )
    
    @property
    async def connect(self) -> asyncpg.Connection:
        psql = self._config.work.psql
        return await asyncpg.connect(
            user=psql.user,
            password=psql.password,
            database=psql.database,
            host=psql.host,
            port=psql.port
        )
