from aiogram import Dispatcher

from app.presentstion.tgbot.dialogs.user.register import register_user_dialogs


def register_dialogs(dp: Dispatcher) -> None:
    register_user_dialogs(dp)
