from dataclasses import dataclass


@dataclass(frozen=True)
class GetLanguage:
    telegram_id: int


@dataclass(frozen=True)
class Language:
    language: str


@dataclass(frozen=True)
class UpdateLanguage:
    telegram_id: int
    language: str
