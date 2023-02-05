import os
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

class KrakenClient: 
    def __init__(self) -> None:
        # Read Kraken API key and secret stored in environment variables
        self._api__url = "https://api.kraken.com"
        self._api__key = os.environ['API_KEY_KRAKEN']
        self._api__secret = os.environ['API_KEY_KRAKEN']

    def get_kraken_signature(self, urlpath, data):

        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['none']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self._api_secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    # Attaches auth headers and returns results of a POST request
    def kraken_request(self, uri_path, data, api_key):
        headers = {}
        headers['API-Key'] = api_key
        # get_kraken_signature() as defined in the 'Authentication' section
        headers['API-Sign'] = get_kraken_signature(self, uri_path, data)             
        req = requests.post((self._api__url + uri_path), headers=headers, data=data)
        return req