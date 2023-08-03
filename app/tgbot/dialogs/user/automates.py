from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start, Row

from aiogram_dialog.widgets.text import Const, Format

from app.tgbot.states.automates import (AutomatesMenu, SlotsMachineState,
                                        DiceState, BanditState)

menu_window = Window(
    Format('ваш баланс: -балик из бд-\n'
           'Выберите игровой автомат'),

    Start(
        Const('Слот-машина'),
        id='slot-machine',
        state=SlotsMachineState.make_bet,
        mode=StartMode.RESET_STACK
    ),

    Start(
        Const('Кости'),
        id='dice',
        state=DiceState.make_bet,
        mode=StartMode.RESET_STACK
    ),

    Start(
        Const('Однорукий бандит'),
        id='bandit',
        state=BanditState.make_bet,
        mode=StartMode.RESET_STACK
    ),

    state=AutomatesMenu.select_slot
)
