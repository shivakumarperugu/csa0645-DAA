def maxCoins(piles):
    piles.sort()
    ans = 0
    left, right = 0, len(piles) - 1

    while left < right:
        right -= 1
        ans += piles[right]
        right -= 1
        left += 1

    return ans

piles = [2,4,1,2,7,8]
print(maxCoins(piles))