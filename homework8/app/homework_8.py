from aiogram import Bot , Dispatcher
from aiogram.types import BotCommand
from app.password import token

bot = Bot(token = token , parse_mode = "HTML")
dp = Dispatcher()


async def set_bot_commands():
    await bot.set_bot_commands([
        BotCommand (command="/start", description = "Начать работу"),
        BotCommand (command="/parse", description = "Запуск бота"),
        BotCommand (command="/help", description = "Помошь")
])