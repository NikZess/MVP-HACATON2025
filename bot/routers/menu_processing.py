from aiogram import types
from ..kbds.inline import (
    get_user_main_btns,
    get_user_tasks_btns,
    get_user_daily_tasks_btns,
    get_user_information_btns,
)
from ..utils.text_inline import get_description_tasks
from src.core.models.db_helper import get_async_session


async def main_menu(level: float, menu_name: str):
    kbds = get_user_main_btns(level=level)
    prefix = "main"
    return kbds, prefix


async def user_tasks_menu(level: float, menu_name: str):
    kbds = get_user_tasks_btns(level=level)
    prefix = "tasks"
    return kbds, prefix

async def user_daily_tasks_menu(level: float, menu_name: str):
    kbds = get_user_daily_tasks_btns(level=level)
    prefix = "daily_tasks"
    return kbds, prefix

async def user_information_menu(level: float, menu_name: str):
    kbds = get_user_information_btns(level=level)
    prefix = "information"
    return kbds, prefix


async def get_menu_content(level: float, menu_name: str):
    if level == 0:
        return await main_menu(level, menu_name)
    if level == 1.0:
        return await user_tasks_menu(level, menu_name)
    if level == 2.0:
        return await user_daily_tasks_menu(level, menu_name)
    if level == 3.0:
        return await user_information_menu(level, menu_name)

