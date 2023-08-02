from abc import ABC, abstractmethod
from typing import List

from app.core.dto.roles import RolesDTO


class AbstractRoles(ABC):
    @abstractmethod
    async def get(self) -> RolesDTO:
        """
        :return: RolesDTO
        
        """
