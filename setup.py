#!/usr/bin/env python3
import telebot
from telebot import types
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


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Like", callback_data="data"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Inline message"),
        reply_markup=keyboard
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


bot.polling(timeout=60)
