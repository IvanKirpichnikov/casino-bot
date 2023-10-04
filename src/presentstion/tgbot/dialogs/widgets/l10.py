from typing import Any, Dict, TYPE_CHECKING

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from src.application.di.stubs.l10n import TranslatorRunner


class L10N(Text):
    def __init__(self, key: str, when: WhenCondition = None):
        super().__init__(when=when)
        self.key = key
    
    async def _render_text(
        self,
        data: Dict[str, Any],
        manager: DialogManager
    ) -> str:
        l10n: TranslatorRunner = manager.middleware_data.get('l10n', None)
        
        if l10n is None:
            raise ValueError("There is no 'l10n' argument in middlewares")
        
        if data:
            return l10n.get(self.key, **data)
        return l10n.get(self.key)
