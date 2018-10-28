#!/usr/bin/env python3
import telebot
from telebot import types
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


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling(timeout=60)
