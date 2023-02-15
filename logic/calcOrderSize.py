def calcOrderSize(client, nonce, buyTicker, sellTicker, buyAmmount):
    uri_path = '/0/public/AssetPairs?pair=' + buyTicker + sellTicker
    price = client._get(uri_path, nonce)
    return price
    #return buyAmmount / price
