from asyncpg import Connection

from app.infra.postgres.dao import RoleDAO, ReferralDAO, UserDAO


class DAO:
    def __init__(self, connect: Connection):
        self.role = RoleDAO(connect)
        self.referral = ReferralDAO(connect)
        self.user = UserDAO(connect)
