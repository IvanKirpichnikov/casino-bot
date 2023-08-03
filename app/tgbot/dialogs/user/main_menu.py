from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start, Row

from app.tgbot.states.main_menu import MainMenuState
from app.tgbot.states.profile import ProfileState
from app.tgbot.states.tops import TopsState
from app.tgbot.states.slots_machine import SlotsMachineState
from app.tgbot.states.about import AboutState
from app.tgbot.dialogs.widgets import L10N


main_menu_dialog = Dialog(
    Window(
        L10N('start'),
        Start(
            L10N('Автоматы'),
            id='slot_machines',
            state=SlotsMachineState.select_slots_machine,
            mode=StartMode.RESET_STACK
        ),
        Row(
            Start(
                L10N('Профиль'),
                id='profile',
                state=ProfileState.main,
                mode=StartMode.RESET_STACK
            ),
            Start(
                L10N('Топ игроков'),
                id='top_players',
                state=TopsState.main,
                mode=StartMode.RESET_STACK
            ),
        ),
        Start(
            L10N('О нас'),
            id='about',
            state=AboutState.main,
            mode=StartMode.RESET_STACK
        ),
        state=MainMenuState.select_option,
    )
)