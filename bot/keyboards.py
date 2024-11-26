from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests

flags = requests.get ('http://127.0.0.1:8000/api/flags/').json()

flags_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

btns = []

for flag in flags:
    btns.append(KeyboardButton(text = flag['country_name']))