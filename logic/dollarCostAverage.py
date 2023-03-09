import os
from helpers.getBalances import getBalances
from .calcPurchaseDistribution import calcPurchaseDistribution
from .calcOrderSize import calcOrderSize
from helpers.getNonce import getNonce

def dollarCostAverage(client, nonce):
    balances = getBalances(client, nonce)

    purchaseDistribution = calcPurchaseDistribution()

    sellTicker = os.getenv("SELL")
    sellFunds = float(balances[sellTicker])

    sellAmount = float(os.getenv("AMOUNT"))
    if  sellFunds < sellAmount:
        diff = sellAmount - sellFunds
        raise Exception(f'Insufficient funds: Please deposit {diff} {sellTicker}')
    
    distBuyAmount = sellAmount / len(purchaseDistribution)
    for key in purchaseDistribution:
        orderSize = calcOrderSize(client, nonce, key, sellTicker, distBuyAmount)

        print(f'purchasing {orderSize} {key}')
        print(key + sellTicker)

        assetPairInfo = client._get ('/0/public/AssetPairs?pair=' + key + sellTicker, getNonce())
        assetPairMin = assetPairInfo[key + sellTicker]['ordermin']

        if  assetPairMin > orderSize:
            raise Exception(f'Less than Order Min for {key + sellTicker}: Please increase {key} distribution % or {sellTicker} amount')

        response = client._post('/0/private/AddOrder', {
            "nonce": getNonce(),
            "ordertype": "market",
            "type": "buy",
            "volume": float(orderSize),
            "pair": f'{key + sellTicker}',        
        })

        print(response)