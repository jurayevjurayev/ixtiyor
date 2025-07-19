import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "7983671016:AAGS7mWsgsuSUKQVGJtY9W75fmCbuFUIeUo"  # ← Bu yerga o'z tokeningizni yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! Bot ishga tushdi va Render’da 24/7 ishlamoqda.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
