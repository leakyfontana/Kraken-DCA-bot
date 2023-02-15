import time

def getNonce():
    return {"nonce": str(int(1000*time.time()))}
