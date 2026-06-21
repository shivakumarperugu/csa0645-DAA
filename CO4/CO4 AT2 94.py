from collections import deque

class WaterAllocation:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def bfs(self, source, sink, parent):
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def max_flow(self, source, sink):
        parent = [-1] * self.n
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink

            while s != source:
                path_flow = min(path_flow,
                                self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Sample Water Network
graph = [
    [0, 10, 8, 0],  # Reservoir
    [0, 0, 5, 10],  # Zone 1
    [0, 0, 0, 10],  # Zone 2
    [0, 0, 0, 0]    # Demand Zone
]

wa = WaterAllocation(graph)
print("Maximum Water Allocation =", wa.max_flow(0, 3))