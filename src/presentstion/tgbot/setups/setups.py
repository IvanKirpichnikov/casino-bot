from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs
from asyncpg import Pool
from fluentogram import TranslatorHub
from redis.asyncio.client import Redis

from src.presentstion.tgbot.dialogs.register import register_dialogs
from src.presentstion.tgbot.setups import setup_inner_middleware
from src.presentstion.tgbot.setups.data import setup_data


def setups(
    dp: Dispatcher,
    pool: Pool,
    redis: Redis,
    hub: TranslatorHub
) -> None:
    setup_data(dp, redis, pool)
    setup_inner_middleware(dp, pool, hub)
    setup_dialogs(dp)
    register_dialogs(dp)
