import os
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
load_dotenv()
gtoken = os.getenv("GEMINI_TOKEN")
genai.configure(api_key=gtoken)
model = genai.GenerativeModel('gemini-flash-latest')
bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я бот, который может ответить на твой вопрос")
@dp.message()
async def ai(message: types.Message):
    if not message.text:
        return
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        response = await model.generate_content_async(message.text)
        await message.answer(response.text)
    except Exception as e:
        print(f"Ошибка при запросе к Gemini: {e}")
        await message.answer("Произошла ошибка")
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот запущен...")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())