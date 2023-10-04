from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start, Row

from src.presentstion.tgbot.states.main_menu import MainMenuState
from src.presentstion.tgbot.states.profile import ProfileState
from src.presentstion.tgbot.states.tops import TopsState
from src.presentstion.tgbot.states.slots_machine import SlotsMachineState
from src.presentstion.tgbot.states.about import AboutState
from src.presentstion.tgbot.dialogs.widgets import L10N


main_menu_dialog = Dialog(
    Window(
        L10N('start'),
        Start(
            L10N('btn-machines'),
            id='slot_machines',
            state=SlotsMachineState.select_slots_machine,
            mode=StartMode.RESET_STACK
        ),
        Row(
            Start(
                L10N('btn-profile'),
                id='profile',
                state=ProfileState.main,
                mode=StartMode.RESET_STACK
            ),
            Start(
                L10N('btn-leaderboard'),
                id='top_players',
                state=TopsState.main,
                mode=StartMode.RESET_STACK
            ),
        ),
        Start(
            L10N('btn-about'),
            id='about',
            state=AboutState.main,
            mode=StartMode.RESET_STACK
        ),
        state=MainMenuState.select_option,
    )
)
