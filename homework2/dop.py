from aiogram.types import KeyboardButton , ReplyKeyboardMarkup

home= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Новости")],
        [KeyboardButton(text="Курсы валют")],
        [KeyboardButton(text="Контактная информация")],
        [KeyboardButton(text="Часто задаваемые вопросы ")]

    ],
    resize_keyboard=True
)