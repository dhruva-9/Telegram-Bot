from telegram import *
from telegram.ext import *
import Responces as R

api_key = "1770974330:AAFOaTA3iXAlLwMT7OTUL1Ie_RRSwIyIrcA"

print("Bot Started...")


def start_command(update, context):
    update.message.reply_text("Type something random to get started")


def help_command(update, context):
    update.message.reply_text(
        "If you need help then you should ask for it on Goole!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    responce = R.sample_responces(text)

    update.message.reply_text(responce)


def main():
    updater=Updater(api_key, use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

main()
