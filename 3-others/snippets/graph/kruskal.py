# BOJ 1197
V, E = map(int, input().split())
parent = list(range(V + 1))
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()  # 핵심: 간선을 비용순으로 정렬


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total_cost = 0

for cost, a, b in edges:  # 모든 간선을 확인하며
    if find(a) != find(b):  # 사이클이 발생하지 않는 경우에만 MST에 포함 (union)
        union(a, b)
        total_cost += cost

print(total_cost)
