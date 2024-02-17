# BOJ 1647
# 출처: 이코테
import collections

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

parent = collections.defaultdict(int)
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


total_cost = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        last = cost

print(total_cost - last)
