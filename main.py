from classes.kraken import KrakenClient
from classes.asset import Asset
from helpers.getNonce import getNonce

def setAssets():
    client = KrakenClient()

    balances = client._post('/0/private/Balance', getNonce())

    print(balances)

    asset_query = "?asset="
    for idx, asset in enumerate(balances):
        if (idx != 0):
            asset_query += ','

        asset_query += asset

    uri_path = '/0/public/Assets' + asset_query
    asset_response = client._get(uri_path, getNonce())

    assets = {}
    for asset in asset_response:
        temp_asset = Asset(asset_response[asset])
        assets[temp_asset.altname] = temp_asset
    
    return assets


if __name__ == "__main__":

    print(setAssets())