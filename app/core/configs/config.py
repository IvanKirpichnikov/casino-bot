from dataclasses import dataclass

from adaptix import Retort
from dynaconf import Dynaconf

@dataclass(frozen=True)
class _BotConfig:
    token: str
    skip_updates: bool

@dataclass(frozen=True)
class _PSQLConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

@dataclass(frozen=True)
class _RedisConfig:
    host: str
    port: int
    password: str
    db: int

@dataclass(frozen=True)
class Config:
    BOT: _BotConfig
    PSQL: _PSQLConfig
    REDIS: _RedisConfig


settings = Dynaconf(
    settings_files=['configs/.toml'],
    environments=True
)

data = settings.as_dict()
retort = Retort()
config = retort.load(data, Config)
