from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from asyncpg import Connection
from fluentogram import TranslatorHub

from app.infra.postgres import DAO


class L10NMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')
        
        if user is None:
            return await handler(event, data)
        
        connect: Connection = data.get('connect')
        dao: DAO = data.get('dao')
        user_language = await dao.users.get_language(user.id)
        hub: TranslatorHub = data.get('_hub')
        l10n = hub.get_translator_by_locale(user_language)
        
        data['l10n'] = l10n
        
        return await handler(event, data)
