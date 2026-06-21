def minContainers(weights, capacity):
    containers = 1
    current = 0

    for w in weights:
        if current + w <= capacity:
            current += w
        else:
            containers += 1
            current = w

    return containers

weights = [5,10,15,20,25,30,35]
capacity = 50

print(minContainers(weights, capacity))