from asyncpg import Connection

from src.infrastructure.postgres.repository import RoleDAO, UserDAO


class DAO:
    """
    DAO class containing implemented all DAO
    
    """
    __slots__ = ('connect', 'role', 'referral', 'user')
    
    def __init__(self, connect: Connection) -> None:
        """
        :param connect: postgresql connect
        :return None:
        
        """
        self.role = RoleDAO(connect)
        # self.referrals = ReferralDAO(connect)
        self.user = UserDAO(connect)
