# BOJ 18352
# 출처: 이코테
from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
# 가중치는 모두 1이므로 생략
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 초기화 (출발점은 0)
dist = [-1] * (N + 1)
dist[X] = 0

# BFS
Q = deque([X])
while Q:
    curr = Q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[curr]:
        # 아직 방문하지 않은 도시라면
        if dist[next] == -1:
            # 최단 거리 갱신
            dist[next] = dist[curr] + 1
            Q.append(next)

has_answer = False
for i in range(1, N + 1):
    if dist[i] == K:
        print(i)
        has_answer = True
if not has_answer:
    print(-1)
