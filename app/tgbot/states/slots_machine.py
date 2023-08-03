from aiogram.fsm.state import StatesGroup, State


class SlotsMachineState(StatesGroup):
    select_slots_machine = State()


class RouletteState(StatesGroup):
    make_bet = State()


class DiceState(StatesGroup):
    make_bet = State()


class BanditState(StatesGroup):
    make_bet = State()