from aiogram.fsm.state import StatesGroup, State


class AutomatesMenu(StatesGroup):
    select_slot = State()


class SlotsMachineState(StatesGroup):
    make_bet = State()


class DiceState(StatesGroup):
    make_bet = State()


class BanditState(StatesGroup):
    make_bet = State()
