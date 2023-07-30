from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

router = Router()


@router.message(Command('link', 'ref'))
async def link_cmd(msg: Message, bot: Bot):
    await msg.answer(
        'Твоя личная ссылка \n'
        f'{await create_start_link(bot=bot, payload=msg.from_user.id, encode=True)}'
    )