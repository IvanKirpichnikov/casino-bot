from abc import ABC, abstractmethod


class BaseDAO(ABC):
    @abstractmethod
    async def create_table(self) -> None:
        pass
