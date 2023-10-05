from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from src.application.models.dto.base import DataTransferObject


@dataclass(frozen=True)
class Add(DataTransferObject):
    telegram_id: int
    chat_id: int
    datetimeutc: datetime
    
    __slots__ = (
        'telegram_id',
        'chat_id',
        'datetimeutc'
    )
    
    if TYPE_CHECKING:
        def __init__(
            self,
            telegram_id: int,
            chat_id: int,
            datetimeutc: datetime
        ) -> None:
            ...
