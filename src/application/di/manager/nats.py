from src.application.configs.config import Config


class NatsManager:
    _config: Config
    __slots__ = ('_config',)
    
    def __init__(self, config: Config) -> None:
        self._config = config
