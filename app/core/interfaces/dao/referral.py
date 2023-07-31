from abc import ABC, abstractmethod


class AbstractReferral(ABC):
    @abstractmethod
    async def add(self, tid: int) -> None:
        pass

    @abstractmethod
    async def create(self, tid: int) -> None:
        pass
