from collections import defaultdict

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

parent = defaultdict(int)
for i in range(1, N + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 크루스칼
edges.sort()
total_cost = 0
mst_cost = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst_cost += cost
    total_cost += cost

print(total_cost - mst_cost)
