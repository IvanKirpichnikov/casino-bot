from asyncpg import Connection

from app.core.interfaces.dao.referral import AbstractReferral


class ReferralDAO(AbstractReferral):
    def __init__(self, connect: Connection):
        self.connect = connect

    async def add(self, tid: int, referral_link: str) -> None:
        connect = self.connect
        async with connect.transaction():
            await connect.execute('''
                INSERT INTO referrals(id, referral_link)
                SELECT id, $1 FROM users WHERE tid = $2;
            ''', referral_link, tid
            )

    async def get_referrals_count(self, tid: int) -> int:
        connect = self.connect
        cursor = await connect.cursor('''
            SELECT referrals_count FROM referrals
            JOIN users ON users.id = referrals.id
            WHERE users.tid = $1;
        '''
        )
        data = await cursor.fetchrow()
        return data.get('referrals_count')
