from dataclasses import dataclass
from typing import List

from app.core.enums.roles_type import RoleType


@dataclass(frozen=True)
class RolesDTO:
    roles: List[RoleType]
