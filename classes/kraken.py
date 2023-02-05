import os
import requests
import urllib.parse
import hashlib
import hmac
import base64
from dotenv import load_dotenv

class KrakenClient: 
    def __init__(self) -> None:
        # Read Kraken API key and secret stored in environment variables
        load_dotenv()
        self._api__url = "https://api.kraken.com"
        self._api__key = os.getenv('API_KEY_KRAKEN')
        self._api__secret = os.getenv('API_SECRET_KRAKEN')

    def get_kraken_signature(self, urlpath, data) -> bytes:

        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self._api__secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    # Attaches auth headers and returns results of a POST request
    def kraken_request(self, uri_path, data):
        headers = {}
        headers['API-Key'] = self._api__key
        # get_kraken_signature() as defined in the 'Authentication' section
        headers['API-Sign'] = self.get_kraken_signature(uri_path, data)             
        req = requests.post((self._api__url + uri_path), headers=headers, data=data)
        return req