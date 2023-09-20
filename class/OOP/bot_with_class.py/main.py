import logging

from sql import Work_Database

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5939110451:AAHd3BnHchgsazL-111kod9Yab_gKCWoBUY'

data = Work_Database("ombor.db")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    data.create_table()
    data.insert_users()
    await message.reply("Hi!")
    
@dp.message_handler(commands=['Update'])
async def send_welcome(message: types.Message):
    name = message.answer("Ismingiz: ")
    new_category = message.answer("Nimani ozgartirish: ")

    



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)