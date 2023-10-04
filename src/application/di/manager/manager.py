from src.application.configs.config import Config
from src.application.di.manager.config import ConfigManager
from src.application.di.manager.l10n import L10NManager
from src.application.di.manager.nats import NatsManager
from src.application.di.manager.psql import PostgresqlManager
from src.application.di.manager.redis import RedisManager


class Manager:
    config: ConfigManager
    l10n: L10NManager
    nats: NatsManager
    psql: PostgresqlManager
    redis: RedisManager
    __slots__ = (
        'config',
        'l10n',
        'nats',
        'psql',
        'redis'
    )
    
    def __init__(
        self,
        config: Config,
        path_to_files: str = 'locales/{0}/txt.ftl'
    ) -> None:
        self.config = ConfigManager()
        self.l10n = L10NManager(path_to_files)
        self.nats = NatsManager(config)
        self.psql = PostgresqlManager(config)
        self.redis = RedisManager(config)
