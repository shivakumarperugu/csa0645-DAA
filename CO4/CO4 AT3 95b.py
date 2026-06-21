def prim(graph, n):
    selected = [False] * n
    selected[0] = True

    print("Edge : Weight")

    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True


# Sample Input
graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 3],
    [4, 1, 0, 5],
    [0, 3, 5, 0]
]

prim(graph, 4)