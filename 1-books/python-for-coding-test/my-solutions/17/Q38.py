# 출처: 이코테
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신은 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 플로이드 배열에서 본인의 행 or 열에서 연결된 개수를 세고, 전체 인원수와 같으면 순위 확정.
answer = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:
        answer += 1
print(answer)
