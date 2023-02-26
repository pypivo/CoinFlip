from ...db.engine import get_db

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .services import _create_new_user, _get_user_by_id
from .models import UserCreate, UserShow

user_router = APIRouter()

@user_router.post('/', response_model=UserShow)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> UserShow:
    return await _create_new_user(body, db)

@user_router.get('/', response_model=UserShow)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)) -> UserShow:
    user = await _get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(
            status_code=404, detail=f"User with id {user_id} not found."
        )
    return user