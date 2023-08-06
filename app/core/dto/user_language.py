from dataclasses import dataclass

from app.core.enums import LanguagesType


@dataclass(frozen=True)
class UserLanguageDTO:
    language: LanguagesType
