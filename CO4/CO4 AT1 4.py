INF = float('inf')

def floyd_warshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print("Shortest Distance Matrix:")
    for row in dist:
        for val in row:
            if val == INF:
                print("INF", end=" ")
            else:
                print(val, end=" ")
        print()

# Sample Input
n = 3
graph = [
    [0, 5, INF],
    [2, 0, 3],
    [INF, INF, 0]
]

floyd_warshall(graph, n)