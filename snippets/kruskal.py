from collections import defaultdict

V, E = map(int, input().split())

parent = defaultdict(int)
for i in range(1, V + 1):
    parent[i] = i


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
total_cost = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 MST에 포함 (union)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost

print(total_cost)
