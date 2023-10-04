from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.application.models.dto.base import DataTransferObject


@dataclass(frozen=True)
class Get(DataTransferObject):
    telegram_id: int
    
    __slots__ = ('telegram_id',)
    
    if TYPE_CHECKING:
        def __init__(
            self,
            telegram_id: int
        ) -> None:
            ...
