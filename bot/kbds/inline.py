from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class MenuCallBack(CallbackData, prefix="menu"):
    level: float
    menu_name: str
    page: int = 0


def get_user_main_btns(*, level: float, sizes: tuple[int] = (2, 1, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Общие задачи 📔": "tasks",
        "Ежедневные задачи 📕": "daily_tasks",
        "Информация и помощь ✏️": "information",
        "Регистрация ®️": "register",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "tasks":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1.0, menu_name=menu_name).pack()
            ))
        if menu_name == "daily_tasks":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=2.0, menu_name=menu_name).pack()
            ))
        if menu_name == "information":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))
        if menu_name == "register":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=4.0, menu_name=menu_name).pack()
            ))
    return keyboard.adjust(*sizes).as_markup()

def get_user_tasks_btns(*, level: float, sizes: tuple[int] = (1, )) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Назад 🔙": "back_menu_from_tasks_menu",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "back_menu_from_tasks_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))
    return keyboard.adjust(*sizes).as_markup()

def get_user_daily_tasks_btns(*, level: float, sizes: tuple[int] = (1, )) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Назад 🔙": "back_menu_from_daily_tasks_menu",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "back_menu_from_daily_tasks_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))
    return keyboard.adjust(*sizes).as_markup()

def get_user_information_btns(*, level: float, sizes: tuple[int] = (1, )) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Назад 🔙": "back_menu_from_information_menu",        
    }
    
    for text, menu_name in btns.items():
        if menu_name == "back_menu_from_information_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name="main").pack()
            ))
    return keyboard.adjust(*sizes).as_markup()
