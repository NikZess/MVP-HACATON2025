import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher, types

from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from bot.routers.user_private import router as user_private_router
from bot.routers.user_group import router as user_group_router
from bot.routers.admin_private import router as admin_private_router
from bot.common.bot_cmds_list import private

from src.core.config import bot_data

ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

bot = Bot(token=bot_data.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())