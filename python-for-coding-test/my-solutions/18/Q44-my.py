# BOJ 2887
# 실패. (메모리 초과)
from collections import defaultdict

N = int(input())

planets = []
for _ in range(N):
    planets.append(list(map(int, input().split())))

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


# 행성 사이의 모든 터널을 구함
edges = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        a = planets[i - 1]
        b = planets[j - 1]
        cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
        edges.append((cost, i, j))
edges.sort()

# 크루스칼
answer = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)
