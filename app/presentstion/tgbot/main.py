from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from aiogram_dialog import setup_dialogs

from app.core.configs.config import get_config
from app.core.di.manager import Manager
from app.presentstion.tgbot.dialogs.register import register_dialogs
from app.presentstion.tgbot.handlers import router
from app.presentstion.tgbot.middlewares import DAOMiddleware, L10NMiddleware, ThrottlingMiddleware
from app.presentstion.tgbot.utils.get_translator_hub import get_translator_hub


async def main() -> None:
    config = get_config()
    manager = Manager(config)
    hub = get_translator_hub()
    pool = await manager.psql.pool
    redis = await manager.redis.connect
    bot = Bot(
        config.work.tgbot.token, parse_mode=ParseMode.HTML
    )
    if config.work.tgbot.skip_updates:
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
    
    dp.update.middleware(DAOMiddleware(pool))
    dp.update.middleware(L10NMiddleware(hub))
    dp.callback_query.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(DAOMiddleware(pool))
    dp.message.middleware(ThrottlingMiddleware())
    
    dp.include_router(router)
    
    setup_dialogs(dp)
    register_dialogs(dp)
    
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await pool.close()
        await redis.close()
