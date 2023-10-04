from dataclasses import asdict
from typing import Optional

from aiogram.fsm.storage.redis import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.application.configs.config import Config


class RedisManager:
    _config: Config
    _redis: Redis
    __slots__ = ('_config', '_redis')
    
    def __init__(self, config: Config) -> None:
        self._config: Config = config
        self._redis: Optional[Redis] = None
    
    @property
    async def connect(self) -> Redis:
        redis = self._config.work.redis
        if self._redis is None:
            self._redis = Redis(**asdict(redis))
        return self._redis
    
    @property
    def aiogram_fsm_storage(self) -> RedisStorage:
        if self._redis is None:
            raise ValueError("No created Redis connect")
        
        return RedisStorage(
            self._redis,
            key_builder=DefaultKeyBuilder(with_destiny=True)
        )
