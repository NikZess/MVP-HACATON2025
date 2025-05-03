from sqlalchemy import select
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from ...core.models import User

async def get_users(session: AsyncSession) -> list[User]:
    query = select(User).order_by(User.id)
    result = await session.execute(query)
    users = result.scalars().all()
    return list(users)

async def get_user_by_username(
    session: AsyncSession, 
    username: str
) -> User | None:
    query = select(User).where(User.username == username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user

async def delete_all_users(session: AsyncSession) -> dict:
    query = await session.execute(select(User))
    users = query.scalars().all()
    for user in users:
        await session.delete(user)
    await session.commit()
    return {"message": "ok"}

async def delete_user_by_username(
    session: AsyncSession, 
    user: User,    
) -> None:
    await session.delete(user)
    await session.commit()
    return {"message": "ok"}
