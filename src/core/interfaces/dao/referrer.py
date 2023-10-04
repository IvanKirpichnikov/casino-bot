from abc import ABC, abstractmethod

from app.core.dto import UserDTO


class AbstractReferrerDAO(ABC):
    @abstractmethod
    async def get_my_referrer(self, tid: int) -> UserDTO:
        pass
