def getAssets(client, nonce, balances):
    asset_query = "?asset="
    for idx, asset in enumerate(balances):
        if (idx != 0):
            asset_query += ','

        asset_query += asset

    uri_path = '/0/public/Assets' + asset_query
    return client._get(uri_path, nonce)