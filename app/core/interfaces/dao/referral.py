from abc import ABC, abstractmethod


class AbstractReferral(ABC):
    @abstractmethod
    async def add(self, tid: int) -> None:
        pass

    @abstractmethod
    async def get_referrers_count(self, tid: int) -> None:
        pass
