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

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Поле для крестиков-ноликов:", reply_markup=kb.pole_keyboards())


@dp.callback_query(F.data == f"cell_{0}_{0}")
async def handle_callback(callback: CallbackQuery):
    await callback.message.answer(f"cell_{0}_{0}")
    # await callback.answer("({kb.line},{kb.index})")


async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())