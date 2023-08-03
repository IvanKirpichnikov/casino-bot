from aiogram.fsm.state import StatesGroup, State


class MainMenuState(StatesGroup):
    main = State()
    slot_machines = State()
    top_players = State
    profile = State()
    about = State()


class SlotsMachinesState(StatesGroup):
    roulette = State()
    dice = State()
    bandit = State()


class ProfileState(StatesGroup):
    stats = State()
    settings = State()
    referral = State()


class AboutState(StatesGroup):
    support = State()
    authors = State()
