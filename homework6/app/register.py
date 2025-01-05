from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3

router = Router()

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    address TEXT,
    phone TEXT
)''')
conn.commit()


class OrderStates(StatesGroup):
    waiting_for_product = State()
    waiting_for_address = State()
    waiting_for_phone = State()


@router.message(OrderStates.waiting_for_product)
async def handle_product(message:types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer("Введите адрес доставки:")
    await state.set_state(OrderStates.waiting_for_address)

@router.message(OrderStates.waiting_for_address)
async def handle_address(message:types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(OrderStates.waiting_for_phone)

@router.message(OrderStates.waiting_for_phone)
async def handle_phone(message:types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()

    confirmation_message = (
        f"Пожалуйста, подтвердите ваш заказ:\n"
        f"Товар: {user_data['product']}\n"
        f"Адрес доставки: {user_data['address']}\n"
        f"Телефон: {user_data['phone']}\n"
        "Напишите 'подтвердить' для подтверждения или 'отменить' для отмены."
    )
    await message.answer(confirmation_message)
    await state.clear()

@router.message()
async def confirmation_handler(message:types.Message):
    if message.text.lower() == 'подтвердить':
        user_data = await State.get_data()
        cursor.execute('''INSERT INTO orders (user_id, product, address, phone) VALUES (?, ?, ?, ?)''',
                       (message.from_user.id, user_data['product'], user_data['address'], user_data['phone']))
        conn.commit()
        await message.answer("Ваш заказ подтверждён! Спасибо за покупку.")
    elif message.text.lower() == 'отменить':
        await message.answer("Ваш заказ отменён.")
    else:
        await message.answer("Пожалуйста, напишите 'подтвердить' или 'отменить'.")
