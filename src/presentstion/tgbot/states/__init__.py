from .main_menu import MainMenuState
from .slots_machine import (
    SlotsMachineState, RouletteState,
    DiceState, BanditState
)
from .tops import TopsState
from .about import AboutState
from .profile import (
    ProfileState, StatsState,
    SettingsState, ReferralState
)


__all__ = (
    'MainMenuState',
    'SlotsMachineState',
    'RouletteState',
    'DiceState',
    'BanditState',
    'TopsState',
    'AboutState',
    'ProfileState',
    'SettingsState',
    'StatsState',
    'ReferralState'
)
