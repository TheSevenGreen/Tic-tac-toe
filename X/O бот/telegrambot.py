import asyncio
from aiogram import Bot, Dispatcher,F,types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from config import TOKEN

import keyboards as kb
import lobby as lb

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Поле для крестиков-ноликов:", reply_markup=kb.pole_keyboards())

@dp.callback_query()
async def handle_callback(callback: CallbackQuery):
    data = list(callback.data)
    print(data," --", type(data))
    kb.line = int(data[0])
    kb.index = int(data[1])
    kb.turn = data[2]
    if kb.field[kb.line][kb.index] != " ":
        await callback.message.answer("Клетка уже занята! Попробуй другую.", reply_markup=kb.pole_keyboards())
    else:
        kb.field[kb.line][kb.index] = kb.turn
    kb.switch_turn()
    await callback.message.answer(f"{kb.turn} поставлен в клетку {kb.line}-{kb.index}",reply_markup=kb.pole_keyboards())
    kb.check_win()
    if kb.check_win() == True:
        await callback.message.answer(f"Победил: {kb.val1}")
    

@dp.message(Command("/join_lobby"))
async def join_lobby(message: Message):
    lb.lobbies["players"] = message.from_user.id
    pass


@dp.message(Command("/create_lobby"))
async def create_lobby(message: Message):
    lb.lobbies["host_id"] = message.from_user.id
    lb.lobbies["players"] = message.from_user.id
    await message.answer("Cоздаёться лобби")




async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())