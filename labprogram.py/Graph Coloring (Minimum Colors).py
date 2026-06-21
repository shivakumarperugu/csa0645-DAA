def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n

    def safe(v, c):
        for i in range(n):
            if graph[v][i] == 1 and colors[i] == c:
                return False
        return True

    def solve(v):
        if v == n:
            return True

        for c in range(1, m + 1):
            if safe(v, c):
                colors[v] = c

                if solve(v + 1):
                    return True

                colors[v] = 0

        return False

    return colors if solve(0) else None

graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

print(graph_coloring(graph,3))