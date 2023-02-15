from classes.kraken import KrakenClient
from classes.asset import Asset
from helpers.getNonce import getNonce
from helpers.getBalances import getBalances
from helpers.getAssets import getAssets
from helpers.setAssets import setAssets
from helpers.getOrder import getOrder
from logic.calcOrderSize import calcOrderSize

if __name__ == "__main__":

    client = KrakenClient()

    balances = getBalances(client, getNonce())

    # kraken_assets = getAssets(client, getNonce(), balances)

    # assets = setAssets(kraken_assets)

    # for asset in assets:
    #     print(asset.__str__())

    # print(balances)
    print(calcOrderSize(client, getNonce(), 'ETH', 'USD', .50));