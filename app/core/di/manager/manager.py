from app.core.configs.config import Config
from app.core.di.manager.psql import Postgresql
from app.core.di.manager.rabbit import Rabbit
from app.core.di.manager.redis import Redis


class Manager:
    def __init__(self, config: Config) -> None:
        self.psql = Postgresql(config)
        self.redis = Redis(config)
        self.rabbit = Rabbit(config)
