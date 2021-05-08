from telegram.ext import Updater, CommandHandler
import logging
from config import telegram_token
from balance import balance
from tickerprice import tickerprice
from symbols import symbols
from wallet import wallet

bot_token = telegram_token
bot_user_name = "bitvavo-telegrambot"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(bot_user_name)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    queue = updater.job_queue

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("balance", balance))
    dispatcher.add_handler(CommandHandler("tickerprice",tickerprice))
    dispatcher.add_handler(CommandHandler("symbols", symbols))
    dispatcher.add_handler(CommandHandler("wallet",wallet))

    # Start the Bot
    updater.start_polling()

    updater.idle()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
