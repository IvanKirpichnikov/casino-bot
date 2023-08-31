from aiogram.fsm.state import StatesGroup, State


class AboutState(StatesGroup):
    main = State()
    support = State()
    authors = State()
