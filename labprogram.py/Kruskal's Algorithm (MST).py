def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    parent = list(range(n))
    rank = [0] * n

    mst = []
    total = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            total += w

    return mst, total

edges = [
    (0,1,10),
    (0,2,6),
    (0,3,5),
    (1,3,15),
    (2,3,4)
]

mst, total = kruskal(4, edges)

print(mst)
print(total)