def hamiltonian_cycle(graph):
    n = len(graph)
    path = [0]

    def safe(v, pos):
        if graph[path[pos-1]][v] == 0:
            return False

        if v in path:
            return False

        return True

    def solve(pos):
        if pos == n:
            return graph[path[-1]][path[0]] == 1

        for v in range(1, n):
            if safe(v, pos):
                path.append(v)

                if solve(pos + 1):
                    return True

                path.pop()

        return False

    return solve(1)

graph = [
 [0,1,1,1],
 [1,0,1,0],
 [1,1,0,1],
 [1,0,1,0]
]

print(hamiltonian_cycle(graph))