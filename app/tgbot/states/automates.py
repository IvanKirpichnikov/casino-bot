from aiogram.fsm.state import StatesGroup, State


class AutomatesState(StatesGroup):
    main = State()


class RouletteState(StatesGroup):
    main = State()


class DiceState(StatesGroup):
    main = State()


class BanditState(StatesGroup):
    main = State()
