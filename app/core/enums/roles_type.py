from enum import Enum
from typing import List


class RoleType(str, Enum):
    USER = 'user'
    ADMIN = 'admin'

    @classmethod
    def get_all(cls) -> List[str]:
         values = [role.value for role in cls]
         return values
