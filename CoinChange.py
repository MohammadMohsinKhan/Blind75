
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if (amount == 0):
        return amount
    count = 0
    coins.sort()
    while amount > 0:
        flag = True
        if (amount in coins):
            count += 1
            return count
        elif (amount >= max(coins)):
            amount = amount - max(coins)
            count += 1
        else:
            for coin in reversed(coins):
                if (amount >= coin):
                    flag = False
                    amount -= coin
                    count += 1
                    break
            if (flag):
                return -1
        
    return -1
            
print(coinChange([186,419,83,408],6249))