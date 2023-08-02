from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    start: Start
    select: Select
    button: Button


class Start:
    @staticmethod
    def __call__() -> Literal["""Привет, дружище. Рад тебя видеть в нашем казино!
"""]: ...

    @staticmethod
    def ref(*, money) -> Literal["""Здарова, братишка! Рад тебя видеть в нашем казино. Нам за тебя замолвили словечко, держи бонусные { $money } монет!
"""]: ...


class Select:
    @staticmethod
    def game() -> Literal["""Во что играем сегодня?"""]: ...


class Button:
    @staticmethod
    def roulette() -> Literal["""Рулетка"""]: ...

    @staticmethod
    def dice() -> Literal["""Кости"""]: ...

    @staticmethod
    def bandit() -> Literal["""Однорукий бандит"""]: ...

