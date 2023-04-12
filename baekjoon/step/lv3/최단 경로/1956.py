# 운동
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]
answer = INF

# 간선정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최소 사이클 찾기
for i in range(1, V + 1):
    answer = min(answer, graph[i][i])

print(answer if answer != INF else -1)

"""
- 난이도: 골드4
- 분류: 플로이드-워셜

핵심
- 플로이드-워셜을 응용해서 사이클을 찾을 수 있다.
- graph[i][i]를 0으로 초기화 하지 않고 INF로 두면 된다.
"""
