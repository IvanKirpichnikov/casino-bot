from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub



class L10NgMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data.get('event_from_user')
        
        if user is None:
            return await handler(event, data)
        
        hub: TranslatorHub = data.get('_hub')
        locales = hub.get_translator_by_locale(user.language_code)
        data['l10n'] = locales
        
        return await handler(event, data)
