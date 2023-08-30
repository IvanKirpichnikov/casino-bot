from redis.asyncio import Redis as AioRedis

from app.core.configs.config import Config


class Redis:
    def __init__(self, config: Config) -> None:
        self._config = config
    
    @property
    async def connect(self) -> AioRedis:
        redis = self._config.work.redis
        return AioRedis(
            host=redis.host,
            port=redis.port,
            password=redis.password,
            db=redis.db
        )
