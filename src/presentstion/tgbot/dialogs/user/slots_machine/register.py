from aiogram import Dispatcher

from app.presentstion.tgbot.dialogs.user.slots_machine.dialog import slots_machine_dialog


def register_sm_dialog(dp: Dispatcher) -> None:
    dp.include_router(slots_machine_dialog)
