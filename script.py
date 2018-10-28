#!/usr/bin/env python3
import telebot
from telebot.types import Message

TOKEN = '723184454:AAFuL24x7eKP86ht425-OPNTl5VArXm0hWA'

bot = telebot.TeleBot(TOKEN)

USER = set()


@bot.message_handler(commands=['start'])
def send_start(message: Message):
    bot.reply_to(message, "This is test bot.")


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    bot.send_message(message.chat.id, "Try to figure out by yourself!")


@bot.edited_message_handler(content_types=['text'], func=lambda message: True)
@bot.message_handler(content_types=['text'], func=lambda message: True)
def reply_message(message: Message):
    if message.from_user.id not in USER:
        bot.send_message(message.chat.id, 'Hi, this is your first message! How are you?')
        USER.add(message.from_user.id)
    else:
        bot.send_message(message.chat.id, 'What has changed since the previous time?')


bot.polling(timeout=60)
