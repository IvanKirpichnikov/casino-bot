from dataclasses import dataclass
from typing import List

from src.core.enums import RolesType


@dataclass(frozen=True)
class RoleDTO:
    """
    DTO object
    
    """
    roles: List[RolesType]
