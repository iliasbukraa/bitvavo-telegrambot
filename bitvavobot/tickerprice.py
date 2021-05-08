from python_bitvavo_api.bitvavo import Bitvavo
from config import bitvavo_token, bitvavo_token_secret

bitvavo = Bitvavo({
    'APIKEY': bitvavo_token,
    'APISECRET': bitvavo_token_secret
})


def tickerprice(update, context):
    tickers = context.args
    modded_tickers = []

    response = bitvavo.tickerPrice({})
    possible_tickers = [d["market"] for d in response]

    for ticker in tickers:
        if "-" not in ticker:
            m_t = str.upper(ticker) + "-EUR"
        else:
            m_t = str.upper(ticker)
        if m_t not in possible_tickers:
            update.message.reply_text(ticker + " is not a valid ticker symbol! Use the /symbols command to get a list "
                                               "of all allowed symbols.")
        else:
            modded_tickers.append(m_t)

    for wanted_price in modded_tickers:
        for market_ticker in response:
            if market_ticker["market"] == wanted_price:
                update.message.reply_text(wanted_price + " currently trades at €" + market_ticker["price"])
