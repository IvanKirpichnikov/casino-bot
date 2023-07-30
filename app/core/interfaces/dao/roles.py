from abc import ABC, abstractmethod
from typing import List


class AbstractRole(ABC):
    @abstractmethod
    async def get(self) -> List[str]:
        pass
