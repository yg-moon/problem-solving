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

# 플로이드 배열에서, 본인의 행+열에서 모든 학생이 한번이라도 등장하면 정확한 순위를 알 수 있다.
answer = 0
students = set([x for x in range(1, N + 1)])
for student in students:
    exists = set()
    for row in range(1, N + 1):
        if graph[row][student] != INF:
            exists.add(row)
    for col in range(1, N + 1):
        if graph[student][col] != INF:
            exists.add(col)
    if exists == students:
        answer += 1
print(answer)
