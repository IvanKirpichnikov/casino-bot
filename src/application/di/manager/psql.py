from dataclasses import asdict

import asyncpg

from src.application.configs.config import Config


class PostgresqlManager:
    _config: Config
    __slots__ = ('_config',)
    
    def __init__(self, config: Config) -> None:
        self._config = config
    
    @property
    async def pool(self) -> asyncpg.Pool:
        psql = self._config.work.psql
        return await asyncpg.create_pool(**asdict(psql))
    
    @property
    async def connect(self) -> asyncpg.Connection:
        psql = self._config.work.psql
        return await asyncpg.connect(**asdict(psql))
