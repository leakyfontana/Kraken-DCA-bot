from classes.kraken import KrakenClient
from helpers.getNonce import getNonce
from logic.dollarCostAverage import dollarCostAverage
import json


def lambda_handler(event, context):

    try:
        client = KrakenClient()
        dollarCostAverage(client, getNonce())

        return {
            'statusCode': 200,
            'body': json.dumps('Succesful Dollar Cost Average!')
        }

    except:

        return {
            'statusCode': 500,
            'body': json.dumps('Unsuccesful Dollar Cost Average :(. Please check logs for more info.')
        }
