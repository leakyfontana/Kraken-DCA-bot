def getBalances(client, nonce):
    return client._post('/0/private/Balance', nonce)