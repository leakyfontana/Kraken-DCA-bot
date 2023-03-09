import os

def calcPurchaseDistribution(): 
    purchaseValues = os.getenv("BUY").split(' ')

    if purchaseValues.__len__() % 2 != 0:

        raise Exception('Purchase input formatted incorrectly: Value missing')
    
    order = { }
    totalPercent = 0
    for idx, x in enumerate(purchaseValues):

        if idx % 2 == 0 and x.isdigit():            
            raise Exception(f'Purchase input formatted incorrectly: Index {idx} should be a coin ticker')

        if idx % 2 == 1:

            if x.isdigit():
                percent = int(x)

                totalPercent += percent
                if totalPercent > 100:
                    raise Exception(f'Purchase input formatted incorrectly: Dsitribution is more than 100%')

                order[purchaseValues[idx - 1]] = percent

            else:
                raise Exception(f'Purchase input formatted incorrectly: Index {idx} should be a distribution percentage (1 - 100)')

    return order