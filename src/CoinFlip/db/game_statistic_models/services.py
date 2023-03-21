from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.result import Result

from .models import GeneralGameStatistics

class GeneralGameStatisticsService:
    pass
    # def __init__(self, db_session: AsyncSession):
    #     self.db_session = db_session
    #
    # async def add_in_session_ggs(self, user_id: int) -> None:
    #     new_ggs = GeneralGameStatistics(user_id=user_id)
    #     self.db_session.add(new_ggs)
