from asyncpg import Connection

from src.application.models.dto import ReferrersCountDTO, DeepLinkDTO
from src.application.interfaces.dao.referral import AbstarctReferralDAO


class ReferralDAO(AbstarctReferralDAO):
    __slots__ = ('connect',)
    
    def __init__(self, connect: Connection):
        self.connect = connect
    
    async def add_user_data(self, tid: int, deep_link: str) -> None:
        await self.connect.execute(
            '''
                INSERT INTO referral(id, deep_link)
                SELECT id, $2 FROM users
                WHERE users.tid = $1;
            ''',
            tid, deep_link
        )
    
    async def add_referer(self, tid: int) -> None:
        await self.connect.execute(
            '''
                UPDATE referrals
                SET referrers_count = referrers_count + 1
                FROM referrals
                JOIN users ON users.id = referrals.id
                WHERE users.id = $1;
            ''',
            tid
        )
    
    async def get_referrers_count(self, tid: int) -> ReferrersCountDTO:
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await self.connect.cursor(
                '''
                    SELECT referrers_count FROM referrals
                    JOIN users ON users.id = referrals.id
                    WHERE users.id = $1;
                ''',
                tid
            )
            data = await cursor.fetchrow()
            return ReferrersCountDTO(count=data.get('referrers_count'))
    
    async def get_deep_link(self, tid: int) -> DeepLinkDTO:
        connect = self.connect
        async with connect.transaction(readonly=True):
            cursor = await connect.cursor(
                '''
                    SELECT deep_link FROM referrals
                    JOIN users ON users.id = referrals.id
                    WHERE users.id = $1;
                ''',
                tid
            )
            data = await cursor.fetchrow()
            return DeepLinkDTO(link=data.get('deep_link'))
    
    async def update_deep_link(self, tid: int, deep_link: str) -> None:
        await self.connect.execute(
            '''
                UPDATE referrals
                SET deep_link = $2
                FROM referrals
                JOIN users ON users.id = referrals.id
                WHERE users.id = $1;
            ''',
            tid, deep_link
        )
