# 아기 상어 2
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
answer = 0

# 모든 상어를 큐에 넣기
q = deque()
dist = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0  # 시작점 방문처리

# BFS
while q:
    x, y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# 모든 빈칸의 안전거리중 최댓값
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer = max(answer, dist[i][j])

print(answer)

"""
- 난이도: 실버2
- 분류: BFS

핵심
- 조건: 4방향이 아니라 8방향으로 이동 가능
- 효율성1: 빈칸(0)에서 출발하는게 아니라, 상어(1)에서 출발해서 최단거리를 계산 (역발상)
- 효율성2: 모든 시작점을 큐에 넣고 BFS를 딱 한번만 돌리기
"""
