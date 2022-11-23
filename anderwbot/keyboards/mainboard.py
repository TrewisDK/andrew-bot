from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

clothes_kb = KeyboardButton('👕 Одежда 👕')
shoes_kb = KeyboardButton('👟 Обувь 👟')

mainboard = ReplyKeyboardMarkup(resize_keyboard=True)
mainboard.add(clothes_kb, shoes_kb)