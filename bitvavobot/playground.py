from config import bitvavo_token, bitvavo_token_secret
from python_bitvavo_api.bitvavo import Bitvavo

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})

# possible_tokens = {}
#
# for token in bitvavo.assets({}):
#     sym = token.get("symbol")
#     name = token.get("name")
#
#     possible_tokens[sym] = name
#
# print(possible_tokens)

print(bitvavo.tickerPrice({}))