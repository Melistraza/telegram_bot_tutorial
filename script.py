#!/usr/bin/env python3
import telebot
from telebot.types import Message

TOKEN = 'your_token'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message: Message):
    bot.reply_to(message, "This is test bot.")


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    bot.send_message(message.chat.id, "Try to figure out by yourself!")


@bot.edited_message_handler(content_types=['text'], func=lambda message: True)
@bot.message_handler(content_types=['text'], func=lambda message: True)
def reply_message(message: Message):
    bot.reply_to(message, 'Bot response: {}'.format(message.text))


bot.polling()
