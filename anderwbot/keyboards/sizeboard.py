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

size_365 = KeyboardButton("36.5")
size_37 = KeyboardButton("37")
size_38 = KeyboardButton("38")
size_385 = KeyboardButton("38.5")
size_39 = KeyboardButton("39")
size_40 = KeyboardButton("40")
size_405 = KeyboardButton("40.5")
size_41 = KeyboardButton("41")
size_42 = KeyboardButton("42")
size_425 = KeyboardButton("42.5")
size_43 = KeyboardButton("43")
size_44 = KeyboardButton("44")
size_445 = KeyboardButton("44.5")
size_45 = KeyboardButton("45")
size_46 = KeyboardButton("46")
size_465 = KeyboardButton("46.5")
size_47 = KeyboardButton("47")
size_48 = KeyboardButton("48")

sizeboard_cloath = ReplyKeyboardMarkup(resize_keyboard=True)
sizeboard_cloath.row(xs_kb, s_kb, m_kb).row(l_kb, xl_kb, xxl_kb).row(back_kb)

sizeboard_shoez = ReplyKeyboardMarkup(resize_keyboard=True)
sizeboard_shoez.row(size_365, size_37, size_38, size_385, size_39, size_40).row(size_405, size_41, size_42, size_425,
                                                                                size_43, size_44).row(size_445, size_45,
                                                                                                      size_46, size_465,
                                                                                                      size_47, size_48).row(back_kb)
