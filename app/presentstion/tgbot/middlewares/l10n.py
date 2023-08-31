from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

from app.infra.db.rdb.dao.dao import DAO


class L10NMiddleware(BaseMiddleware):
    def __init__(self, hub: TranslatorHub) -> None:
        self._hub = hub
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')
        
        if user is None:
            return await handler(event, data)
        
        dao: DAO = data.get('dao')
        user_language = await dao.user.get_language(user.id)
        
        data['l10n'] = self._hub.get_translator_by_locale(user_language)
        
        return await handler(event, data)
