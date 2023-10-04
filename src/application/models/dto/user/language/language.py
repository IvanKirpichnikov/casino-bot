from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.application.models.dto.base import DataTransferObject
from src.application.models.enums import LanguagesType


@dataclass(frozen=True)
class Language(DataTransferObject):
    language: LanguagesType
    
    __slots__ = ('language',)
    
    if TYPE_CHECKING:
        def __init__(
            self,
            language: LanguagesType
        ) -> None:
            ...
