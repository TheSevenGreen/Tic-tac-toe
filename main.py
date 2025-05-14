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
import GameSession as gm

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("хуй", reply_markup=kb.keyboards)

# reply_markup=kb.pole_keyboards()

@dp.message(F.text == "🕹 Играть")
async def play(message: Message):
    await message.answer("Игра с самим собой:", reply_markup=kb.pole_keyboards())

@dp.callback_query()
async def handle_callback(callback: CallbackQuery):
    data = list(callback.data)
    kb.row = int(data[0])
    kb.col = int(data[1])
    kb.turn = data[2]
    if kb.field[kb.row][kb.col] != " ":
        await callback.message.answer("Клетка уже занята! Попробуй другую.", reply_markup=kb.pole_keyboards())
    else:
        kb.field[kb.row][kb.col] = kb.turn
    gm.game.switch_turn()
    await callback.message.answer(f"{kb.turn} поставлен в клетку {kb.row}-{kb.col}",reply_markup=kb.pole_keyboards())
    gm.game.check_win()
    if gm.game.check_win() == True:
        await callback.message.answer(f"Победил: {gm.val1}")
    

@dp.message(F.text == "🤼‍♂ Присоединиться к лобби")
async def join_lobby(message: Message):
    user_id = message.from_user.id
    abc = "4353244353"
    await bot.send_message(user_id, text="Привет!")
    if user_id != None:
        print("user_id не пустой")
        print(user_id)
        print(lb.playing_lobbies)
    else:
        print("user_id пустой")
    lb.handle_join(user_id)
    for i in lb.playing_lobbies:
        print(i)
        print(i)
    






async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())