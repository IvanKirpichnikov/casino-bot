from enum import Enum
from typing import List


class RoleType(str, Enum):
    """
    Listed user roles in the bot
    
    """
    USER = 'user'
    ADMIN = 'admin'
    
    @classmethod
    def get_all(cls) -> List[str]:
        return [role.value for role in cls]
