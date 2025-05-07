from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from sqlalchemy import select

from src.core.models import User, Task, TaskDaily, Information
from src.core.models.db_helper import get_async_session

from ..filters.chat_type_filter import ChatTypeFilter
from ..kbds.inline import MenuCallBack
from .menu_processing import get_menu_content

router = Router()
router.message.filter(ChatTypeFilter(["private"]))

@router.message(CommandStart())
async def command_start_handler(message: types.Message):
    reply_markup, _ = await get_menu_content(level=0, menu_name="main")
    await message.answer("<strong>Главное меню</strong>", reply_markup=reply_markup)


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack):
    print(callback_data)
    reply_markup, prefix = await get_menu_content(
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    username = callback.from_user.username
    async for session in get_async_session():
        if prefix == "main":
            description = "<strong>Главное меню</strong>"
        if prefix == "tasks":
            main = "<strong>Ваши задачи: </strong>\n\n"
            query = await session.execute(
                select(Task).where(Task.username == username)
            )
            tasks = query.scalars().all()
            if not tasks:
                description = "У вас пока, что нет задач."
            else:
                for task in tasks:
                    main += f"• {task.description}\n"
                description = main
        if prefix == "daily_tasks":
            main = "<strong>Ваши ежедневные задачи: </strong>\n\n"
            query = await session.execute(
                select(TaskDaily).where(TaskDaily.username == username)
            )
            tasks = query.scalars().all()
            if not tasks:
                description = "У вас пока, что нет ежедневных задач."
            for task in tasks:
                main += f"• {task.description}\n"
            description = main
        if prefix == "information":
            main = "<strong>Информация:</strong>\n\n"
            query = await session.execute(
                select(Information).where(Information.username == username)
            )
            information = query.scalar()
            if not information:
                description = "Информации о вас пока, что нет."
            else:
                description = f"<strong>Информация о вас:</strong> \n\nДолжность: {information.job_title}\n\
Место работы: {information.work_place}\nВремя работы: {information.timetable}"
    try:
        await callback.message.edit_text(description, reply_markup=reply_markup)
    except Exception as e:
        await callback.answer("Не удалось обновить меню. Попробуйте позже.")

    await callback.answer()

@router.message(Command("tasks"))
async def command_tasks_handler(message: Message):
        username = message.from_user.username
        async for session in get_async_session():
            tasks = await session.execute(
                select(Task).where(Task.username == username)
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
