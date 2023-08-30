from aiogram import Router

from . import other, user


router = Router(name=__name__)
files = (other, user)

for file in files:
    router.include_router(file.router)
