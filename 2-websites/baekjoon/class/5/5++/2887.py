# 행성터널
from collections import defaultdict


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


N = int(input())

parent = defaultdict(int)
for i in range(1, N + 1):
    parent[i] = i


# 모든 행성의 x,y,z 값을 따로 저장하고 각각 정렬한다.
x = []
y = []
z = []
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    # (좌표값, 행성번호)
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

# 각 축마다 인접한 값들로 만들어지는 간선만 고려한다.
edges = []
for i in range(N - 1):
    # (cost, a, b)
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 크루스칼
edges.sort()
answer = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)

"""
- 난이도: 플래5
- 분류: MST, 정렬

핵심
- 크루스칼에서 고려할 간선의 개수를 줄인다.
- 원리: 문제 조건에 의해 각 좌표값 차이의 최소치만 고려대상이므로,
       정렬 이후 인접한 값들끼리의 차이만이 가능한 후보가 된다.
"""
