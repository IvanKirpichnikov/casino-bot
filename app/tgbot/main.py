from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs
from asyncpg import create_pool
from redis.asyncio import Redis

from app.core.configs.config import config
from app.tgbot.middlewares import DAOMiddleware, L10NMiddleware, ThrottlingMiddleware
from app.tgbot.utils.get_translator_hub import get_translator_hub
from app.tgbot.dialogs.register import register_dialogs


async def main() -> None:
    pool = await create_pool(
        user=config.psql.user,
        password=config.psql.password,
        database=config.psql.database,
        host=config.psql.host,
        port=config.psql.port
    )
    redis = Redis(
        host=config.redis.host,
        port=config.redis.port,
        password=config.redis.password,
        db=config.redis.db
    )
    bot = Bot(
        config.bot.token,
        parse_mode=ParseMode.HTML
    )
    if config.bot.skip_updates:
        await bot.delete_webhook(drop_pending_updates=True)
    
    storage = RedisStorage(
        redis,
        key_builder=DefaultKeyBuilder(with_destiny=True)
    )
    dp = Dispatcher(
        storage=storage,
        events_isolation=storage.create_isolation()
    )
    
    dp['redis'] = redis
    dp['pool'] = pool
    dp['_hub'] = get_translator_hub()
    
    dp.update.middleware(DAOMiddleware())
    dp.update.middleware(L10NMiddleware())
    dp.callback_query.middleware(ThrottlingMiddleware())
    dp.message.middleware(ThrottlingMiddleware())
    
    setup_dialogs(dp)
    register_dialogs(dp)
    
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await pool.close()
