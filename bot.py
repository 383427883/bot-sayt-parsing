from telebot import TeleBot
from key import g_m_m,laptop,buy_laptops
from pers import product_data
import os

token = os.environ.get('TOKEN')
bot = TeleBot(token)

@bot.message_handler(['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    send = f'salom!\n hurmatli:{first_name}'
    contact = bot.send_message(chat_id,send,reply_markup=g_m_m())
    bot.register_next_step_handler(contact,reg)

def reg(message):
    chat_id = message.chat.id
    p_n = message.contact.phone_number
    bot.send_message(chat_id,f"siz {p_n} orqali ro'yxatdan o'tdingiz!", reply_markup=laptop())
    bot.register_next_step_handler(message,lap)


def lap(message):
    chat_id = message.chat.id
    if message.text == 'Laptops':
        for product in product_data:
            p_i = product["noutbuk_rasmi"]
            p_n = product["noutbuk_nomi"]
            p_p = product["noutbuk_narxi"]
            p_k = product["noutbuk_oy"]
            laptop_data = f"Noutbuk nomi:  {p_n}\n\nNoutbuk narxi: {p_p}\n\nMudatli to'lov: {p_k}"
            bot.send_photo(chat_id,p_i,caption=laptop_data, reply_markup=buy_laptops())







while True:
    try:
        print('bot run!')
        bot.polling()
    except:
        print("error!")
        bot.stop_polling()