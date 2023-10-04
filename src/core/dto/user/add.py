from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Add:
    telegram_id: int
    chat_id: int
    datetimeutc: datetime
