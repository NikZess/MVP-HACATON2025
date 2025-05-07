from ..kbds.inline import (
    get_user_main_btns,
    get_user_tasks_btns,
    get_user_daily_tasks_btns,
    get_user_information_btns,
    get_user_help_btns,
)

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

async def user_help_menu(level: float, menu_name: str):
    kbds = get_user_help_btns(level=level)
    prefix = "help"
    return kbds, prefix
    
async def get_menu_content(level: float, menu_name: str):
    if level == 0.0:
        return await main_menu(level, menu_name)
    elif level == 1.0:
        return await user_tasks_menu(level, menu_name)
    elif level == 2.0:
        return await user_daily_tasks_menu(level, menu_name)
    elif level == 3.0:
        return await user_information_menu(level, menu_name)
    elif level == 4.0:
        return await user_help_menu(level, menu_name)
    else:
        return await main_menu(0.0, "main")  
