from abc import ABC, abstractmethod
from datetime import datetime


class AbstractUserDAO(ABC):
    """
    Table users
        id SERIAL,
        tid BIGINT,
        cid BIGINT,
        role SMALLINT REFERENCES roles(name) ON DELETE CASCADE,
        datetime TIMESTAMPTZ,
        PRIMARY KEY(id, tid, cid, datetime)
    """
    @abstractmethod
    async def add(self, tid: int, cid: int, dtutc: datetime) -> None:
        """
        Add user
        :param tid: user telegram id
        :param cid: user chat id
        :param dtutc: datetime utc format
        :return: None
        """
    
    @abstractmethod
    async def delete(self, tid: int) -> None:
        """
        Delete user
        :param tid: user telegram id
        :return: None
        """
