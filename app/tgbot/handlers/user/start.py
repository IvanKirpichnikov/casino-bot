from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message

router = Router()


@router.message(CommandStart(deep_link=True, deep_link_encoded=True))
async def trs(msg: Message, command: CommandObject):
    await msg.answer('txt')


@router.message(CommandStart())
async def trs(msg: Message, command: CommandObject):
    await msg.answer('txt')