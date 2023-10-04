from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.application.models.dto.base import DataTransferObject
from src.application.models.enums import LanguagesType


@dataclass(frozen=True)
class Update(DataTransferObject):
    telegram_id: int
    language: LanguagesType
    
    __slots__ = (
        'telegram_id',
        'language'
    )
    
    if TYPE_CHECKING:
        def __init__(
            self,
            telegram_id: int,
            language: LanguagesType
        ) -> None:
            ...
