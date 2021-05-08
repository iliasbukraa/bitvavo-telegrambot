from config import bitvavo_token, bitvavo_token_secret
from python_bitvavo_api.bitvavo import Bitvavo

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret,
})

response = bitvavo.tickerPrice({})
possible_tickers = [d["market"] for d in response]

print(response)
# possible_tokens = {}
#
# for token in bitvavo.assets({}):
#     sym = token.get("symbol")
#     name = token.get("name")
#
#     possible_tokens[sym] = name
#
# print(possible_tokens)

# print(bitvavo.tickerPrice({}))
# possible_tokens={}
# for token in bitvavo.assets({}):
#     possible_tokens[token.get("symbol")] = token.get("name")
#
# print(possible_tokens)


# response = bitvavo.account()
# print(response)
