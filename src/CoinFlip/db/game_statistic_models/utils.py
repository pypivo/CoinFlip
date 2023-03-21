from sqlalchemy.ext.asyncio import AsyncSession

from .models import GeneralGameStatistics

async def add_in_session_ggs(user_id: int, db_session: AsyncSession) -> None:
    new_ggs = GeneralGameStatistics(user_id=user_id)
    db_session.add(new_ggs)