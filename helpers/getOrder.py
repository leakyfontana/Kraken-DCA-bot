import os
from dotenv import load_dotenv

def getOrder():
    load_dotenv()
    buyValues = os.getenv("BUY").split(' ')

    if buyValues.__len__() % 2 != 0:
        raise Exception('Buy input formatted incorrectly: Value missing')
    
    order = { }

    totalPercent = 0
    for idx, x in enumerate(buyValues):

        if idx % 2 == 0 and x.isdigit():            
            raise Exception(f'Buy input formatted incorrectly: Index {idx} should be a coin ticker')

        if idx % 2 == 1:

            if x.isdigit():
                percent = int(x)

                totalPercent += percent
                if totalPercent > 100:
                    raise Exception(f'Purchase input formatted incorrectly: Distribution is more than 100%')

                order[buyValues[idx - 1]] = percent

            else:
                raise Exception(f'Buy input formatted incorrectly: Index {idx} should be a distribution percentage (1 - 100)')

    return order