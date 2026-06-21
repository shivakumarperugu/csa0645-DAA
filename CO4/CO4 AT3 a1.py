def warshall(graph, n):
    reach = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    print("Reachability Matrix:")
    for row in reach:
        print(*row)


# Sample Input
graph = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

warshall(graph, 3)