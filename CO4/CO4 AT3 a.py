class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax edges V-1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative cycles
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return

        print("Vertex\tDistance from Source")
        for i in range(self.V):
            print(i, "\t", dist[i])


# Sample Input
g = Graph(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 2, 7)
g.add_edge(1, 2, 8)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, -4)
g.add_edge(2, 3, -3)
g.add_edge(2, 4, 9)
g.add_edge(3, 1, -2)
g.add_edge(4, 0, 2)
g.add_edge(4, 3, 7)

g.bellman_ford(0)