from decimal import Decimal
from model_db import *
from data import *
import telebot


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Войти")
    item2 = telebot.types.KeyboardButton("Зарегистрироваться")
    bot.send_message(message.chat.id, first_greeting)
    markup.add(item1)
    markup.add(item2)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Войти":
        bot.send_message(message.chat.id, "здест типа вход")
    elif message.text == 'Зарегистрироваться':
        bot.send_message(message.chat.id, "здест типа регистрация")


bot.infinity_polling()
