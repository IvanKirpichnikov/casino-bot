from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from fluentogram import TranslatorRunner

from app.tgbot.states import MainMenuState

if TYPE_CHECKING:
    from stubs import TranslatorRunner


router = Router()


@router.message(CommandStart(deep_link=True, deep_link_encoded=True))
async def trs(message: Message, command: CommandObject):
    await message.answer('Разработка...')


@router.message(CommandStart())
async def start_dialog_(_: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(
        state=MainMenuState.select_option,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.EDIT
    )
