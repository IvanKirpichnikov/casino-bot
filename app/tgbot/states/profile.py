from aiogram.fsm.state import StatesGroup, State


class ProfileState(StatesGroup):
    main = State()


class StatsState(StatesGroup):
    main = State()


class SettingsState(StatesGroup):
    main = State()


class ReferralState(StatesGroup):
    main = State()
