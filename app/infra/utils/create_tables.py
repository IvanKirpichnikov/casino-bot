from asyncpg import Connection


async def _create_users_table(connect: Connection) -> None:
    async with connect.transaction():
        await connect.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL,
                tid BIGINT,
                cid BIGINT,
                role SMALLINT REFERENCES roles(name) ON DELETE CASCADE,
                datetime TIMESTAMPTZ,
                PRIMARY KEY(id, tid, cid, datetime)
            );
        ''')
