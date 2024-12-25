# from aiogram import Bot,Dispatcher,types,F
# from aiogram.filters import Command
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from password import token
# import asyncio

# bot = Bot(token = token)
# dp = Dispatcher()

# AVTO={
# "Зимний шины":1500,
# "Летние шины":1000,
# "Все сизонный шины":860,
# "Шипованный шины":1550
# }

# MOB={
# "Зарядник тайпси":350,
# "Лупа для камер":480,
# "Зашитное стекло":250
# }

# orders={}

# @dp.message(Command("start"))
# async def start(message:types.Message):
#     await message.answer("Добро пожаловать в онлайн магазин.\n Для выбора авто запчастей переходите-> /avto \n Для выбора мобильных запчастей пероходите-> /mob")

# @dp.message(Command("avto"))
# async def avto(message:types.Message):
#     builder = InlineKeyboardBuilder()

#     for spares, price in AVTO.items():
#         builder.button(
#             text=f"{spares} - {price}",
#             callback_data=f"avto_{spares}"
#         )
#     builder.adjust(2)
#     await message.answer("Каталок запчастей : ", reply_markup=builder.as_markup())

# @dp.callback_query(F.data.startswith("avto_"))
# async def choose_spares(callback: types.CallbackQuery):
#     spares = callback.data.split("_")[1]
#     orders[callback.from_user.id] = {"spares" : spares, "quantity": 1}

#     builder = InlineKeyboardBuilder()
#     for i in range(1, 6):
#         builder.button(
#             text=str(i),
#             callback_data=f"quantity_{i}"
#         )
#     builder.adjust(2)
#     await callback.message.answer(f"Вы выбрали {spares}. Укажите количество: ", 
#                                   reply_markup=builder.as_markup())

# @dp.callback_query(F.data.startswith("quantity_"))
# async def choose_quantity(callback:types.CallbackQuery):
#     quantity = int(callback.data.split("_")[1])
#     user_id = callback.from_user.id

#     if user_id in orders:
#         orders[user_id]['quantity'] = quantity
#         spares = orders[user_id]['spares']
#         price = AVTO[spares] * quantity

#         builder = InlineKeyboardBuilder()
#         builder.button(
#             text="Подтвердить заказ",
#             callback_data="confirm_orders"
#         )

#         await callback.message.answer(
#             f"Ваш заказ: {spares} x {quantity} = {price} сомов.\nПодтвердите Заказ?",
#             reply_markup=builder.as_markup()
#         )

# @dp.callback_query(F.data == "confirm_orders")
# async def confirm_orders(callback:types.CallbackQuery):
#     user_id = callback.from_user.id

#     if user_id in orders:
#         spares = orders[user_id]['spares']
#         quantity = orders[user_id]['quantity']
#         total_price = AVTO[spares] * quantity

#         del orders[user_id]

#         await callback.message.answer(
#             f"Спасибо за заказ!\nВы заказали: {spares} x{quantity}.\nИтог к оплате: {total_price} сомов"
#         )



# @dp.message(Command("mob"))
# async def mob(message:types.Message):
#     builder = InlineKeyboardBuilder()

#     for zap, price in MOB.items():
#         builder.button(
#             text=f"{zap} - {price}",
#             callback_data=f"mob_{zap}"
#         )
#     builder.adjust(2)
#     await message.answer("Список товара для телефона: ", reply_markup=builder.as_markup())

# @dp.callback_query(F.data.startswith("mob_"))
# async def choose_zap(callback: types.CallbackQuery):
#     zap = callback.data.split("_")[1]
#     orders[callback.from_user.id] = {"zap" : zap, "quantity": 1}

#     builder = InlineKeyboardBuilder()
#     for i in range(1, 6):
#         builder.button(
#             text=str(i),
#             callback_data=f"quantity_{i}"
#         )
#     builder.adjust(2)
#     await callback.message.answer(f"Вы выбрали {zap}. Укажите количество: ", 
#                                   reply_markup=builder.as_markup())

# @dp.callback_query(F.data.startswith("quantity_"))
# async def choose_quantity(callback:types.CallbackQuery):
#     quantity = int(callback.data.split("_")[1])
#     user_id = callback.from_user.id

#     if user_id in orders:
#         orders[user_id]['quantity'] = quantity
#         zap = orders[user_id]['zap']
#         price = MOB[zap] * quantity

#         builder = InlineKeyboardBuilder()
#         builder.button(
#             text="Подтвердить заказ",
#             callback_data="confirm_orders"
#         )

#         await callback.message.answer(
#             f"Ваш заказ: {zap} x {quantity} = {price} сомов.\nПодтвердите Заказ?",
#             reply_markup=builder.as_markup()
#         )

# @dp.callback_query(F.data == "confirm_orders")
# async def confirm_orders(callback:types.CallbackQuery):
#     user_id = callback.from_user.id

#     if user_id in orders:
#         zap = orders[user_id]['zap']
#         quantity = orders[user_id]['quantity']
#         total_price = MOB[zap] * quantity

#         del orders[user_id]

#         await callback.message.answer(
#             f"Спасибо за заказ!\nВы заказали: {zap} x{quantity}.\nИтог к оплате: {total_price} сомов"
#         )



# async def main():
#     print("Запуск бота")
#     await dp.start_polling(bot)

# asyncio.run(main())



