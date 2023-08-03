from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start, Row

from aiogram_dialog.widgets.text import Const
from app.tgbot.states import MainMenuState

main_menu_dialog = Dialog(
    Window(
        Const('Меню'),
        Start(
            Const('Автоматы'),
            id='slot_machines',
            state=MainMenuState.slot_machines,
            mode=StartMode.RESET_STACK

        ),
        Row(
            Start(
                Const('Профиль'),
                id='profile',
                state=MainMenuState.profile,
                mode=StartMode.RESET_STACK
            ),

            Start(
                Const('Топ игроков'),
                id='top_players',
                state=MainMenuState.top_players,
                mode=StartMode.RESET_STACK
            ),
        ),

        Start(
            Const('О нас'),
            id='about',
            state=MainMenuState.about,
            mode=StartMode.RESET_STACK
        ),

        state=MainMenuState.main,
    ),
)
