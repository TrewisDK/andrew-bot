from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

xs_kb = KeyboardButton("XS")
s_kb = KeyboardButton("S")
m_kb = KeyboardButton("M")
l_kb = KeyboardButton("L")
xl_kb = KeyboardButton("XL")
xxl_kb = KeyboardButton("XXL")
back_kb = KeyboardButton("🔙 Назад")


sizeboard = ReplyKeyboardMarkup(resize_keyboard=True)
sizeboard.row(xs_kb, s_kb, m_kb).row(l_kb, xl_kb, xxl_kb).row(back_kb)
