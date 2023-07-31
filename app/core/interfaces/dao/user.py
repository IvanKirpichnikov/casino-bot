from abc import ABC, abstractmethod
from datetime import datetime


class AbstractUser(ABC):
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

    async def get_language(self, tid: int) -> str:
        pass

    async def update_language(self, tid: int, lang_code: str) -> None:
        pass
