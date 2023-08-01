from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio import Redis

from app.core.configs.config import config
from app.tgbot.middlewares import DAOMiddleware, L10NMiddleware, ThrottlingMiddleware
from app.infra.utils.create_pool import create_pool


async def main() -> None:
    redis = Redis(
        host=config.REDIS.host,
        port=config.REDIS.port,
        password=config.REDIS.password,
        db=config.REDIS.db
    )
    bot = Bot(
        config.BOT.token,
        parse_mode=ParseMode.HTML
    )
    if config.BOT.skip_updates:
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
    dp['pool'] = await create_pool(config)
    
    dp.update.middleware(DAOMiddleware())
    dp.update.middleware(L10NMiddleware())
    dp.callback_query.middleware(ThrottlingMiddleware())
    dp.message.middleware(ThrottlingMiddleware())
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
