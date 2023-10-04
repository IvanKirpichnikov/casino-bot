from src.application.configs.config import Config
from src.application.di.manager.config import ConfigManager
from src.application.di.manager.l10n import L10N
from src.application.di.manager.psql import Postgresql
from src.application.di.manager.rabbit import Rabbit
from src.application.di.manager.redis import Redis


class Manager:
    def __init__(self, config: Config) -> None:
        self.psql = Postgresql(config)
        self.redis = Redis(config)
        self.rabbit = Rabbit(config)
        self.l10n = L10N()
        self.config = ConfigManager()
