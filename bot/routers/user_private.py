from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from sqlalchemy import select

from src.core.models import User, Task, TaskDaily, Information
from src.core.models.db_helper import get_async_session

from ..filters.chat_type_filter import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(["private"]))

@router.message(CommandStart())
async def command_start_handler(message: types.Message):
    telegram_id = message.from_user.id
    async for session in get_async_session():
        query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        
        await message.answer("Привет, это бот помощник 🤖, который поможет тебе в твоей карьере программиста ⌨️")
        if not user:
            await message.answer("Чтобы начать пользоваться ботом, зарегистрируйтесь - /register")

@router.message(Command("tasks"))
async def command_tasks_handler(message: Message):
        username = message.from_user.username
        async for session in get_async_session():

            tasks = await session.execute(
                select(Task).where(Task.user_id == username)
            )
            tasks = tasks.scalars().all()

            if tasks:
                text = "Ваши задачи:\n"
                for task in tasks:
                    text += f"• {task.description}\n"
                await message.answer(text)
            else:
                await message.answer("У вас пока нет задач!")

@router.message(Command("daily_tasks"))
async def command_daily_tasks_handler(message: types.Message):
    await message.answer("Ежедневные задачи: ")
    
@router.message(Command("info"))
async def command_daily_tasks_handler(message: types.Message):
    await message.answer("Информация: ")

    username = message.from_user.username
    async for session in get_async_session():
        query = await session.execute(
            select(Task).where(Task.username == username)
        )
        tasks = query.scalars().all()
        if tasks:
            text = "Ваши задачи:\n"
            for task in tasks:
                text += f"• ✅ {task.description}\n"
            await message.answer(text)
        else:
            await message.answer("У вас пока нет задач!")

@router.message(Command("daily_tasks"))
async def command_daily_tasks_handler(message: types.Message):
    username = message.from_user.username
    async for session in get_async_session():
        query = await session.execute(
            select(TaskDaily).where(TaskDaily.username == username)
        )
        tasks_daily = query.scalars().all()
        if tasks_daily:
            text = "Ежедневные задачи:\n"
            for task in tasks_daily:
                text += f"• ✅ {task.description}\n"
            await message.answer(text)
        else:
            await message.answer("У вас пока нет задач!")
    
@router.message(Command("info"))
async def command_user_information_handler(message: types.Message):
    username = message.from_user.username
    async for session in get_async_session():
        query = await session.execute(
            select(Information).where(Information.username == username)
        )
        information = query.scalar()
        await message.answer(f"<strong>Информация о вас:</strong> \n\nДолжность: {information.job_title}\n\
Место работы: {information.work_place}\nВремя работы: {information.timetable}")

    
@router.message(Command("register"))
async def command_register_handler(message: Message):
    async for session in get_async_session():
    
        telegram_id = message.from_user.id
        full_name = message.from_user.full_name
        username = message.from_user.username

        query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if not user:
            new_user = User(
                telegram_id=telegram_id,
                full_name=full_name,
                username=username,
            )
            session.add(new_user)
            await session.commit()
            await message.answer("Добро пожаловать! Вы успешно зарегистрированы!")
                        
        else:
            await message.answer("Вы уже зарегистрированы")
