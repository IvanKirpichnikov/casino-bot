from asyncpg import Connection

from app.infra.postgres.dao import RolesDAO, ReferralDAO, UsersDAO


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
        self.roles = RolesDAO(connect)
        self.referrals = ReferralDAO(connect)
        self.users = UsersDAO(connect)
