import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.core.di.manager import Manager
from app.core.di.manager.config import ConfigManager
from app.presentstion.tgbot.handlers import router
from app.presentstion.tgbot.setups.setups import setups


async def main() -> None:
    config = ConfigManager().config
    manager = Manager(config)
    
    pool = await manager.psql.pool
    redis = await manager.redis.connect
    
    bot = Bot(
        config.work.tgbot.token,
        parse_mode=ParseMode.HTML
    )
    if config.work.tgbot.skip_updates:
        await bot.delete_webhook(drop_pending_updates=True)
    
    storage = manager.redis.aiogram_storage
    dp = Dispatcher(
        storage=storage,
        events_isolation=storage.create_isolation()
    )
    
    dp.include_router(router)
    setups(dp, pool, redis, manager.l10n.hub)
    
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await pool.close()
        await redis.close()


asyncio.run(main())
