from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import Task, User
from ...core.models.db_helper import get_async_session
from .schemas import TaskCreate
from ...core.models import User, Task
from sqlalchemy import select
from . import crud
from ..auth.authx_config import security

router = APIRouter(
    tags=["Tasks"],
)

@router.post("/", 
    summary="Добавить новую задачу для пользователя", 
    description="Добавляет новую задачу для пользователя по его username",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)]
)
async def create_task(
    username: str,
    description: str,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_task(
        username=username,
        description=description,
        session=session,
    )