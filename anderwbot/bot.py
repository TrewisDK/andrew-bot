from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards.mainboard import mainboard
from keyboards.sizeboard import sizeboard
from keyboards.adminboard import adminboard
from database.database import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from states.ads_states import NewClothes, NewShoes
from random import randint

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Приветсвуем в боте!\n\nЧто хотите купить?", reply_markup=mainboard)
    user(message.from_user.id)


@dp.message_handler(commands=['admin'])
async def process_help_command(message: types.Message):
    if is_admin(message.from_user.id):
        await bot.send_message(message.from_user.id, "Добро пожаловать в админпанель", reply_markup=adminboard)
    else:
        await bot.send_message(message.from_user.id, "Извините, вы не админ")


@dp.message_handler(commands=['getid'])
async def get_id(message: types.Message):
    print(message.from_user.id)


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == '👕 Одежда 👕':
        await bot.send_message(msg.from_user.id, "Отлично!\n\nТеперь определимся с размером: ", reply_markup=sizeboard)
        update_type(1, msg.from_user.id)
    elif msg.text == '👟 Обувь 👟':
        await bot.send_message(msg.from_user.id, "Отлично!\n\nТеперь определимся с размером: ", reply_markup=sizeboard)
        update_type(2, msg.from_user.id)
    elif msg.text == 'XS':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == 'S':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == 'L':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == 'M':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == 'XL':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == 'XXL':
        update_size(msg.text, msg.from_user.id)
        data = get_user_data(msg.from_user.id)
        if data[0] == 1:
            ads = show_ads_clothes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
        else:
            ads = show_ads_shoes(data[1])
            for ad in ads:
                photo = open(ad[4], 'rb')
                await bot.send_photo(msg.from_user.id, photo,
                                     caption=f"{ad[0]}\n\n{ad[2]}\n\nРазмер: {ad[1]}\n\nДля покупки: {ad[3]}")
    elif msg.text == "🔙 Назад":
        await bot.send_message(msg.from_user.id, "Вернемся к выбору категории", reply_markup=mainboard)
    elif msg.text == "🔙 Выход":
        await bot.send_message(msg.from_user.id, "Выход из админпанели", reply_markup=mainboard)
    elif msg.text == '👕 Новое объявление Одежда 👕':
        if is_admin(msg.from_user.id):
            await bot.send_message(msg.from_user.id, "Введите название товара")
            await NewClothes.get_title.set()
        else:
            await bot.send_message(msg.from_user.id, "Извините, вы не админ")
    elif msg.text == '👟 Новое объявление Обувь 👟':
        if is_admin(msg.from_user.id):
            await bot.send_message(msg.from_user.id, "Введите название товара")
            await NewShoes.get_title.set()
        else:
            await bot.send_message(msg.from_user.id, "Извините, вы не админ")


@dp.message_handler(state=NewClothes.get_title)
async def title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await bot.send_message(message.from_user.id, "Добавьте описание товара")
    await NewClothes.next()


@dp.message_handler(state=NewClothes.get_description)
async def description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await bot.send_message(message.from_user.id, "Введите контакты для связи")
    await NewClothes.next()


@dp.message_handler(state=NewClothes.get_contacts)
async def contacts(message: types.Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await bot.send_message(message.from_user.id, "Укажите размер")
    await NewClothes.next()


@dp.message_handler(state=NewClothes.get_size)
async def size(message: types.Message, state: FSMContext):
    await state.update_data(size=message.text)
    await bot.send_message(message.from_user.id, "Отправьте фотографию товара (jpg формат)")
    await NewClothes.next()


@dp.message_handler(state=NewClothes.get_image, content_types=['photo'])
async def image(message: types.Message, state: FSMContext):
    photo_name = randint(1, 99999999999999)
    await message.photo[-1].download(f'images/{photo_name}.jpg')
    data = await state.get_data()
    await state.finish()
    new_clothes(data['title'], data['size'], data['description'], data['contacts'], f'images/{photo_name}.jpg')
    await bot.send_message(message.from_user.id, "Объявление успешно создано")


@dp.message_handler(state=NewShoes.get_title)
async def title2(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await bot.send_message(message.from_user.id, "Добавьте описание товара")
    await NewShoes.next()


@dp.message_handler(state=NewShoes.get_description)
async def description2(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await bot.send_message(message.from_user.id, "Введите контакты для связи")
    await NewShoes.next()


@dp.message_handler(state=NewShoes.get_contacts)
async def contacts2(message: types.Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await bot.send_message(message.from_user.id, "Укажите размер")
    await NewShoes.next()


@dp.message_handler(state=NewShoes.get_size)
async def size2(message: types.Message, state: FSMContext):
    await state.update_data(size=message.text)
    await bot.send_message(message.from_user.id, "Отправьте фотографию товара (jpg формат)")
    await NewShoes.next()


@dp.message_handler(state=NewShoes.get_image, content_types=['photo'])
async def image2(message: types.Message, state: FSMContext):
    photo_name = randint(1, 99999999999999)
    await message.photo[-1].download(f'images/{photo_name}.jpg')
    data = await state.get_data()
    await state.finish()
    new_shoes(data['title'], data['size'], data['description'], data['contacts'], f'images/{photo_name}.jpg')
    await bot.send_message(message.from_user.id, "Объявление успешно создано")


if __name__ == '__main__':
    executor.start_polling(dp)
