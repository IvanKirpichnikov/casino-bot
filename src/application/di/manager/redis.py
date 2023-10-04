from typing import Optional

from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from redis.asyncio import Redis as AioRedis

from src.application.configs.config import Config


class Redis:
    def __init__(self, config: Config) -> None:
        self._config: Config = config
        self._redis: Optional[AioRedis] = None
    
    @property
    async def connect(self) -> AioRedis:
        redis = self._config.work.redis
        self._redis = AioRedis(
            host=redis.host,
            port=redis.port,
            password=redis.password,
            db=redis.db
        )
        return self._redis
    
    @property
    def aiogram_storage(self) -> RedisStorage:
        if self._redis is None:
            raise ValueError("No created Redis connect")
        
        return RedisStorage(
            self._redis,
            key_builder=DefaultKeyBuilder(with_destiny=True)
        )
