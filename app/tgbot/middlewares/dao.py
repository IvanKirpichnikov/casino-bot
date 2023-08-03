from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from asyncpg import Pool

from app.infra.postgres import DAO


class DAOMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        pool: Pool = data.get('pool')
        
        async with pool.acquire() as connect:
            data['dao'] = DAO(connect)
            
            return await handler(event, data)
