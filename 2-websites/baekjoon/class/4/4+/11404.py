# 플로이드
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 그래프는 INF로 채운 2차원 배열로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)  # 주의: 최소 간선만 남기기

# 자기자신으로 가는 거리는 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
    print()

"""
- 난이도: 골드4
- 분류: 플로이드-워셜
"""
