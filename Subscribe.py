import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
load_dotenv()
bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Приобрести подписку"))
    builder.add(types.KeyboardButton(text="Помощь"))
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я асинхронный бот иммитирования покупки подписки",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )
@dp.message(F.text == "Приобрести подписку")
async def order_coffee(message: types.Message):
    await message.answer("Начинаю обрабатывать вашу покупку... Подождите 3 секунды")
    await asyncio.sleep(3) 
    await message.answer("Ваша подписка активирована!")
@dp.message(F.text == "Помощь")
async def help_cmd(message: types.Message):
    await message.answer("Я умею активировать подписку. Просто нажми на кнопку!")
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())