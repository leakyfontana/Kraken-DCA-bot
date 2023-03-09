from classes.kraken import KrakenClient
from helpers.getNonce import getNonce
from logic.dollarCostAverage import dollarCostAverage

if __name__ == "__main__":

    client = KrakenClient()
    dollarCostAverage(client, getNonce())