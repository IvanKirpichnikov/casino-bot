import asyncio
import logging

from app.presentstion.tgbot.main import main


logging.basicConfig(level=logging.DEBUG)
asyncio.run(main())
