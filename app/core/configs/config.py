from dataclasses import dataclass
from ipaddress import IPv4Address

from adaptix import NameStyle, Retort, name_mapping
from dynaconf import Dynaconf


@dataclass(frozen=True)
class _BotConfig:
    """
    :param token: Telegram bot token
    :param skip_updates: skip bot updates if True
    
    """
    token: str
    skip_updates: bool


@dataclass(frozen=True)
class _PSQLConfig:
    """
    :param host: server ip address
    :param port: server port
    :param user: postgresql user name
    :param password: postgresql user password
    :param database: postgresql database name
    
    """
    host: IPv4Address
    port: int
    user: str
    password: str
    database: str


@dataclass(frozen=True)
class _RedisConfig:
    """
    :param host: server ip address
    :param port: server port
    :param password: redis user password
    :param db: redis database name
    
    """
    host: str
    port: int
    password: str
    db: int


@dataclass(frozen=True)
class Config:
    """
    :param bot: Bot config
    :param psql: Postgresql config
    :param redis: Redis config
    
    """
    bot: _BotConfig
    psql: _PSQLConfig
    redis: _RedisConfig


dynaconf = Dynaconf(
    settings_files=['.toml'],
    environments=True
)

data = dynaconf.as_dict()

retort = Retort(
    recipe=[
        name_mapping(Config, name_style=NameStyle.UPPER)
    ]
)
config = retort.load(data, Config)
