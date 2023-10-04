from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator
from fluentogram import TranslatorHub

from src.application.models.enums import LanguagesType


class L10NManager:
    _path_to_files: str
    __slots__ = ('_path_to_files',)
    
    def __init__(
        self,
        path_to_files: str
    ) -> None:
        self._path_to_files: str = path_to_files
    
    @property
    def hub(self) -> TranslatorHub:
        path_to_files = self._path_to_files
        locales_map = [
            LanguagesType.RU,
            LanguagesType.EN,
            LanguagesType.FR
        ]
        return TranslatorHub(
            dict(
                ru=locales_map,
                en=locales_map[1:],
                fr=locales_map[2]
            ),
            [
                FluentTranslator(
                    locale=LanguagesType.RU,
                    translator=FluentBundle.from_files(
                        locale='ru_RU',
                        filenames=[path_to_files.format('ru')]
                    )
                ),
                FluentTranslator(
                    locale=LanguagesType.EN,
                    translator=FluentBundle.from_files(
                        locale='en_US',
                        filenames=[path_to_files.format('en')]
                    )
                ),
                FluentTranslator(
                    locale=LanguagesType.FR,
                    translator=FluentBundle.from_files(
                        locale='fr_FR',
                        filenames=[path_to_files.format('fr')]
                    )
                ),
            ],
            root_locale=LanguagesType.RU
        )
