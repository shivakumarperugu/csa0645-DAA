import heapq

def shortestPath(n, edges, source, target):
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if u == target:
            return d

        for v, w in graph[u]:
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return -1

edges = [
    (0,1,7),(0,2,9),(0,5,14),
    (1,2,10),(1,3,15),(2,3,11),
    (2,5,2),(3,4,6),(4,5,9)
]

print(shortestPath(6, edges, 0, 4))