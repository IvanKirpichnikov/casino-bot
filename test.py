from asyncpg import Connection, connect
import asyncio
from app.core.configs.config import config
from app.infra.utils.creates_postgres_data import create


async def main():
    psql = config.PSQL
    c = await connect(user=psql.user, host=psql.host, port=psql.port, password=psql.password, database=psql.database)
    await create(c)

asyncio.run(main())
