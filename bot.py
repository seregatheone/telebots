import telebot
import config
import random
import pogoda
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    bot.send_message(message.chat.id,"Это мой первый бот)))")
@bot.message_handler(content_types=['text'])
def lalala(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Vizinga")
    item2 = types.KeyboardButton("Drugoe mesto")
    item3 = types.KeyboardButton("Syktyvkar")
    markup.add(item1, item2,item3)
    reply_markup=markup
    if message.chat.type == 'private':
        if message.text == 'Vizinga':
            bot.send_message(message.chat.id, pogoda.pogoda("Vizinga"))
        elif message.text == 'Drugoe mesto':
            bot.send_message(message.chat.id, 'Enter this place')
        elif message.text == 'Syktyvkar':
            bot.send_message(message.chat.id, pogoda.pogoda("Syktyvkar"))
        elif isinstance(message.text,(str,int)):
            try:
                bot.send_message(message.chat.id, pogoda.pogoda(message.text))
            except :
                bot.send_message(message.chat.id, "Vvedite gorod")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


bot.polling(none_stop=True)
