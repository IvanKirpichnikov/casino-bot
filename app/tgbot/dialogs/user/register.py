from aiogram import Dispatcher

from app.tgbot.dialogs.user.main_menu import main_menu_dialog
from app.tgbot.dialogs.user.slots_machine.register import register_sm_dialog


def register_user_dialogs(dp: Dispatcher) -> None:
    dp.include_router(main_menu_dialog)
    register_sm_dialog(dp)
