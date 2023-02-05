import os
import time
import requests
from classes.kraken import KrakenClient

def getAccountBalance():
    # Construct the request and print the result
    resp = KrakenClient().kraken_request('/0/private/Balance', {
        "nonce": str(int(1000*time.time()))
    })
    return resp.json()


if __name__ == "__main__":
    print(getAccountBalance())