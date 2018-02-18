#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.

# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import os
from onliner_moto_fetcher import fetch
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

keyboard = [[InlineKeyboardButton("Gime the latest motocycles", callback_data='1')]]
reply_markup = InlineKeyboardMarkup(keyboard)

def start(bot, update):
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    onliner_data = fetch()
    if not len(onliner_data):
        bot.send_message(chat_id=query.message.chat_id, text="Very bad news: we did not find any " +
                                                                        "motorcycle that responds your intrests :(")
    else:
        for _, _, link in onliner_data:
            bot.send_message(chat_id=query.message.chat_id, text=link)

    bot.send_message(chat_id=query.message.chat_id, text='Please choose:', reply_markup=reply_markup)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    token = os.environ['TELEGRAM_TOKEN']
    if not token:
        raise ValueError('Invalid telegram token - missing env var TELEGRAM_TOKEN.')
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
