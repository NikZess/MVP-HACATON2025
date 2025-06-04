from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models.db_helper import get_async_session
from . import crud
from ..auth.authx_config import security
from .schemas import TaskDailyCreate

router = APIRouter(
    tags=["Daily Tasks"],
)

@router.post("/daily/",
    summary="Добавить новую ежедневную задачу для пользователя",
    description="Добавляет новую ежедневную задачу для пользователя по его username",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)]
)   
async def create_task_daily(
    task_daily_data: TaskDailyCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_daily_task(
        task_daily_data=task_daily_data,
        session=session
    )

@router.get("/daily/",
    summary="Получить все ежедневные задачи",
    description="Возвращает все ежедневные задачи пользователей из базы данных",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)],
)
async def get_all_tasks_daily(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_all_tasks_daily(session=session)

@router.get("/daily/{username}/",
    summary="Получить ежедневные задачи пользователя",
    description="Возвращает все ежедневные задачи пользователя по его username",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)],
)
async def get_user_tasks_daily(
    username: str,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.get_user_tasks_daily(
        username=username,
        session=session,
    )

@router.delete("/daily/",
    summary="Удалить все ежедневные задачи",
    description="Удаляет все ежедневные задачи, всех пользователей из базы данных",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)],           
)
async def delete_all_tasks_daily(session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_all_tasks_daily(session=session)

@router.delete("/daily/{username}/",
    summary="Удалить ежедневные задачи пользователя",
    description="Удаляет все ежедневные задачи пользователя по его username",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_user_tasks_daily(
    username: str,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.delete_user_tasks_daily(
        username=username,
        session=session,
    )