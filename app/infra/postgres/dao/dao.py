from asyncpg import Connection

from app.infra.postgres.dao import RoleDAO, ReferralDAO, UserDAO


class DAO:
    """
    DAO class containing implemented all DAO
    
    """
    __slots__ = ('connect', 'roles', 'referrals', 'users')
    
    def __init__(self, connect: Connection) -> None:
        """
        :param connect: postgresql connect
        :return None:
        
        """
        self.roles = RoleDAO(connect)
        self.referrals = ReferralDAO(connect)
        self.users = UserDAO(connect)
