from dataclasses import dataclass
from typing import TYPE_CHECKING


@dataclass(frozen=True)
class _TGBotConfig:
    """
    :param token: Telegram bot token
    :param skip_updates: skip bot updates if true

    """
    token: str
    skip_updates: bool
    
    if TYPE_CHECKING:
        def __init__(
            self,
            token: str,
            skip_updates: bool
        ) -> None:
            pass


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
    
    if TYPE_CHECKING:
        def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
            database: str
        ) -> None:
            ...


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
    
    if TYPE_CHECKING:
        def __init__(
            self,
            host: str,
            port: int,
            password: str,
            db: str
        ) -> None:
            ...


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
    
    if TYPE_CHECKING:
        def __init__(
            self,
            tgbot: _TGBotConfig,
            psql: _PSQLConfig,
            redis: _RedisConfig
        ) -> None:
            ...


@dataclass(frozen=True)
class Config:
    work: _WorkConfig
    
    if TYPE_CHECKING:
        def __init__(
            self,
            work: _WorkConfig
        ) -> None:
            ...
