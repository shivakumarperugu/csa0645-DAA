def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0] * n for _ in range(n)]

    # Cost for single key
    for i in range(n):
        cost[i][i] = freq[i]

    # Length of chain
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            freq_sum = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                total = left + right + freq_sum

                cost[i][j] = min(cost[i][j], total)

    return cost[0][n - 1]

# Sample Input
keys = [10, 12, 20]
freq = [34, 8, 50]

print("Minimum Cost =", optimal_bst(keys, freq))