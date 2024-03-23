# BOJ 11404
N = int(input())
M = int(input())

# INF로 초기화
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신은 0
for i in range(1, N + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 주의: k가 가장 위에 있어야 함
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print("%-5s" % "INF", end=" ")
        else:
            print("%-5d" % graph[i][j], end=" ")
    print()
