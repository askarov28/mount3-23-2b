import asyncio 
from aiogram import types 
from app.homework_8 import bot, dp, set_bot_commands 
from app.parsing import parse_website 
 
@dp.message(commands=["start"]) 
async def start_command(message: types.Message): 
    await message.answer( 
        "Привет! Я парсинг-бот. Используй /parse, чтобы запустить парсинг, или /help для получения информации." 
    ) 
 
@dp.message(commands=["parse"]) 
async def parse_command(message: types.Message): 
    try: 
        url = "https://example.com"  # Укажите URL для парсинга 
        result = await parse_website(url) 
        await message.answer(f"✅ Результаты парсинга:\n{result}") 
    except Exception as e: 
        await message.answer(f"⚠️ Ошибка при парсинге: {e}") 
 
# Обработчик команды /help 
@dp.message(commands=["help"]) 
async def help_command(message: types.Message): 
    await message.answer( 
        "Я могу:\n" 
        "/start — начать работу\n" 
        "/parse — спарсить данные с сайта\n" 
        "/help — показать это сообщение" 
    ) 
 
 
async def main(): 
  
    await set_bot_commands() 
    
    await dp.start_polling(bot) 
 
if __name__ == "__main__": 
    asyncio.run(main())