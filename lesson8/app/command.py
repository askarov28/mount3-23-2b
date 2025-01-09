from aiogram import Router , types
from app.parsing import get_news
from aiogram.filters import Command

router = Router()

@router.message(Command("news"))
async def news (message:types.Message):
    try:
        new = get_news()
        if news:
            await message.answer("\n\n".join(news))
        else:
            await message.answer("Новостей не найдино ")  

    except Exception as e:
        logging.error(f"Ошибка ")       
