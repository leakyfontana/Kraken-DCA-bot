from classes.kraken import KrakenClient
from helpers.getNonce import getNonce
from logic.dollarCostAverage import dollarCostAverage
import json

def lambda_handler(event, context):

    client = KrakenClient()
    dollarCostAverage(client, getNonce())

    return {
        'statusCode': 200,
        'body': json.dumps('Succesful Dollar Cost Average!')
    }