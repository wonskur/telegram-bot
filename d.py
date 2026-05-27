import os
import asyncio
import aiogram
import dotenv
from aiogram.filters import CommandStart
dotenv.load_dotenv()
token = os.getenv("TG_TOKEN")
bot = aiogram.Bot(token=token)
dp = aiogram.Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message: aiogram.types.Message):
    await message.answer("Привет! Я запущен и готов к работе.")
@dp.message()
async def echo(message: aiogram.types.Message):
    if message.text:
        await message.answer(message.text)
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("bot started")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())