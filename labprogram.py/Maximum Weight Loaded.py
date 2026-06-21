def maxLoadedWeight(weights, capacity):
    weights.sort(reverse=True)

    total = 0

    for w in weights:
        if total + w <= capacity:
            total += w

    return total

weights = [10,20,30,40,50]
capacity = 60

print(maxLoadedWeight(weights, capacity))