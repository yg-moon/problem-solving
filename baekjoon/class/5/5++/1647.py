# 도시 분할 계획
from collections import defaultdict

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

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


total_cost = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        last = cost

print(total_cost - last)

"""
- 난이도: 골드4
- 분류: MST

- 핵심: 그래프를 MST 2개로 분할하는 방법은, 크루스칼 적용 이후 (비용이 가장 큰) 마지막 엣지를 제거하는 것.
"""
