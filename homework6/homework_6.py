from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from app.register import router as register
import asyncio , os , logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv ()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message:types.Message):
    await message.answer("Добро пожаловать! Какой товар вы хотите заказать?")


async def main():
    dp.include_router(register)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())