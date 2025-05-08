import asyncio
from aiogram import Bot, Dispatcher,F,types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery


field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def pole_keyboards():
    global line
    global index
    buttons = []
    for line in range(3): 
        row = []
        for index in range(3): 
            row.append(InlineKeyboardButton(text=field[line][index], callback_data=f"cell_{line}_{index}"))
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


pole_keyboards()
