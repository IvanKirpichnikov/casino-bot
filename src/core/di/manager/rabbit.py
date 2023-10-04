from app.core.configs.config import Config


class Rabbit:
    def __init__(self, config: Config) -> None:
        self._config = config
