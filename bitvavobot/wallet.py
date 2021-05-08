from config import bitvavo_token_secret, bitvavo_token
from python_bitvavo_api.bitvavo import Bitvavo

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret
})


def wallet(update, message):
    response = bitvavo.balance({})
    for asset in response:
        update.message.reply_text(asset["symbol"]+" : "+asset["available"])