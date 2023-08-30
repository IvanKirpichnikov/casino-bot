from dataclasses import dataclass
from typing import Dict

from adaptix import name_mapping, NameStyle, Retort
from dynaconf import Dynaconf


@dataclass(frozen=True)
class _TGBotConfig:
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
    host: str
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
class _WorkConfig:
    """
    :param tgbot: Telegram bot config
    :param psql: Postgresql config
    :param redis: Redis config
    
    """
    tgbot: _TGBotConfig
    psql: _PSQLConfig
    redis: _RedisConfig


@dataclass(frozen=True)
class Config:
    work: _WorkConfig


def get_config() -> Config:
    data: Dict = Dynaconf(
        settings_files=['configs/.toml']
    ).as_dict()
    
    retort = Retort(
        recipe=[
            name_mapping(Config, name_style=NameStyle.UPPER)
        ]
    )
    return retort.load(data, Config)
