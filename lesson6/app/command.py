from aiogram.filters import Command 
from aiogram import  Router, types


router = Router()

@router.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет пожалуйста продите регистрацию!")

@router.message(Command("about"))
async def about(message:types.Message):
    await message.answer("Команда о нас")

@router.message(Command("info"))
async def info(message:types.Message):
    await message.answer("Geeks")

@router.message(Command("team"))
async def team(message:types.Message):
    await message.answer("мы команда из 3 человек ")

