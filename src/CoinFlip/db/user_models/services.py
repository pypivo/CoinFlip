from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.result import Result

from CoinFlip.db.user_models.models import User


class UserServices:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, nick_name: str, email: str, password: str, is_admin: bool = False) -> User:
        new_user = User(
            nick_name=nick_name,
            email=email,
            password=password,
            is_admin=is_admin
        )
        self.db_session.add(new_user)
        await self.db_session.commit()
        return new_user

    async def get_user_by_id(self, user_id: int):
        query = select(User).where(User.user_id == user_id)
        rs: Result = await self.db_session.execute(query)
        users = rs.fetchone()
        if users is not None:
            return users[0]