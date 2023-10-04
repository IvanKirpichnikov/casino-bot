from asyncpg import Pool
from redis.asyncio.client import Redis
from aiogram import Dispatcher

def setup_data(
    dp: Dispatcher,
    redis: Redis,
    pool: Pool
) -> None:
    dp['redis'] = redis
    dp['pool'] = pool
    