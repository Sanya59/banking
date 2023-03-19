from decimal import Decimal
from model_db import *
from data import *
import telebot
from telebot import types

bot = telebot.TeleBot(token)


def registration(message, action):
    if action == 'fio_register':
        fio = message.text
        print(fio)
    elif action == 'data_register':
        data = message.text
        print(fio, data)


@bot.message_handler(commands=['start'])
def start_message(message):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="Войти", callback_data="login"))
    kb.add(types.InlineKeyboardButton(text="Зарегистрироватьсяти", callback_data="reg"))
    bot.send_message(message.chat.id, first_greeting, reply_markup=kb)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "login":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Введите вашу серию и номер паспорта:")
        elif call.data == 'reg':
            sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Введите ваше ФИО через пробел (например, Иванов Иван Иванович):")
            bot.register_next_step_handler(sent, registration(message=call.message, action='fio_register'))

            sent2 = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Введите вашу дату рождения в формате ДД.ММ.ГГГГ (например, 01.01.1970):")
            bot.register_next_step_handler(sent2, registration(message=call.message, action='data_register'))




bot.infinity_polling()
