def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

    return True

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    mst = []
    weight = 0

    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            weight += w

    return mst, weight

n = 5

edges = [
    (0,1,1),
    (0,2,1),
    (1,3,2),
    (2,3,2),
    (3,4,3),
    (4,2,3)
]

mst, wt = kruskal(n, edges)

print("MST:", mst)
print("Total Weight:", wt)