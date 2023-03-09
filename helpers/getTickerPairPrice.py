def getTickerPairPrice(client, nonce, buyTicker, sellTicker):    
    uri_path = '/0/public/Ticker?pair=' + buyTicker + sellTicker
    response = client._get(uri_path, nonce)
    tickerPair = next(iter(response))
    price = response[tickerPair]['c'][0]
    return price