from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ...core.models import Task, User
from ...core.models.db_helper import get_async_session
from .schemas import TaskCreate
from ...core.models import User, Task
from sqlalchemy import select
from typing import Annotated
from annotated_types import MinLen, MaxLen

async def create_task(
    username: str,
    description: Annotated[str, MinLen(3), MaxLen(1000)],
    session: AsyncSession,
):
    query = await session.execute(
        select(User).where(User.username == username)
    )
    user = query.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    task = Task(
        user_id=user.username,
        description=description,
    )
    session.add(task)
    await session.commit()
    return {"status": "ok", "task_id": task.id}