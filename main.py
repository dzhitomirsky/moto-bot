#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.

# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import os
from onliner_moto_fetcher import fetch
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, RegexHandler
from models import model_queries
model_names = model_queries.keys()[::-1]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

keyboard = [
    [model_names[0]],
    [model_names[1], model_names[2]],
    [model_names[3], model_names[4]]
]
reply_markup = ReplyKeyboardMarkup(keyboard)

def start(bot, update):
    update.message.reply_text('Wroom! Wroom! It is oliner-moto-bot!', reply_markup=reply_markup)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def get_search_callback(model_name):
    def search(bot, update):
        """Echo the user message."""
        onliner_data = fetch(model_name)
        if not len(onliner_data):
            update.message.reply_text("Very bad news: we did not find any motorcycle that responds your intrests :(")
        else:
            for _, _, link in onliner_data:
                update.message.reply_text(link)
    return search


def main():
    token = os.environ['TELEGRAM_TOKEN']
    if not token:
        raise ValueError('Invalid telegram token - missing env var TELEGRAM_TOKEN.')
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    for m_name in model_queries.keys():
        updater.dispatcher.add_handler(RegexHandler(pattern=m_name, callback=get_search_callback(m_name)))

    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
