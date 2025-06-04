from fastapi import APIRouter, status, Depends
from ...core.models.db_helper import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import user_by_username
from ...core.models import User
from . import crud
from ..auth.authx_config import security

router = APIRouter(tags=["Users"])

@router.get("/", 
    summary="Получить всех пользователей", 
    description="Возвращает всех пользователей из базы данных",
    status_code=status.HTTP_200_OK, 
    dependencies=[Depends(security.access_token_required)],
)
async def get_users(
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.get_users(session=session)


@router.get("/{username}/", 
    summary="Получить конкретного пользователя",
    description="Возвращает пользователя из базы данных по его username",
    status_code=status.HTTP_200_OK, 
    dependencies=[Depends(security.access_token_required)],
)
async def get_user_by_username(
    user: User = Depends(user_by_username),
):
    return user


@router.delete("/", 
    summary="Удалить всех пользователей",
    description="Удаляет всех пользователей из базы данных",
    status_code=status.HTTP_204_NO_CONTENT, 
    dependencies=[Depends(security.access_token_required)],
)
async def delete_all_users(
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.delete_all_users(session=session)


@router.delete("/{username}/", 
    summary="Удаление пользователя", 
    description="Удаляет пользователя из базы данных по его username",
    status_code=status.HTTP_204_NO_CONTENT, 
    dependencies=[Depends(security.access_token_required)],
)
async def delete_user_by_username(
    user: User = Depends(user_by_username),
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.delete_user_by_username(
        session=session,
        user=user,
    )


