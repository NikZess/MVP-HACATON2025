from fastapi import APIRouter, Depends, status
from . import crud
from ...core.models.db_helper import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.authx_config import security
from .schemas import InformationCreate
 
router = APIRouter(
    tags=["Informations"],
)

@router.post("/",
    summary="Добавить информацию для пользователя",
    description="Добавляет информацию для пользователя по его username",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security.access_token_required)],
)
async def create_information(
    information_data: InformationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.create_information(
        information_data=information_data,
        session=session,
    )

@router.get("/",
    summary="Получить всю базу информации о пользователях",
    description="Возвращает всю базу данных информации, о всех пользователях",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)],
)
async def get_all_informations(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_all_informations(session=session)

@router.get("/{username}/",
    summary="Получить информацию о пользователе",
    description="Возвращает всю информацию о пользователе из базы данных по его username",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(security.access_token_required)],
)
async def get_user_information(
    username: str,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.get_user_information(
        username=username,
        session=session,
    )

@router.delete("/",
    summary="Удалить всю информацию о пользователях",
    description="Удаляет всю информацию, о всех пользователях из базы данных",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_all_informations(session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_all_informations(session=session)

@router.delete("/{username}/",
    summary="Удалить всю информацию о пользователе",
    description="Удаляет всю информацию о пользователе из базы данных по его username",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security.access_token_required)],
)
async def delete_user_information(
    username: str,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.delete_user_information(
        username=username,
        session=session,
    )