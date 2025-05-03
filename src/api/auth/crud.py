from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Response, HTTPException, status
from .authx_config import security, config
<<<<<<< HEAD
from ...core.config import admin_data
=======
>>>>>>> 06bdc42 (crud funcs for users)
from ...core.models import Admin

async def login_admin(
    session: AsyncSession,
    username: str,
    password: str,
    response: Response,
):
    query = select(Admin).where(Admin.username == username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Администратор не найден"
        )
    
    if user.password != password:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль"
        )
    
    access_token = security.create_access_token(uid=str(user.id))
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
    
    return {"access_token": access_token}