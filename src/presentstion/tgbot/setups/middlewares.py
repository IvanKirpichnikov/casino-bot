from aiogram import Dispatcher
from asyncpg import Pool
from fluentogram import TranslatorHub

from src.presentstion.tgbot.middlewares import DAOMiddleware, L10NMiddleware, ThrottlingMiddleware


def setup_inner_middleware(
    dp: Dispatcher,
    pool: Pool,
    hub: TranslatorHub
) -> None:
    dp.update.middleware(DAOMiddleware(pool))
    dp.update.middleware(L10NMiddleware(hub))
    
    dp.callback_query.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(DAOMiddleware(pool))
    
    dp.message.middleware(ThrottlingMiddleware())
