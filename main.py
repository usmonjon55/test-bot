import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from button import *

API_TOKEN = '6126061222:AAGoX2vmBQZVPi1T_Dx6YYI203r2WeQTMgY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Salom zakaz qilish uchun biror tugmani bosing", reply_markup=bosh_menu_inline_keyboard)

@dp.callback_query_handler(text="1")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://cdn.punchng.com/wp-content/uploads/2017/03/29201341/soft-drinks.png", reply_markup=Ichimliklar_inline_keyboard)

@dp.callback_query_handler(text="2")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20lavash.jpg", reply_markup=Lavashlar_inline_keyboard)

@dp.callback_query_handler(text="3")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://media.express24.uz/r/:w/:h/ivb3TFYWWrHDo1XKzuT57.jpg", reply_markup=Burgerlar_inline_keyboard)

@dp.callback_query_handler(text="4")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Pizza-3007395.jpg/800px-Pizza-3007395.jpg", reply_markup=Pizzalar_inline_keyboard)

















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)