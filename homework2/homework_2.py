from password import token
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from dop import home
import asyncio


bot = Bot(token = token)
dp = Dispatcher()

 

@dp.message(CommandStart())
async def start(message:types.Message):
    await message.answer("Здраствуйте вас приветствует бот созданый Улуком", reply_markup=home)
    await message.answer("Хотите узнать что я за бот? нажмите на /about")

@dp.message(Command("about")) 
async def about(message:types.Message):
    await message.answer("Ничего толкавого не нашёл))")   

@dp.message(Command("menu"))
async def menu(message:types.Message):
    await message.answer("Вы вернулись начальное меню)) нажмите /start",reply_markup=home)

@dp.message(F.text == "Новости")   
async def new(message:types.Message):
    await message.answer("""Новости на сегодня:Бишкек  – Жогорку Кенеш 18 декабря рассматривает кандидатов на должности главы Кабинета министров Адылбека Касымалиева, его первого заместителя Данияра Амангельдиева и министра экономики Бакыта Сыдыкова.
""") 
    
@dp.message(F.text == "Курсы валют")   
async def cash(message:types.Message):
    await message.answer(f"Курсы разных валют к сому\n\n Курс доллара - 86.90 \n\n Курс рубля - 0.837 \n\n Курс юяня - 11.80") 

@dp.message(F.text == "Контактная информация")
async def info(message:types.Message):
    await message.answer(f"Если вам нужна подробная информация то обращайтесь \n\n Телефон:+996(755)-28-06-06 \n\n Электроная почта: Askarov228666@gmail.com \n\n Всегда рады вам помочь) ")

@dp.message(F.text == "Часто задаваемые вопросы")
async def dop(message:types.Message):
    await message.answer("Почему курс рубля упал?")

@dp.message()
async def help(message:types.Message):
    await message.reply("Извините я вас не понел\n /start - Старт\n/about - Информация о нас ")
    await message.answer("Если хотите вернутся в начальное меню то нажмите /menu")

async def main():
    print("Запуск бота")
    await dp.start_polling(bot)

asyncio.run(main())
  