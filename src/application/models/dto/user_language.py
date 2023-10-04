from dataclasses import dataclass

from src.application.models.enums import LanguagesType


@dataclass(frozen=True)
class UserLanguageDTO:
    language: LanguagesType
