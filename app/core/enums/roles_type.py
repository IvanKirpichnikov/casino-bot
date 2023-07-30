from enum import Enum
from typing import Tuple


class RoleType(str, Enum):
    USER = 'user'
    ADMIN = 'admin'
    BANNED = 'banned'
    KICKED = 'kicked'

    @classmethod
    def get_tuple(cls) -> Tuple[str]:
         values = [role.value for role in cls]
         return tuple(values)
