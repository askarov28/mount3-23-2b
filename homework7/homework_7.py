from aiogram import Bot , types , Dispatcher , F
from aiogram.filters import Command, CommandStart
import sqlite3
import asyncio
import aioschedule
from password import token
from datetime import datetime
import logging  
logging.basicConfig(level=logging.INFO)

bot = Bot(token = token)
dp = Dispatcher()

connect = sqlite3.connect("schedule.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS schedules (    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,    task TEXT,
    time TEXT)
""")
               
connect.commit()

@dp.message(CommandStart())
async def start_command(message:types.Message):
    user_id = message.from_user.id    
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    connect.commit()    
    await message.answer("Вы успешно зарегистрированы! Используйте команду /task, чтобы добавить задачу.")

@dp.message(Command('task'))
async def task_(message:types.Message):    
    await message.answer('Введите задачу:')

@dp.message(F.text)
async def save_task(message:types.Message):
    user_id = message.from_user.id
    task = message.text            
    cursor.execute("INSERT INTO schedules (user_id, task) VALUES (?, ?)", (user_id, task))
    connect.commit()           
    await message.answer("Задача успешно добавлена! Воспользуйтесь командами:  \n1.Для настройки времени - /set_schedule \n2.Для просмотра ряда задач со временем - /view_schedule \n3.Для удаления задачи по времени - /delete_schedule \n4.Для изменения времени - /update_schedule ")
      

@dp.message(Command('set_schedule'))
async def set_schedule(message:types.Message):
    await message.answer('Введите время для задачи в формате ЧЧ:ММ')
    
@dp.message(F.text)    
async def save_time(message:types.Message):
    user_id = message.from_user.id            
    time = message.text
    cursor.execute("INSERT INTO schedules (user_id, time) VALUES (?, ?)", (user_id, time))            
    connect.commit()
async def send_reminder():   
        schedules = cursor.execute("SELECT user_id, time FROM schedules").fetchall()
        for user_id, time in schedules:        
            current_time = datetime.now().strftime("%H:%M")
        if current_time == time:            
             await bot.send_message(user_id, "Пора выполнить задачу!")

async def scheduler():
    aioschedule.every().minute.do(send_reminder)   
    while True:
        await aioschedule.run_pending()        
        await asyncio.sleep(1)
async def on_start():
    asyncio.run(scheduler()) 

@dp.message(Command("view_schedule"))
async def view_schedule(message:types.Message):  
    user_id = message.from_user.id
    schedules = cursor.execute("SELECT time FROM schedules WHERE user_id = ?", (user_id,)).fetchall()    
    if schedules:
        await message.answer(f"Ваше расписание:\n{schedules}")    
    else:
        await message.answer("Ваше расписание пусто.")

@dp.message(Command("delete_schedule"))
async def delete_schedule(message:types.Message):
    try:        
        time = message.get_args()
        user_id = message.from_user.id        
        cursor.execute("DELETE FROM schedules WHERE user_id = ? AND time = ?", (user_id, time))
        connect.commit()        
        await message.answer(f"Задача на {time} удалена.")
    except Exception as e:        
        await message.answer("Ошибка:", e)

@dp.message(Command("update_schedule"))
async def update_schedule(message:types.Message):    
    try:
        args = message.get_args()       
        old_time, new_time = args
        user_id = message.from_user.id
        cursor.execute("UPDATE schedules SET time = ? WHERE user_id = ? AND time = ?", (new_time, user_id, old_time))        
        connect.commit()
        await message.answer(f"Время уведомления изменено с {old_time} на {new_time}.")    
    except Exception as e:
        await message.answer("Ошибка:", e)
    async def main():
        await dp.start_polling(bot) 
        try:        
            asyncio.run(main())
        except KeyboardInterrupt:        
            print('Выход')