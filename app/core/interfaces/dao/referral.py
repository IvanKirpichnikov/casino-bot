from abc import ABC, abstractmethod


class AbstractReferral(ABC):
    @abstractmethod
    async def add(self, tid: int, referral_link: str) -> None:
        pass

    @abstractmethod
    async def get_referrals_count(self, tid: int) -> int:
        pass
