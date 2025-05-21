from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy import select

from ..models.admin import AddAdmin

from ..filters.chat_type_filter import ChatTypeFilter, IsAdmin

from src.core.models import Admin
from src.core.models.db_helper import get_async_session

router = Router()
router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

@router.message(StateFilter(None), Command("admin"))
async def set_admin(message: types.Message, state: FSMContext): 
    async for session in get_async_session():
        telegram_id = message.from_user.id
        query = select(Admin).where(Admin.telegram_id == telegram_id)
        result = await session.execute(query)
        admin = result.scalar_one_or_none()    
            
        if admin:
            await message.answer("Вы уже зарегистрированы")
        else:
            await message.answer("Зарегистрируйтесь, как администратор. Для этого придумайте пароль")
            await state.set_state(AddAdmin.password)
    
@router.message(AddAdmin.password, F.text)
async def add_admin_password(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    
    async for session in get_async_session():
        telegram_id = message.from_user.id
        full_name = message.from_user.full_name
        username = message.from_user.username
        password = data["password"]
        
    admin = await session.get(Admin, telegram_id)
    
    if not admin:
        new_admin = Admin(
            telegram_id=telegram_id,
            full_name=full_name,
            username=username,
            password=password
        )
        session.add(new_admin)
        await session.commit()
        await message.answer(f"Администратор {full_name} был успешно зарегистрирован")
    elif admin:
        await message.answer(f"Администратор {full_name} уже зарегистрирован")
    await state.clear()
    
@router.message(AddAdmin.password, F.text)
async def add_name(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели недопустимые данные, введите пароль")