from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ...core.models import User, Information
from .schemas import InformationCreate

async def create_information(
    information_data: InformationCreate,
    session: AsyncSession,
) -> Information:
    query = await session.execute(
        select(User).where(User.username == information_data.username)
    )
    user = query.scalar_one_or_none()
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )
    information = Information(
        username=user.username,
        job_title=information_data.job_title,
        work_place=information_data.work_place,
        timetable=information_data.timetable,
    )
    session.add(information)
    await session.commit()
    return {"status": "ok", "information": information}

async def get_all_informations(session: AsyncSession) -> list[Information]:
    query = await session.execute(
        select(Information).order_by(Information.id)
    ) 
    informations = query.scalars().all()
    return {"informations_about_users": informations}

async def get_user_information(
    username: str,
    session: AsyncSession
) -> Information:
    query = await session.execute(
        select(Information).where(Information.username == username)
    )
    information = query.scalars().all()
    return {f"{username} information": information}

async def delete_all_informations(session: AsyncSession) -> None:
    query = await session.execute(
        select(Information).order_by(Information.id)
    )
    informations = query.scalars().all()
    for info in informations:
        await session.delete(info)
    await session.commit()
    return {"message": "ok"}

async def delete_user_information(
    username: str,
    session: AsyncSession,
) -> None:
    query = await session.execute(
        select(Information).where(Information.username == username)
    )
    information = query.scalars().all()
    for info in information:
        await session.delete(info)
    await session.commit()
    return {"message": "ok"}