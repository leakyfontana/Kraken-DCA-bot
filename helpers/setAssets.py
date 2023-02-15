from classes.asset import Asset

def setAssets(kraken_assets):
    assets = {}
    for asset in kraken_assets:
        temp_asset = Asset(kraken_assets[asset])
        assets[temp_asset.altname] = temp_asset
    
    return assets