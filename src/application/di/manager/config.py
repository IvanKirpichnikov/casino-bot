from typing import Any
from typing import Dict
from typing import Optional

from adaptix import NameStyle
from adaptix import Retort
from adaptix import name_mapping
from toml import load

from src.application.configs.config import Config


class ConfigManager:
    _retort: Optional[Retort]
    _data: Optional[Dict[str, Any]]
    __slots__ = ('_retort', '_data')
    
    def __init__(self, retort: Optional[Retort] = None) -> None:
        self._data = None
        if retort is None:
            self._retort = Retort(
                recipe=[
                    name_mapping(Config, name_style=NameStyle.UPPER)
                ]
            )
        else:
            self._retort = retort
    
    def _toml_parse(self) -> Dict[str, Any]:
        if self._data is None:
            self._data = load('configs/settings.toml')
        return self._data
    
    @property
    def config(self) -> Config:
        retort = self._retort
        data = self._toml_parse()
        return retort.load(data, Config)
