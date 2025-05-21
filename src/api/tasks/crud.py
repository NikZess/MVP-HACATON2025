from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import Task, User
from ...core.models.db_helper import get_async_session
from .schemas import TaskCreate
from ...core.models import User, Task
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import Task, User
from sqlalchemy import select
from typing import Annotated
from .schemas import TaskCreate
from annotated_types import MinLen, MaxLen

async def create_task(
    task_data: TaskCreate,
    session: AsyncSession,
) -> Task:
    query = await session.execute(
        select(User).where(User.username == task_data.username)
    )
    user = query.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Пользователь не найден"
        )
    task = Task(
        username=user.username,
        description=task_data.description,
    )
    session.add(task)
    await session.commit()
 
    return {"status": "ok", "task_id": task.id}

async def get_all_tasks(
    session: AsyncSession,
) -> list[Task]:
    query = select(Task).order_by(Task.id)
    result = await session.execute(query)
    tasks = result.scalars().all()
    return {"tasks": list(tasks)}

async def get_user_tasks(
    username: str,
    session: AsyncSession,
) -> list[Task]:
    query = select(Task).where(Task.username == username)
    result = await session.execute(query)
    user_tasks = result.scalars().all()
    return {f"{username}'s tasks": user_tasks}

async def delete_all_tasks(session: AsyncSession) -> None:
    query = await session.execute(
        select(Task).order_by(Task.id)
    )
    tasks = query.scalars().all()
    for task in tasks:
        await session.delete(task)
    await session.commit()
    return {"message": "ok"}

async def delete_user_tasks(
    username: str,
    session: AsyncSession
) -> None:
    query = await session.execute(
        select(Task).where(Task.username == username)
    )
    tasks = query.scalars().all()
    for task in tasks: 
        await session.delete(task)
    await session.commit()
    return {"message": "ok"}
