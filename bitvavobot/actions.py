from config import bitvavo_token, bitvavo_token_secret
from python_bitvavo_api.bitvavo import Bitvavo
from bot import logger

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def balance(update, context):
    logger.info(update.message)
    response = bitvavo.account()
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.get("fees").get("volume"))


def asset(update, context):
    logger.info(update.message)
    response = bitvavo.assets({})
    for asset in response:
        sym_name = "{} - {}".format(asset.get("symbol"), asset.get("name"))
        context.bot.send_message(chat_id=update.effective_chat.id, text=sym_name)


def price(update, context):
    logger.info(update.message)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="What token would you like to get the current price of (symbol or name)?")


def get_price(update, context):
    logger.info(update.message)
    possible_tokens = {}

    for token in bitvavo.assets({}):
        possible_tokens[token.get("symbol")] = token.get("name")

    curr_price = bitvavo.tickerPrice({})

    if update.message.text in possible_tokens.keys():
        ticker = update.message.text
    elif update.message.text in possible_tokens.values():
        ticker = update.message.text + "-EUR"
    else:
        ticker = None

    if ticker:
        ticker_price = next((item for item in curr_price if item["market"] == ticker))
        context.bot.send_message(chat_id=update.effective_chat.id, text=ticker_price)
