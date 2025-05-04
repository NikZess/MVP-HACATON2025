from aiogram import types
from ..kbds.inline import (
    get_user_main_btns,
)

async def main_menu(level: float, menu_name: str, message: types.Message):
    description = "<strong>Главное меню бота</strong>"
    kbds = get_user_main_btns(level=level)
    return description, kbds

async def get_menu_content(
    level: float,
    menu_name: str,
    message: types.Message
):
    if level == 0:
        return await main_menu(level, menu_name, message)