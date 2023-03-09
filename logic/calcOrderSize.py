from helpers.getTickerPairPrice import getTickerPairPrice

def calcOrderSize(client, nonce, buyTicker, sellTicker, buyAmmount):
    
    tickerPrice = getTickerPairPrice(client, nonce, buyTicker, sellTicker)

    return buyAmmount / float(tickerPrice)
