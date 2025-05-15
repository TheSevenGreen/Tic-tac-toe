import asyncio
from aiogram import Bot, Dispatcher,F,types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
import GameSession as gm
import lobby as lb

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
    global row
    global col
    global turn
    buttons = []
    for row in range(3): 
        line = []
        for col in range(3): 
            line.append(InlineKeyboardButton(text=gm.game.field[row][col], callback_data=f"{row}{col}{turn}"))
        buttons.append(line)
    return InlineKeyboardMarkup(inline_keyboard=buttons)



keyboards = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text="🤼‍♂ Присоединиться к лобби")],
[KeyboardButton(text="🕹 Играть")]],
    resize_keyboard=True,)

async def lobby_keyboards(self):
    global row
    global col
    global turn
    buttons = []
    for row in range(3): 
        line = []
        for col in range(3): 
            line.append(InlineKeyboardButton(text=lb.game.game_session.field[row][col], callback_data=f"{row}{col}{self.turn}"))
        buttons.append(line)
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# line.append(InlineKeyboardButton(text=self.game_session.field[row][col], callback_data=f"{row}{col}{self.turn}"))
