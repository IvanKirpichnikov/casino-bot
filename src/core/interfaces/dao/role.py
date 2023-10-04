from abc import ABC, abstractmethod
from typing import List

from src.core.dto import RoleDTO


class AbstractRoleDAO(ABC):
    @abstractmethod
    async def get_roles(self) -> RoleDTO:
        """:return: RolesDTO"""
