from abc import ABC, abstractmethod


class AbstractDeepLink(ABC):
    @abstractmethod
    async def add(self, tid: int) -> None:
        pass

    @abstractmethod
    async def create(self, tid: int) -> None:
        pass

    @abstractmethod
    async def



