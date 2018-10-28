#!/usr/bin/env python3
import telebot

bot = telebot.TeleBot('your_token')


@bot.message_handler(content_types=['text'])
def reply_message(message):
    bot.reply_to(message, message.text)


bot.polling()
