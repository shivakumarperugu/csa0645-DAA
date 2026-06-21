def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        visited[u] = True

        for v in range(n):
            if graph[u][v] != float('inf'):
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist

INF = float('inf')

graph = [
    [0,10,3,INF,INF],
    [INF,0,1,2,INF],
    [INF,4,0,8,2],
    [INF,INF,INF,0,7],
    [INF,INF,INF,9,0]
]

print(dijkstra(graph,0))