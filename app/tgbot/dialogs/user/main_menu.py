from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start, Row

from aiogram_dialog.widgets.text import Const

from app.tgbot.states.main_menu import MainMenuState
from app.tgbot.states.profile import ProfileState
from app.tgbot.states.tops import TopsState
from app.tgbot.states.automates import AutomatesMenu
from app.tgbot.states.about import AboutState

main_menu_dialog = Dialog(
    Window(
        Const('Меню'),
        Start(
            Const('Автоматы'),
            id='slot_machines',
            state=AutomatesMenu.select_slot,
            mode=StartMode.RESET_STACK

        ),
        Row(
            Start(
                Const('Профиль'),
                id='profile',
                state=ProfileState.main,
                mode=StartMode.RESET_STACK
            ),

            Start(
                Const('Топ игроков'),
                id='top_players',
                state=TopsState.main,
                mode=StartMode.RESET_STACK
            ),
        ),

        Start(
            Const('О нас'),
            id='about',
            state=AboutState.main,
            mode=StartMode.RESET_STACK
        ),

        state=MainMenuState.select_option,
    ),
)
