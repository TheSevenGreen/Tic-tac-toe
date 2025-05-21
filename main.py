import asyncio
from aiogram import Bot, Dispatcher,F,types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from game_keyboard import lobby_keyboards,pole_keyboards,keyboards_buttons
import lobby as lb
from lobby import find_lobby
from GameSession import game
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

bot = Bot(os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
pole = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Выберите режим: ", reply_markup=keyboards_buttons)

@dp.message(Command("clear"))
async def clear_field(message: Message):
    game.field = pole
    await message.answer("Поле очистилось")   

@dp.message(F.text == "🕹 Играть")
async def play(message: Message):
    await message.answer("Игра с самим собой:", reply_markup=await pole_keyboards())

# @dp.callback_query()
# async def handle_callback(callback: CallbackQuery):
#     data = list(callback.data)
#     row = int(data[0])
#     col = int(data[1])
#     game.turn = data[2]
#     if game.field[row][col] != " ":
#         await callback.message.edit_text("Клетка уже занята! Попробуй другую.", reply_markup=await kb.pole_keyboards())
#     else:
#         game.field[row][col] = game.turn
#     game.switch_turn()
#     await callback.message.edit_text(f"{game.turn} поставлен в клетку {row}-{col}",reply_markup=await kb.pole_keyboards())
#     if game.check_win() is True:
#         await callback.message.edit_text(f"Победил: {game.winner}")
#         game.field = pole
#     if game.is_draw() is True:
#         await callback.message.edit_text("Ничья!")    
#         game.field = pole
    



@dp.message(F.text == "🤼‍♂ Присоединиться к лобби")
async def join_lobby(message: Message):
    user_id = message.from_user.id
    lb.handle_join(user_id)
    if lb.waiting_lobby is not None:
        await bot.send_message(user_id, text="Вы зашли в лобби, ожидайте противника")
    else:
        lobby = find_lobby(user_id)
        await bot.send_message(lobby.player_x,text="Игра началась",reply_markup=await lobby_keyboards(user_id))
        await bot.send_message(lobby.player_y,text="Игра началась",reply_markup=await lobby_keyboards(user_id))

@dp.callback_query(F.data.startswith('game_'))
async def handle_callback(callback: CallbackQuery):
    global cl_user_id
    user_id = callback.from_user.id
    data = list(callback.data)
    row = int(data[0])
    col = int(data[1])
    lobby = find_lobby(user_id)
    lobby.game_session.turn = data[2]
    if lobby.game_session.field[row][col] != " ":
        await callback.message.edit_text("Клетка уже занята! Попробуй другую.", reply_markup=await lobby_keyboards(user_id))
    else:
        lobby.game_session.field[row][col] = lobby.game_session.turn
    lobby.game_session.switch_turn()
    await callback.message.edit_text(f"{lobby.game_session.turn} поставлен в клетку {row}-{col}",reply_markup=await lobby_keyboards(user_id))
    if lobby.game_session.check_win() is True:
        await callback.message.edit_text(f"Победил: {lobby.game_session.turn.winner}")
        lobby.game_session.field = pole
    if lobby.game_session.is_draw() is True:
        await callback.message.edit_text("Ничья!")    
        lobby.game_session.field = pole
    



async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())