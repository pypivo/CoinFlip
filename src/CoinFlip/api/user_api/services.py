from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserCreate, UserShow
from ...db.services import UserServices


async def _create_new_user(body: UserCreate, session: AsyncSession):
    async with session.begin():
        user_service = UserServices(session)
        user = await user_service.create_user(
            nick_name=body.nick_name,
            email=body.email,
            # дописать хешер
            password=body.password
        )
        return UserShow(
            user_id=user.user_id,
            nick_name=user.nick_name,
            email=user.email,
            is_admin=user.is_admin
        )

async def _get_user_by_id(user_id: int, session: AsyncSession) -> Optional[UserShow]:
    async with session.begin():
        user_service = UserServices(session)
        user = await user_service.get_user_by_id(
            user_id=user_id,
        )
        if user is not None:
            return UserShow(
                user_id=user.user_id,
                nick_name=user.nick_name,
                email=user.email,
                is_admin=user.is_admin,
            )

