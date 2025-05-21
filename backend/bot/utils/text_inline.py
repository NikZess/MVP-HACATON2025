from src.api.tasks.crud import get_user_tasks
from sqlalchemy.ext.asyncio import AsyncSession

async def get_description_tasks(username: str, session: AsyncSession):
    return await get_user_tasks(username=username, session=session)