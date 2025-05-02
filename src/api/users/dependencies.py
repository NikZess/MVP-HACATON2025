from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import HTTPException, Depends, status, Path
from ...core.models.db_helper import get_async_session
from . import crud
from ...core.models import User

async def user_by_username(
    username: Annotated[str, Path],
    session: AsyncSession = Depends(get_async_session),
):
    user = await crud.get_user_by_username(
        session=session,
        username=username,
    )
    if user is not None:
        return user
    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь {username} не найден"
    )
