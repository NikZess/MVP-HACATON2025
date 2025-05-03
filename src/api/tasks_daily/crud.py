from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import User, TaskDaily
from ...core.models import User
from sqlalchemy import select
from typing import Annotated
from annotated_types import MinLen, MaxLen

async def create_daily_task(
    username: str,
    description: Annotated[str, MinLen(3), MaxLen(1000)],
    session: AsyncSession
) -> TaskDaily:
    query = await session.execute(
        select(User).where(User.username == username)
    )
    user = query.scalar_one_or_none()
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )
    task_daily = TaskDaily(
        username=user.username,
        description=description
    )
    session.add(task_daily)
    await session.commit()
    return {"status": "ok", "task_daily_id": task_daily.id}

async def get_all_tasks_daily(session: AsyncSession) -> list[TaskDaily]:
    query = select(TaskDaily).order_by(TaskDaily.id)
    result = await session.execute(query)
    tasks_daily = result.scalars().all()
    return {"tasks_daily": tasks_daily}

async def get_user_tasks_daily(
    username: str,
    session: AsyncSession
) -> list[TaskDaily]:
    query = select(TaskDaily).where(TaskDaily.username == username)
    result = await session.execute(query)
    tasks_daily = result.scalars().all()
    return {f"{username}'s tasks_daily": tasks_daily}

async def delete_all_tasks_daily(session: AsyncSession) -> None:
    query = await session.execute(
        select(TaskDaily).order_by(TaskDaily.id)
    )
    tasks = query.scalars().all()
    for task in tasks:
        await session.delete(task)
    await session.commit()
    return {"message": "ok"}

async def delete_user_tasks_daily(
    username: str,
    session: AsyncSession
) -> None:
    query = await session.execute(
        select(TaskDaily).where(TaskDaily.username == username)
    )
    tasks = query.scalars().all()
    for task in tasks:
        await session.delete(task)
    await session.commit()
    return {"message": "ok"}