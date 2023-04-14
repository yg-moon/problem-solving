# 토마토
from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

q = deque()
answer = 0

# 처음 토마토 위치를 큐에 넣기
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                q.append([k, i, j])

# BFS
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append([nz, nx, ny])

# 그래프 전체를 돌면서 정답 구하기
for floor in graph:
    for row in floor:
        for r in row:
            if r == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(row))
print(answer - 1)

"""
- 난이도: 골드5
- 분류: BFS

- 요약: 3차원 그래프에서의 BFS
"""
