from config import bitvavo_token_secret, bitvavo_token
from python_bitvavo_api.bitvavo import Bitvavo

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret
})


def balance(update, context):
    ticker_prices = bitvavo.tickerPrice({})
    response = bitvavo.balance({})
    total = 0
    for item in response:
        asset = item.get("symbol")
        if asset == "EUR":
            total += int(item.get("available"))

        else:
            ticker = asset + "-EUR"
            for market in ticker_prices:
                if market.get("market") == ticker:
                    total += float(market.get("price")) * float(item.get("available"))

    total = str(round(total, 2))
    update.message.reply_text("Your total balance is €" + total)
