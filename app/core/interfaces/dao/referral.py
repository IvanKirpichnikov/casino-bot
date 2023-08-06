from abc import ABC, abstractmethod

from app.core.dto import DeepLinkDTO, ReferrersCountDTO


class AbstarctReferralDAO(ABC):
    
    @abstractmethod
    async def add_referer(self, tid: int) -> None:
        pass
    
    @abstractmethod
    async def add_user_data(self, tid: int, deep_link: str) -> None:
        pass
    
    @abstractmethod
    async def get_deep_link(self, tid: int) -> DeepLinkDTO:
        pass
    
    @abstractmethod
    async def get_referrers_count(self, tid: int) -> ReferrersCountDTO:
        pass
    
    @abstractmethod
    async def update_deep_link(self, tid: int, deep_link: str) -> None:
        pass
