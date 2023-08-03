import asyncio
import logging

from app.tgbot.main import main


logging.basicConfig(level=logging.DEBUG)
asyncio.run(main())
