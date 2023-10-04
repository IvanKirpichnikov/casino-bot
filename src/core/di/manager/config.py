from typing import Any, Dict, Optional

from adaptix import name_mapping, NameStyle, Retort
from dynaconf import Dynaconf

from app.core.configs.config import Config


class ConfigManager:
    def __init__(self) -> None:
        self._retort: Optional[Retort] = None
    
    @property
    def _toml_parse(self) -> Dict[str, Any]:
        return Dynaconf(
            settings_files=['configs/.toml']
        ).as_dict()
    
    @property
    def config(self) -> Config:
        if self._retort is None:
            self._retort = Retort(
                recipe=[
                    name_mapping(Config, name_style=NameStyle.UPPER)
                ]
            )
        data = self._toml_parse
        return self._retort.load(data, Config)
