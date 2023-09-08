from dataclasses import dataclass


@dataclass(frozen=True)
class Delete:
    telegram_id: int
