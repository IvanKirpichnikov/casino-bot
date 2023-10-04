from dataclasses import dataclass

from src.core.enums import LanguagesType


@dataclass(frozen=True)
class UserLanguageDTO:
    language: LanguagesType
