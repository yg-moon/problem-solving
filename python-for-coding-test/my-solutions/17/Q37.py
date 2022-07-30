# BOJ 11404
from collections import defaultdict

INF = int(1e9)

N = int(input())
M = int(input())

# 그래프 초기화
# - 자기 자신에게로 가는 비용은 0
# - 나머지는 INF
graph = defaultdict(dict)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = INF

# 각 간선에 대한 값을 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    # 조건: “시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.”
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        result = graph[i][j]
        # 주의: 갈 수 없는 경우에는 0을 출력
        if result == INF:
            result = 0
        if j != N:
            print(result, end=" ")
        else:
            print(result)
