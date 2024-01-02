INF = int(1e9)

N = int(input())
M = int(input())

# INF로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신은 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c


def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd()

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print("%-5s" % "INF", end=" ")
        else:
            print("%-5d" % graph[i][j], end=" ")
    print()
