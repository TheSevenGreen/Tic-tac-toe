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

turn = "❌"

def switch_turn():
    global turn
    turn = "⭕️" if turn == "❌" else "❌"

def pole_keyboards():
    global line
    global index
    global turn
    buttons = []
    for line in range(3): 
        row = []
        for index in range(3): 
            row.append(InlineKeyboardButton(text=field[line][index], callback_data=f"{line}{index}{turn}"))
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def check_win():
        global val1
        win_combos = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        for combo in win_combos:
            a, b, c = combo
            val1 = field[a[0]][a[1]]
            val2 = field[b[0]][b[1]]
            val3 = field[c[0]][c[1]]
            if val1 == val2 == val3 and val1 != " ":
                return True
        return False