from python_bitvavo_api.bitvavo import Bitvavo
from config import bitvavo_token, bitvavo_token_secret

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret
})

def symbols(update, context):
    response = bitvavo.tickerPrice({})
    for symbol in response:
        update.message.reply_text(symbol["market"])