from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import Task, User
from ...core.models.db_helper import get_async_session
from .schemas import TaskCreate
from ...core.models import User, Task
from sqlalchemy import select

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models.db_helper import get_async_session
from . import crud
from ..auth.authx_config import security

router = APIRouter(
    tags=["Tasks"],
)


@router.post("/common/", 
    summary="Добавить новую задачу для пользователя", 
    description="Добавляет новую задачу для пользователя по его username",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)]
)
async def create_task(
    task_data: TaskCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_task(
        task_data=task_data,
        session=session,
    )

@router.get("/common/",
    summary="Получить все задачи",
    description="Возвращает все задачи, всех пользователей из базы данных",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)]
)
async def get_all_tasks(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_all_tasks(session=session)

@router.get("/common/{username}/",
    summary="Получить задачи пользователя",
    description="Возвращает все задачи пользователя по его username",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)]
)
async def get_user_tasks(
    username: str,
    session: AsyncSession = Depends(get_async_session)
): 
    return await crud.get_user_tasks(
        username=username,
        session=session,
    ),

@router.delete("/common/",
    summary="Удалить все задачи",
    description="Удаляет все задачи, всех пользователей из базы данных",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_all_tasks(session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_all_tasks(session=session)

@router.delete("/common/{username}/",
    summary="Удалить задачи пользователя",
    description="Удаляет все задачи пользователя по его username",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)]
)
async def delete_user_tasks(
    username: str,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.delete_user_tasks(
        username=username,
        session=session,
    )