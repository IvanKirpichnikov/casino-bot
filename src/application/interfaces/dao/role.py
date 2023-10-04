from abc import ABC, abstractmethod

from src.application.models.dto import RoleDTO


class AbstractRoleDAO(ABC):
    @abstractmethod
    async def get_roles(self) -> RoleDTO:
        """:return: RolesDTO"""
