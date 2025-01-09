from aiogram import Bot , Dispatcher
import asyncio , logging , os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

bot = Bot(token = os.environ.getnv("token"))
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

