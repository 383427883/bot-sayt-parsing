from telebot import types

def g_m_m():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Share contact",request_contact=True)
    keyboard.row(btn)
    return keyboard

def laptop():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Laptops")
    keyboard.row(btn)
    return keyboard

def buy_laptops():
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Batafsil:', url='https://alifshop.uz/ru/categories/vse-noutbuki?gad_source=1&gclid=EAIaIQobChMIlNqZh6_GhQMVb0ZBAh0F5AsOEAAYASAAEgKK8PD_BwE')
    keyboard.row(btn)
    return keyboard