def minimumAddedCoins(coins, target):
    coins.sort()
    reach = 0
    i = 0
    added = 0

    while reach < target:
        if i < len(coins) and coins[i] <= reach + 1:
            reach += coins[i]
            i += 1
        else:
            reach += reach + 1
            added += 1

    return added

coins = [1,4,10]
target = 19
print(minimumAddedCoins(coins, target))