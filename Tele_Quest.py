import requests
import json
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler

cur_scen = "Beginning.sc"


def iteration(bot, update):
    query = update.callback_query
    global cur_scen
    cur_scen = query.data
    with open(cur_scen, 'r') as event:
        description, choice = json.load(event)

        options = []
        for txt, result in choice.items():
            options.append([InlineKeyboardButton(txt, callback_data=result)])
        reply_markup = InlineKeyboardMarkup(options)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="-" * 15 + "\n" + description + '\n' + "-" * 15 + '\nЧто вы будете делать:',
                              reply_markup=reply_markup)
        # update.message.reply_text('Что вы будете делать:', reply_markup=reply_markup)


def start(bot, update):
    update.message.reply_text(
        'Привет {}\nНачнём наш квест\n'
            .format(update.message.from_user.first_name))
    with open(cur_scen, 'r') as event:
        description, choice = json.load(event)
        options = []
        for txt, result in choice.items():
            options.append([InlineKeyboardButton(txt, callback_data=result)])
        reply_markup = InlineKeyboardMarkup(options)
        update.message.reply_text("-" * 15 + "\n" + description + '\n' + "-" * 15 + '\nЧто вы будете делать:',
                                  reply_markup=reply_markup)
    return


def help(bot, update):
    update.message.reply_text(
        'Когда-нибудь здесь будет хелпа'
    )


def handle(bot, update):
    # print(update.message.reply_text(update.message.text))
    # menu_main = [[InlineKeyboardButton('Option 1', callback_data='m1')],
    #             [InlineKeyboardButton('Option 2', callback_data='m2')],
    #             [InlineKeyboardButton('Option 3', callback_data='m3')]]
    # reply_markup = InlineKeyboardMarkup(menu_main)
    # update.message.reply_text('Choose the option:', reply_markup=reply_markup)
    update.message.reply_text(update.message.text)
    return


def menu_actions(bot, update):
    query = update.callback_query
    msg = query.data
    if msg == "m1":
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="One")
    elif msg == "m2":
        update.message.reply_text("Two")
    elif msg == "m3":
        update.message.reply_text("Three")
    return


updater = Updater('589352191:AAHf7ep2TRq1MJxBVavy_BAAl-IvfsCdHaM')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle))
updater.dispatcher.add_handler(CallbackQueryHandler(iteration))
updater.start_polling()
updater.idle()
