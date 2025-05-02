from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession 
from ...core.models.db_helper import get_async_session
from . import crud

router = APIRouter(tags=["Authentication"])

@router.post("/login", summary="Авторизация администратора")
async def login_admin(
    username: str,
    password: str,
    responce: Response,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.login_admin(
        session=session,
        username=username,
        password=password,
        response=responce
    )