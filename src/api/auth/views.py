from fastapi import APIRouter, Response, Depends, Request
# from fastapi.templating import 
from sqlalchemy.ext.asyncio import AsyncSession 
from ...core.models.db_helper import get_async_session
from . import crud
from .schemas import User
from ...core.utils.templates import templates

router = APIRouter(tags=["Authentication"])

from fastapi.responses import JSONResponse

@router.post("/login", summary="Авторизация администратора")
async def login_admin(
    user_data: User,
    response: Response,
    request: Request,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.login_admin(
        user_data=user_data,
        session=session,
        response=response,
    )
