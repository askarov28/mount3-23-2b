# from password import token
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import Command, CommandStart
# import asyncio
# from button import keybord_main, generate_menu_keyboard,keyboard_confirm,MENU

# bot = Bot(token=token)
# dp = Dispatcher()



# @dp.message(CommandStart())
# async def start(message:types.Message):
#     await message.answer("Привет Добро пожаловать", reply_markup=keybord_main)

# @dp.message(F.text == 'О нас')
# async def about(message:types.Message):
#     await message.answer("Информация о нас")

# @dp.message(F.text == 'ИНФО')
# async def info(message:types.Message):
#     await message.answer("улук")

# @dp.message(F.text == 'Контакты')
# async def phone(message:types.Message):
#     await message.answer("0755280606")

# @dp.message(F.text == 'Приветствие')
# async def hello(message:types.Message):
#     await message.answer("всем привет ")

# @dp.message(F.text == "Выбрать напиток")   
# async def choose_drink(message:types.Message):
#     keyboard = generate_menu_keyboard() 
#     await message.answer("Выберитк напиток ", reply_markup=keyboard)

# @dp.message(F.text.in_(MENU))
# async def drink_choice(message:types.Message):
#     select_drink = message.text
#     await message.answer(f"Вы выбрали {select_drink}.Хотите заказать этот напиток?",reply_markup = keyboard_confirm())  

# @dp.message(F.text == 'Да, потвердить')
# async def yes(message:types.Message):
#     await message.answer("Спасибо за заказ приятного употребления")

# @dp.message(F.text == 'Отмена')
# async def nots(message:types.Message):
#     await message.answer("Хорошо всего доброго")

# @dp.message(Command("locations"))
# async def locations(message:types.Message):
#     longitude = 72.7868
#     latitude = 40.5269
#     await message.answer("Локаций города ош")
#     await message.answer_location(latitude, longitude)

# @dp.message(Command("gallery"))
# async def gallery(message:types.Message):
#     photos = [
#         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStkKOvvAmBTYqfpzWsvz1NABFduBZa_fb9eA&s",
#         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8BzUXffTE_rKv0TpBeCc2qzvdzmELN-y4DA&s",
#         ""
#     ]
#     for photo in photos:
#         await message.answer_photo(photo, caption="Фото из галереи")

# @dp.message()
# async def help(message:types.Message):
#     await message.reply("Извините я вас не понел\n /start - Старт\n/locations - Наши локация\n /gallery - Наша галлерия")

# async def main():
#     print("Запуск бота")
#     await dp.start_polling(bot)

# asyncio.run(main())