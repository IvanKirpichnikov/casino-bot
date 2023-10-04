from datetime import datetime

from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, KICKED
from aiogram.types import ChatMemberUpdated

from src.infra.postgres import DAO


router = Router()


@router.my_chat_member(F.chat.type == ChatType.PRIVATE, ChatMemberUpdatedFilter(KICKED >> MEMBER))
async def new_user(event: ChatMemberUpdated, dao: DAO) -> None:
    print('dvhbhfbv,arjbvrf')
    data = dict(
        tid=event.from_user.id,
        cid=event.chat.id,
        dtutc=datetime.utcnow()
    )
    await dao.user.add(**data)
