import logging

from asyncpg import Connection

from src.application.models import dto
from src.application.interfaces.repository.user import AbstractUserDAO

logger = logging.getLogger(__name__)


class UserDAO(AbstractUserDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def add(self, model: dto.user.Add) -> None:
        await self.connect.execute(
            '''
                INSERT INTO users(
                    telegram_id,
                    chat_id,
                    datetimeutc
                )
                VALUES(
                    $1::BIGINT,
                    $2::BIGINT,
                    $3::TIMESTAMPTZ(0)
                )
                ON CONFLICT DO NOTHING;
            ''',
            model.telegram_id,
            model.chat_id,
            model.datetimeutc
        )
        logger.warning(
            'Added user to database. Telegram id=%r. Chat id=%r',
            model.telegram_id,
            model.chat_id
        )
    
    async def remove(self, model: dto.user.Delete) -> None:
        await self.connect.execute(
            '''
                DELETE FROM users
                WHERE telegram_id = $1::BIGINT;
            ''',
            model.telegram_id
            )
        logger.warning(
            'Remove user. Telegram id=%r',
            model.telegram_id
        )
    
    async def get_language(
        self,
        model: dto.user.GetLanguage
    ) -> dto.user.Language:
        # logger.info('')
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await connect.cursor(
                '''
                    SELECT language
                       FROM users
                      WHERE telegram_id = $1::BIGINT;
                ''',
                model.telegram_id
                )
            data = await cursor.fetchrow()
        return dto.user.Language(language=data.get('language'))
    
    async def update_language(self, model: dto.user.UpdateLanguage) -> None:
        await self.connect.execute(
            '''
                UPDATE users
                   SET language = $2::TEXT
                 WHERE telegram_id = $1::BIGINT;
            ''',
            model.telegram_id,
            model.language
        )
