from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


class L10N:
    def __init__(
        self,
        path_to_files: str = 'locales/{0}/txt.ftl'
    ) -> None:
        self._path_to_files: str = path_to_files
    
    @property
    def hub(self) -> TranslatorHub:
        path_to_files = self._path_to_files
        return TranslatorHub(
            dict(
                ru=('ru', 'en', 'fr'),
                en=('en', 'fr'),
                fr=('fr',)
            ),
            [
                FluentTranslator(
                    locale='ru',
                    translator=FluentBundle.from_files(
                        locale='ru_RU',
                        filenames=[path_to_files.format('ru')]
                    )
                ),
                FluentTranslator(
                    locale='en',
                    translator=FluentBundle.from_files(
                        locale='en_US',
                        filenames=[path_to_files.format('en')]
                    )
                ),
                FluentTranslator(
                    locale='fr',
                    translator=FluentBundle.from_files(
                        locale='fr_FR',
                        filenames=[path_to_files.format('fr')]
                    )
                ),
            ],
            root_locale='en'
        )
