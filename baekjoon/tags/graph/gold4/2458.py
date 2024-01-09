# 키 순서
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자신으로 가는 경로는 0
for i in range(1, N + 1):
    graph[i][i] = 0

# 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜
for k in range(1, N + 1):  # 주의: k를 가장 먼저 써야 함
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 핵심: 다른 모든 곳으로 가는 경로가 하나라도 존재하면 됨
answer = 0
for i in range(1, N + 1):
    flag = True
    for j in range(1, N + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            flag = False
            break
    if flag:
        answer += 1

print(answer)

"""
- 난이도: 골드4
- 분류: 플로이드-워셜
- 소요 시간: 30분 (풀이 10분, 디버깅 20분)

- 전형적인 플로이드 문제
"""
