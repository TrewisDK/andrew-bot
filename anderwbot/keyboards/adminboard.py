from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

admin_clothes_kb = KeyboardButton('👕 Новое объявление Одежда 👕')
admin_shoes_kb = KeyboardButton('👟 Новое объявление Обувь 👟')
back_kb = KeyboardButton("🔙 Выход")

adminboard = ReplyKeyboardMarkup(resize_keyboard=True)
adminboard.add(admin_shoes_kb, admin_clothes_kb).row(back_kb)