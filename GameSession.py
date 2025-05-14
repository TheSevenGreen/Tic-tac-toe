import asyncio
from aiogram import Bot, Dispatcher,F,types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from main import user_id

class GameSession:
    def __init__(self):
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "❌"
        
    async def pole_keyboards(self):
        global row
        global col
        global turn
        buttons = []
        for row in range(3): 
            line = []
            for col in range(3): 
                line.append(InlineKeyboardButton(text=self.field[row][col], callback_data=f"{row}{col}{self.turn}"))
            buttons.append(line)
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    def make_turn(self, row, col):
        if self.field[row][col] != " ":
            await bot.send_message(user_id, text="Привет!")
            return False
        self.field[row][col] = self.turn
        return True

    def switch_turn(self):
        self.turn = "⭕️" if self.turn == "❌" else "❌"

    def check_win(self):
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
            val1 = self.field[a[0]][a[1]]
            val2 = self.field[b[0]][b[1]]
            val3 = self.field[c[0]][c[1]]
            if val1 == val2 == val3 and val1 != " ":
                return True
        return False

    def is_draw(self):
        for row in self.field:
            if " " in row:
                return False
        return True
    
game = GameSession()