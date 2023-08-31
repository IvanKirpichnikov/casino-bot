from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


class L10N:
    def __init__(
        self,
        path: str = 'locales/{0}/txt.ftl'
    ) -> None:
        self._path: str = path
    
    @property
    def hub(self) -> TranslatorHub:
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
                        filenames=[self._path.format('ru')]
                    )
                ),
                FluentTranslator(
                    locale='en',
                    translator=FluentBundle.from_files(
                        locale='en_US',
                        filenames=[self._path.format('en')]
                    )
                ),
                FluentTranslator(
                    locale='fr',
                    translator=FluentBundle.from_files(
                        locale='fr_FR',
                        filenames=[self._path.format('fr')]
                    )
                ),
            ],
            root_locale='en'
        )
