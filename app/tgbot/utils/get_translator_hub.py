from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def get_translator_hub() -> TranslatorHub:
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
                    filenames=['locales/ru/txt.ftl']
                )
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en_US',
                    filenames=['locales/en/txt.ftl']
                )
            ),
            FluentTranslator(
                locale='fr',
                translator=FluentBundle.from_files(
                    locale='fr_FR',
                    filenames=['locales/fr/txt.ftl']
                )
            ),
        ],
        root_locale='en'
    )
