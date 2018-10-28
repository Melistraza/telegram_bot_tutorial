#!/usr/bin/env python3
import telebot

TOKEN = 'your_token'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def reply_message(message):
    bot.reply_to(message, message.text)


bot.polling()
