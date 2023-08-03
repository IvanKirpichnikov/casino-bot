from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start

from app.tgbot.states.slots_machine import (
    RouletteState, SlotsMachineState,
    DiceState, BanditState
)
from app.tgbot.dialogs.widgets import L10N


slots_machine_dialog = Dialog(
    Window(
        L10N('select-game'),
        Start(
            text=L10N('btn-roulette'),
            id='slot_machine',
            state=RouletteState.make_bet,
            mode=StartMode.RESET_STACK
        ),
        Start(
            L10N('btn-dice'),
            id='dice',
            state=DiceState.make_bet,
            mode=StartMode.RESET_STACK
        ),
        Start(
            L10N('btn-bandit'),
            id='bandit',
            state=BanditState.make_bet,
            mode=StartMode.RESET_STACK
        ),
        state=SlotsMachineState.select_slots_machine
    )
)
