from aiogram.fsm.state import StatesGroup, State


class MainMenuState(StatesGroup):
    select_option = State()
