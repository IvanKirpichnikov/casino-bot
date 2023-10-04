from aiogram import Router

from src.presentstion.tgbot.handlers.user import start

router = Router(name=__name__)
files = (start,)

for file in files:
    router.include_router(file.router)
