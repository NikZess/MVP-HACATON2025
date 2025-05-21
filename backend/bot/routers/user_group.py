import asyncio
import time

from aiogram import Bot, types, Router
from aiogram.filters import Command

from ..filters.chat_type_filter import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(["group", "supergroup"]))
router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))

@router.message(Command("admin"))
async def auth_admin(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    
    if message.from_user.id in admins_list:
        await message.delete()
        
        full_name = message.from_user.full_name
        time_message = await message.answer(f"Пользователь {full_name} успешно вошел в админ-панель")
        time.sleep(3)
        await time_message.delete()