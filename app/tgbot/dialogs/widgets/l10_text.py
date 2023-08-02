from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from stubs import TranslatorRunner


class L10NText(Text):
    def __init__(self, key: str, when: WhenCondition = None):
        super().__init__(when=when)
    
    async def _render_text(self, data, manager: DialogManager) -> str:
        l10n: TranslatorRunner = manager.middleware_data.get('l10n')
        return l10n.get(self.key, **data)
