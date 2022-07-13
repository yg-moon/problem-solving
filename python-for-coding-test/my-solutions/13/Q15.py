from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
# 간선 길이는 1로 동일하므로 생략
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 초기화, 출발 도시는 0.
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

check = False
for i in range(1, N + 1):
    if dist[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)
